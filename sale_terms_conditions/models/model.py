from odoo import api, fields, models


#
class ResCompany(models.Model):
    _inherit = "res.company"

    sale_terms = fields.Html(
        string="Default Terms and Conditions", translate=True, store=True
    )
    use_sale_terms = fields.Boolean(
        readonly=False,
        store=True
    )


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    use_sale_terms = fields.Boolean(
        related="company_id.use_sale_terms",
        readonly=False,

    )
    sale_terms = fields.Html(
        related="company_id.sale_terms",
        string="sale Terms & Conditions",
        readonly=False,
    )


#
class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def _default_note(self):
        if self.env.company.sale_terms:
            return self.env.company.sale_terms
        else:
            return False


    note = fields.Html("Terms and conditions", default=_default_note)
