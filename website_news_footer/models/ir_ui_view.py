from openerp.osv import osv
from openerp.http import request
from openerp import SUPERUSER_ID
from openerp.addons.website.models import website


class view(osv.osv):
    _inherit = "ir.ui.view"
    
    def _prepare_qcontext(self, cr, uid, context=None):
        qcontext = super(view, self)._prepare_qcontext(cr, uid, context=context)
        news_feed_latest = request.env['news.feed'].search([])[-3:]
        qcontext.update({'news_feed' : news_feed_latest})
        return qcontext