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


