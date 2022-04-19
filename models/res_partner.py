# coding: utf-8
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = ["multi.company.abstract", "res.partner"]
    _name = "res.partner"

    company_ids = fields.Many2many(
        string="Companies",
        comodel_name="res.company",
        default=lambda self: self._default_company_ids(),
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        compute="_compute_company_id",
        inverse="_inverse_company_id",
        search="_search_company_id",
        default="_default_company_id",
    )

    def _default_company_id(self):
        return self.browse(self.env.company.ids)