from odoo import api, fields, models, _
from odoo.exceptions import AccessError
import subprocess


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def sale_order_line_tax_calculation(self, line):
        print("111111startibgggggggggggggggggg11111111111111")
        value = {'CGST': {'per': 0.0, 'value': 0.0},
                 'SGST': {'per': 0.0, 'value': 0.0},
                 # 'KFC': {'per': 0.0, 'value': 0.0},
                 'IGST': {'per': 0.0, 'value': 0.0}
                 }
        for i in line.tax_id:
            print("11111111111111111111")
            if i.tax_group_id.id == self.env.ref('account.1_gst_group').id and i.amount_type == 'group':
                for j in i.children_tax_ids:
                    print("4444444444444444444444", j)
                    if j.tax_group_id.id == self.env.ref('account.1_cgst_group').id:
                        value['CGST']['per'] += j.amount
                        print("amou22222222222222222222nt", j.amount)
                    if j.tax_group_id.id == self.env.ref('account.1_sgst_group').id:
                        value['SGST']['per'] += j.amount
                        print("amou22222222222222222222nt", j.amount)
            elif i.tax_group_id.id == self.env.ref('account.1_igst_group').id and i.amount_type == 'percent':
                value['IGST']['per'] += i.amount
            # elif i.tax_group_id.name == "KFC" and i.amount_type == 'percent':
            #     value['KFC']['per'] += i.amount

        value['CGST']['value'] += (line.price_subtotal / 100) * value['CGST']['per']
        value['SGST']['value'] += (line.price_subtotal / 100) * value['SGST']['per']
        value['IGST']['value'] += (line.price_subtotal / 100) * value['IGST']['per']
        # value['KFC']['value'] += (line.price_subtotal / 100) * value['KFC']['per']
        value['CGST']['value'] = "{:.3f}".format(value['CGST']['value'])
        value['SGST']['value'] = "{:.3f}".format(value['SGST']['value'])
        # value['KFC']['value'] = "{:.3f}".format(value['KFC']['value'])
        value['IGST']['value'] = "{:.3f}".format(value['IGST']['value'])
        return value
