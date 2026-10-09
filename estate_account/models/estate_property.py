from odoo import models

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_sold(self):
        print("Estate Account: action_sold called")
        
        self.ensure_one()

        invoice_lines = [
            (0, 0, {
                "name": "Selling commission (6%)",
                "quantity": 1,
                "price_unit": self.selling_price * 0.06,
            }),
            (0, 0, {
                "name": "Administrative fees",
                "quantity": 1,
                "price_unit": 100.00,
            }),
        ]
        
        invoice = self.env["account.move"].create({
            "partner_id": self.buyer_id.id,
            "move_type": "out_invoice",
            "invoice_line_ids": invoice_lines,
        })
        return super().action_sold()