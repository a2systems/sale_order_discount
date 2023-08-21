from odoo import fields,models, api, _
from odoo.exceptions import UserError, ValidationError
import logging
from datetime import date

_logger = logging.getLogger(__name__)

class SaleOrderDiscountWizard(models.TransientModel):
    _name = 'sale.order.discount.wizard'
    _description = 'sale.order.discount.wizard'

    order_id = fields.Many2one('sale.order','Orden de venta')
    discount = fields.Float('Descuento')
    discount_amount = fields.Float('Monto Descuento')

    def btn_confirm(self):
        if not self.order_id:
            raise ValidationError('No hay orden presente')
        if self.discount > 100 or self.discount <= 0:
            raise ValidationError('Debe ingresar el descuento')
        for order_line in self.order_id.order_line:
            order_line.discount = self.discount
