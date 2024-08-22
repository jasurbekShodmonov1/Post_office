from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError


class PostalOrder(models.Model):
    _name = 'postal.order'
    _description = 'Postal Order'

    invoice_id = fields.Char(string="Invoice ID")
    weight = fields.Float(string="Weight (kg)")
    volume = fields.Float(string="Volume (m3)")
    price = fields.Float(string="Price", compute="_compute_price")
    state = fields.Selection([
        ('draft', 'Qabul qilinmoqda'),
        ('in_stock', 'Skladda'),
        ('in_transit', 'Yetkazib berish jarayonida'),
        ('delivered', 'Yetkazib berildi'),
        ('damaged', 'Shikastlangan'),
    ], string="State", default='draft')

    # Define the delivery_id field to establish a relationship
    delivery_id = fields.Many2one('delivery.process', string="Delivery Process")

    @api.depends('weight', 'volume')
    def _compute_price(self):
        for order in self:
            price = 15000  # Default for up to 1kg
            if order.weight > 1:
                price += 1000 * (min(order.weight, 5) - 1)
            if order.weight > 5:
                price += 1000 * (min(order.weight, 30) - 5)
            if order.weight > 30:
                price += 2000 * (order.weight - 30)

            if order.volume > 1:
                price += 30000

            if order.volume > 2:
                raise ValidationError("2 metr/kub dan yuqori yuklar qabul qilinmaydi")

            order.price = price

    def check_status(self):
        order = self.search([('invoice_id', '=', self.invoice_id)], limit=1)
        if order:
            return order.state
        else:
            return "Invoice ID not found."

    def check_damages(self):
        return False  # Return True if damaged
