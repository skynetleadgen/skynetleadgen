# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2023-today Botspot Infoware Pvt. Ltd. <www.botspotinfoware.com>
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
#################################################################################

{
    "name": "Employee's leads Comission",
    "author": "Botspot infoware Pvt. Ltd.",
    "category": "Employees",
    "summary": """Assign commissions to employees based on a percentage or fixed amount per expected revenue, facilitating easy commissioning for product expected revenue.""",
    "website": "https://www.botspotinfoware.com",
    "company": "Botspot Infoware Pvt. Ltd.",
    "maintainer": "Botspot Infoware Pvt. Ltd.",
    "description": """Assign commissions to employees based on a percentage or fixed amount per expected revenue, facilitating easy commissioning for product expected revenue.""",
    "versio": "17.1",
    "depends": ["base", "hr", "crm"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee_view.xml",
        "views/crm_commission_rule_view.xml",
        "wizard/lead_summary_wizard_view.xml",
        "reports/employee_lead_summary_action.xml",
        "reports/employee_lead_summary_template.xml",
    ],
    "images": ["static/description/Employee Leads Banner.gif"],
    "qweb": [],
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
}
