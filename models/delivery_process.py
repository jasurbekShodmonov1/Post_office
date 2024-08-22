from odoo import models, fields, api

class DeliveryProcess(models.Model):
    _name = 'delivery.process'
    _description = 'Delivery Process'

    order_ids = fields.One2many('postal.order', 'delivery_id', string="Orders")

    def start_delivery(self):
        for order in self.order_ids:
            order.state = 'in_transit'

    def complete_delivery(self):
        for order in self.order_ids:
            if not order.check_damages():
                order.state = 'delivered'
            else:
                order.state = 'damaged'
                self.env['res.users'].search([('is_admin', '=', True)]).message_post(
                    body=f"Order {order.id} is damaged or lost."
                )
