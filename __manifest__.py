# Copyright 2015-2016 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Partner multi-company",
    "summary": "Select individually partner visibility on each " "company",
    "author": "Gabosoft," "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/multi-company",
    "category": "Product Management",
    "version": "15.0.2.0.1",
    "license": "AGPL-3",
    "depends": ["base_multi_company", "contacts"],
    "data": [
        "views/res_partner_views.xml",
        "security/partner_multi_company_security.xml",
    ],
}
