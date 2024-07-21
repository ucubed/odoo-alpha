import datetime
import pytz
from odoo import http, models, fields, api, tools
from odoo.http import request

class BackThemeBits(http.Controller):
    @http.route(['/get/menu_data'], type='json', auth='public')
    def get_irmenu_icondata(self, **kw):
        menuobj = request.env['ir.ui.menu']
        menu_recs = request.env['ir.ui.menu'].sudo().search(
            [('id', 'in', kw.get('menu_ids'))])

        app_menu_dict = {}
        for menu in menu_recs:
            menu_dict = menu.read(set(menuobj._fields))
            app_menu_dict[menu.id] = menu_dict
        return app_menu_dict