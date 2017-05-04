# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016-present Odoo Developers.
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
import openerp
from openerp import http, SUPERUSER_ID
from openerp.http import request

PPG = 20 # Products Per Page
PPR = 4  # Products Per Row


class WebsiteNewsFeed(http.Controller):
    
    @http.route(['/news/<int:news_feed>'], type='http', auth="public", website=True)
    def news_indetailed(self, news_feed=None):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
 
        news_feed_obj = request.env['news.feed'].browse([news_feed])
#         news_feed = news_feed_obj.search([])
#         print news_feed.note,"1="*88
        
        return request.website.render('website_news_footer.news_feed', {'news_detailed': news_feed_obj})
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: