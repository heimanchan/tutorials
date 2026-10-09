from odoo import api, fields, models

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

    _order = "sequence, name"
    
    
    name = fields.Char('Type', required=True)
    
    property_ids = fields.One2many( "estate.property", "property_type_id")
    sequence = fields.Integer()
    offer_ids = fields.One2many(
        "estate.property.offer",
        "property_type_id",
    )
    
    offer_count = fields.Integer(
        compute="_compute_offer_count"
    )
    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)