##############################################################################
#
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'sale_order_discount',
    'description': 'Sale Order Discount',
    'license': 'AGPL-3',
    'category': 'Sale',
    'data': [
        'sale_view.xml',
        'security/ir.model.access.csv',
        'wizard/wizard_view.xml'
    ],
    'demo': [
    ],
    'depends': [
        'base',
        'account',
        'sale',
        'stock',
        'product',
        'sales_team',
    ],
    'installable': True,
    'test': [],
    'version': '16.0.1.1.0',
}
