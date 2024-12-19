# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Arfian(models.Model):
    _name = "arfian"
    _inherit = ["arfian.abstract", "mail.thread"]
    _description = "Modul Saya Sendiri"

    name = fields.Char(string="Name", index=True, size=100, trim=True)
    total = fields.Integer(string="Total", tracking=True)
    description = fields.Text(string="Description", translate=True)
    user_id = fields.Many2one(comodel_name="res.users", string="User", ondelete="restrict", tracking=True)
    total_compute = fields.Float(
        compute="_value_pc", store=True, string="Total Compute", tracking=True
    )
    tags_ids = fields.Many2many(
        comodel_name="res.partner.category",
        relation="arfian_res_partner_category_rel",
        column1="arfian_id",
        column2="partner_category_id",
        string="Tags"
    )
    arfian_line = fields.One2many(
        comodel_name="arfian.line",
        inverse_name="arfian_id",
        string="Arfian Line"
    )
    active = fields.Boolean(string="Active", default=True)
    company_id = fields.Many2one(comodel_name="res.company", string="Company", tracking=True)

    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    price_total = fields.Monetary(
        compute="_compute_total",
        store=True,
        string="Price Total",
        currency_field="currency_id",
        tracking=True
    )
    attachment = fields.Binary(string="Attachment", attachment=False)
    icon_image = fields.Image(string="Icon Image", max_height=1024, max_width=1024)
    note = fields.Html(string="Note")
    date_only = fields.Date(string="On Date", default=fields.Date.today())
    start_date = fields.Datetime(string="Start Date", default=fields.Datetime.now())
    end_date = fields.Datetime(string="End Date")
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("ready", "Ready"),
            ("done", "Done"),
            ("cancel", "Cancel")
        ],
        string="Status", default="draft", required=True, tracking=True
    )
    ref = fields.Reference(string="Reference", selection=[("res.partner", "Partner")])
    model_name = fields.Char(string="Model")
    res_id = fields.Many2oneReference(string="Res ID", model_name="model_name")

    @api.depends('total')
    def _value_pc(self):
        for record in self:
            record.total_compute = float(record.total) / 100
            record.price_total = record.total_compute

    def action_confirm(self):
        """Change state to ready"""
        self.ensure_one()  # Pastikan hanya satu record diproses
        self.state = 'ready'

    def action_done(self):
        """Change state to done"""
        self.ensure_one()
        self.state = 'done'

    def action_cancel(self):
        """Change state to cancel"""
        self.ensure_one()
        self.state = 'cancel'

    def action_view_sales(self):
        return

    # ORM API CRUD
    @api.model_create_multi
    def create(self, vals_list):
        olah_data = vals_list
        res = super().create(vals_list)
        olah_data = res
        return res

    def read(self, fields=None, load='_classic_read'):
        return super().read(fields=fields, load=load)

    def write(self, vals):
        olah_data = vals
        res = super().write(vals)
        olah_data = res
        return res

    def unlink(self):
        # custom code
        return super().unlink()

class ArfianLine(models.Model):
    _name = "arfian.line"
    _description = "Table Child"

    name = fields.Char(string="Name")
    arfian_id = fields.Many2one(comodel_name="arfian", string="Arfian Parent", ondelete="cascade")
    qty = fields.Integer(string="Total")
    price_unit = fields.Integer(string="Price Unit")

