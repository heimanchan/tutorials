from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real estate properties"

    name = fields.Char('Property Name', required=True)
    description = fields.Text('Property Description')
    postcode = fields.Char('Property Zip Code')
    date_availability = fields.Date()
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Type',
        selection=[('east', 'East'), 
                   ('south', 'South'), 
                   ('west', 'West'), 
                   ('north', 'North')])
