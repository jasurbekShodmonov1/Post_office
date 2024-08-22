from odoo import http

class PostalController(http.Controller):
    @http.route('/postal/status', type='http', auth='public', website=True)
    def check_status(self, invoice_id=None):
        if invoice_id:
            order = http.request.env['postal.order'].sudo().search([('invoice_id', '=', invoice_id)], limit=1)
            if order:
                return f"Status: {order.state}"
            else:
                return "Invoice ID not found."
        return "Please provide an Invoice ID."
