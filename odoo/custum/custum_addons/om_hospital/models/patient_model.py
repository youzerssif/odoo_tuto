from odoo import models, fields, api


class PatientModel(models.Model):
    _name = 'patient.model'
    _description = 'Patient model'

    name = fields.Char()
    age = fields.Integer()
    gender = fields.Char()
    description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100