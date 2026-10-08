from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real estate properties type"
    # _sql_constraints = [
    #     (
    #         "unique_property_type_name",
    #         "UNIQUE(name)",
    #         "The property type name must be unique.",
    #     ),
    # ]
    _unique_property_type_name = models.Constraint(
        "UNIQUE(name)",
        "The property type name must be unique.",
    )

    _order = "name"
    
    
    name = fields.Char('Type', required=True)
    
    property_ids = fields.One2many( "estate.property", "property_type_id")