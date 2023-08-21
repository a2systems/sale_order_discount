##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import base64

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def btn_add_discount(self):
        self.ensure_one()
        if self.state not in ['draft','sent']:
            raise ValidationError(_('Pedido en estado incorrecto'))
        vals = {
                'order_id': self.id,
                }
        wizard_id = self.env['sale.order.discount.wizard'].create(vals)
        return {
            'name': _('Add Customer'),
            'res_model': 'sale.order.discount.wizard',
            'view_mode': 'form',
            'res_id': wizard_id.id,
            'type': 'ir.actions.act_window',
            'target': 'new',
        }

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for rec in self:
            for order_line in rec.order_line.filtered(lambda l: l.discount != 0):
                amt_discount = order_line.price_unit * order_line.product_uom_qty * order_line.discount / 100
                order_line.discount_amt_usd = order_line.currency_id._convert(
                        amt_discount,
                        self.env.ref('base.USD'),
                        order_line.company_id,
                        order_line.order_id.date_order,
                    )
        return res

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amt_usd = fields.Float('Monto Descuento USD',copy=False)
