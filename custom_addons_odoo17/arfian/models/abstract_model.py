from odoo import models, fields

class ArfianAbstract(models.AbstractModel):
    _name = "arfian.abstract"
    _description = "Arfian Abstract"

    generate_description = fields.Text()
    instructor_id = fields.Many2one(
        comodel_name="res.users",
        string="Instructor",
        ondelete="restrict",
        required=True
    )

    def _custom_abstract_model_function(self):
        return