from odoo import api, fields, models, _
from odoo.exceptions import AccessError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_enabled_roundoff = fields.Boolean('Enabled Roundoff',
                                         default=lambda self: self.env["ir.config_parameter"].sudo().get_param(
                                             "account.invoice_roundoff"))
    amount_round_off = fields.Monetary(string='Roundoff Amount', store=True, readonly=True, compute='_amount_all')
    apply_round_off = fields.Boolean('Apply Round Off', default=False)

    # @api.onchange('is_enabled_roundoff')
    # def onchange_is_enabled_roundoff(self):
    #     print("is_enabled_roundoff11111111111111111111111111111111111")
    #     self._amount_all()

    @api.depends('order_line.price_total')
    def _amount_all(self):
        print("order_line.price_total2222222222222222222222222222222222")
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            print("order_line.price_total2222222222221111111111111111111111111111")
            amount_untaxed = amount_tax = 0.0;
            amount_round_off = 0.0
            for line in order.order_line:
                print("order_line.price_total222222222222111111111111111111111111111122222222222222222222222")
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax,
            })
            print("order_line.price_total222222222222111111111111111111111111111133333333333333333333333")
            if order.apply_round_off == True:
                print("order_line.price_total222222222222111111111111111111111111111144444444444444444444444")
                if order.is_enabled_roundoff == True:
                    print("order_line.price_total22222222222211111111111111111111111111115555555555555")
                    amount_total = round((order.amount_total))
                    if order.amount_total:
                        print(
                            "order_line.price_total222222222222111111111111111111111111111166666666666666666666666666666")
                        amount_round_off = amount_total - order.amount_total
                        order.update({
                            'amount_total': amount_total,
                            'amount_round_off': amount_round_off})
                        print(
                            "order_line.777777777777777777777777777777777777777777777777")
                    else:
                        print(
                            "order_line.price_total2222222222221111111111111111111111111111777777777777777777")
                        order.update({
                            'amount_total': 0.00,
                            'amount_round_off': 0.00})
