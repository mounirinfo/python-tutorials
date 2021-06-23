from odoo import api, fields, models

class SaleOrder(models.Model):
    _inharit = "sale.order"

    sale_description = fields.Char()
    