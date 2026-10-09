from odoo import api, fields, models
from datetime import timedelta
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real estate property offer"
    # _sql_constraints = [
    #     (
    #         "check_offer_price",
    #         "CHECK(price > 0)",
    #         "The offer price must be strictly positive.",
    #     ),
    # ]
    _check_offer_price = models.Constraint(
        "CHECK(price > 0)",
        "The offer price must be strictly positive.",
    )
    
    _order = "price desc"
    
    price = fields.Float()
    status = fields.Selection(selection=[
                ('accepted', 'Accepted'),
                ('refused', 'Refused'),
            ], copy=False)
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    property_type_id = fields.Many2one(
        "estate.property.type", 
        related="property_id.property_type_id",
        store=True,
    )
    
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline",inverse="_inverse_date_deadline")
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            base_date = record.create_date or fields.Datetime.now()
            record.date_deadline = base_date.date() + timedelta(days=record.validity)
            
    def _inverse_date_deadline(self):
        for record in self:
            base_date = record.create_date or fields.Datetime.now()
            record.validity = (record.date_deadline - base_date.date()).days
            
    def action_accept(self):
        for record in self:
            accepted_offers = self.search([
                ("property_id", "=", record.property_id.id),
                ("status", "=", "accepted"),
                ("id", "!=", record.id),
            ])

            if accepted_offers:
                raise UserError(
                    "Only one offer can be accepted for a property."
                )

            record.status = "accepted"
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price
            record.property_id.state = "offer_accepted"

    def action_refuse(self):
        for record in self:
            record.status = "refused"        
        
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            property_record = self.env["estate.property"].browse(
                vals["property_id"]
            )

            if property_record.offer_ids:
                highest_offer = max(property_record.offer_ids.mapped("price"))

                if vals["price"] < highest_offer:
                    raise UserError(
                        "The offer price cannot be lower than an existing offer."
                    )

            property_record.state = "offer_received"

        return super().create(vals_list)