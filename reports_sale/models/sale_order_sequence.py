from collections import defaultdict
from datetime import timedelta
from itertools import groupby

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.fields import Command
from odoo.osv import expression
from odoo.tools import float_is_zero, format_amount, format_date, html_keep_url, is_html_empty
from odoo.tools.sql import create_index

from odoo.addons.payment import utils as payment_utils


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    sale_order_create = fields.Boolean(string='Create')
    quotation_no = fields.Char(string='Quotation')
    order_seq_no = fields.Char(string='Order')

    def action_confirm(self):
        res = super().action_confirm()

        if not self.sale_order_create:
            self.quotation_no = self.name
            self.name = self.env['ir.sequence'].next_by_code('sale.order.quotation')
            self.order_seq_no = self.name
            self.sale_order_create = True
        else:
            self.name = self.order_seq_no
        return res

    def action_draft(self):
        res = super().action_draft()
        self.name = self.quotation_no
        return res