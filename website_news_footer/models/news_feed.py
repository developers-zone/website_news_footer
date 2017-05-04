# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2016 Odoo Developers
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
from datetime import datetime, timedelta
from openerp import api, fields, models

class NewsFeed(models.Model):
    _name = "news.feed"
    _description = "News Feed"
    
    name = fields.Char(string='News Title', required=True)
    date_order = fields.Datetime(string='Created Date', required=True, readonly=True, default=fields.Datetime.now)
    user_id = fields.Many2one('res.users', string='Created User', track_visibility='onchange', default=lambda self: self.env.user)
    note = fields.Text('News Feed')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: