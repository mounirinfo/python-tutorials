from odoo import fields, models

class TestModelDataScan(models.Model):
    _name = "test.model.datascan"
    _description = "Test Model Datascan"

    name = fields.Char()
    quantite = fields.Char (string='Quantite')
    politique = fields.Selection ([
        ('enstock' , 'Stock'),
        (' alacommande' , 'Commande'),

    ], Required = True, Default= 'enstock')
