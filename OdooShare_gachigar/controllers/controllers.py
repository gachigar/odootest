# -*- coding: utf-8 -*-
import base64
from odoo import http
import werkzeug


class TestModule(http.Controller):
    @http.route('/upload/', website=True, auth='public')
    def index(self, **kw):
        return http.request.render('OdooShare_gachigar.index', {
            'files': http.request.env['odooshare_gachigar.loadedfile'].sudo().search([])
        })

    @http.route(['/upload_file/'], type='http', auth='user', website=True)
    def upload_file(self, redirect=None, **post):
        name = post.get('attachment').filename
        file = post.get('attachment')
        lf = http.request.env['odooshare_gachigar.loadedfile']
        lf.create(vals_list=[{'file_loaded': base64.b64encode(file.read()),
                              'file_name': name}])
        return werkzeug.utils.redirect('/upload/')

    @http.route('/web/binary/download_file/<id>/<filename>', type='http', auth="public", website=True)
    def download_file(self, id, **kw):
        obj = http.request.env['odooshare_gachigar.loadedfile'].sudo().search([
            ('id', '=', id)])
        data = base64.b64decode(obj.file_loaded)
        return http.request.make_response(data, [('Content-Type', 'application/octet-stream'),
                                                 ('Content-Disposition', obj.file_name)])
