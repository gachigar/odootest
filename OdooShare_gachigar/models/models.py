from odoo import models, fields, api


class LoadedFile(models.Model):
    _name = 'odooshare_gachigar.loadedfile'
    file_name = fields.Char()
    file_loaded = fields.Binary(string="File")
