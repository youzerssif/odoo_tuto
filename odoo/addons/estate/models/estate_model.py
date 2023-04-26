from odoo import fields, models

class EstateModel(models.Model):
    _name = "estate.model"
    _description = "Test Model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('NORTH', 'North'), ('SOUTH', 'South'), ('EAST', 'East'), ('WEST', 'West')], string='My Selection Field')
    
    