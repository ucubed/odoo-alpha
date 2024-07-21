# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def menu_ascending(self):
        records = self.env['ir.ui.menu'].search([('parent_id', '=', False)], order="name")
        count = 10
        for alpha in records:
            alpha.write({'sequence': count})
            count = count + 1
        records._copy_sequence()
        return True


class menu_items_aplha(models.Model):
    _inherit = 'ir.ui.menu'

    old_alpha = fields.Integer(string="Old Sequence", compute='_copy_sequence', store=True)

    @api.depends('sequence')
    def _copy_sequence(self):
        for alpha in self:
            if not alpha.old_alpha or alpha.old_alpha == 0:
                alpha.old_alpha = alpha.sequence
            else:
                return False
