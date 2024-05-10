from odoo import api, fields, models, _
from odoo.exceptions import AccessError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    actual_value = fields.Monetary(string='Actual Value ',
                                   currency_field='company_currency',
                                   default=0.0,
                                   help='Help text for your monetary field',
                                   group_operator="sum", compute='_compute_actual_value_sale')


    @api.depends('order_ids')
    def _compute_actual_value_sale(self):
        act_val = ''
        for i in self:
            for j in i.order_ids:
               act_val = j.amount_total
            i.actual_value = act_val
