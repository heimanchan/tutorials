from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real estate property tag"
    # _sql_constraints = [
    #     (
    #         "unique_tag_name",
    #         "UNIQUE(name)",
    #         "The tag name must be unique.",
    #     ),
    # ]
    _unique_tag_name = models.Constraint(
        "UNIQUE(name)",
        "The tag name must be unique.",
    )
    
    _order = "name"
    
    name = fields.Char('Tag', required=True)
    color = fields.Integer()
    