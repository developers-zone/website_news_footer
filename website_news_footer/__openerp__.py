# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2016 Odoo Developers.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Website News Footer',
    'version': '3.0',
    'category': 'Website',
    'summary' : "Latest news created by users will be shown in website footer side !!",
    'description': """
    News will be shown in website created by users !!
    """,
    'author': 'Odoo Developers',
    'depends': ['base','website'], 
    'data': [
            'security/ir.model.access.csv',
            'views/news_feed_view.xml',
            'views/website_templates.xml'
    ],
    'images': ['static/src/img/banner.jpg'],
    'live_test_url': '/static/description/',
    'price': 19.99,
    'currency' : "EUR",
    'installable': True,
    'auto_install': False,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
