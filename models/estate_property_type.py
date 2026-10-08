from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real estate properties type"
    _sql_constraints = [
        (
            "unique_property_type_name",
            "UNIQUE(name)",
            "The property type name must be unique.",
        ),
    ]

    
    name = fields.Char('Type', required=True)
    