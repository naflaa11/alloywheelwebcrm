# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
from datetime import date
from odoo import api, exceptions, fields, models, _
from odoo.exceptions import AccessError, UserError
import pytz
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class Lead(models.Model):
    _inherit = "crm.lead"

    #
    # hunain=fields.Selection([('new', 'NEW'),
    #     ('qualified', 'Qualified'),
    #     ('quotation', 'Quotation'),
    #     ('won', 'Won'),
    #     ], 'Status')


    @api.onchange('stage_id')
    def _onchange_stage_id(self):
        values = self._onchange_stage_id_values(self.stage_id.id)
        self.update(values)
        groupObj = self.env['res.groups'].search([('name', '=', "User: Own Documents Only")])

        for i in groupObj.users:
            userObj = self.env['res.users'].search([('id', '=', i.id)])
            # print(userObj.name)

            if self.stage_id.name == 'Won':



                act_type_xmlid = 'mail.mail_activity_data_todo'
                date_deadline = datetime.now().strftime('%Y-%m-%d')
                summary = 'Won Lead Notification'
                note = 'This Lead is Won, Please take follow-up.'

                if act_type_xmlid:
                    activity_type = self.sudo().env.ref(act_type_xmlid)

                model_id = self.env['ir.model']._get(self._name).id

                create_vals = {
                    'activity_type_id': activity_type.id,
                    'summary': summary or activity_type.summary,
                    'automated': True,
                    'note': note,
                    'date_deadline': date_deadline,
                    'res_model_id': model_id,
                    'res_id': self._origin.id,
                    'user_id': userObj.id,

                }

                activities = self.env['mail.activity'].create(create_vals)

            if self.stage_id.name == 'Quotation':



                act_type_xmlid = 'mail.mail_activity_data_todo'
                date_deadline = datetime.now().strftime('%Y-%m-%d')
                summary = 'Quoation Notification'
                note = 'Your Lead Quotation is created, Please take follow-up.'

                if act_type_xmlid:
                    activity_type = self.sudo().env.ref(act_type_xmlid)

                model_id = self.env['ir.model']._get(self._name).id

                create_vals = {
                    'activity_type_id': activity_type.id,
                    'summary': summary or activity_type.summary,
                    'automated': True,
                    'note': note,
                    'date_deadline': date_deadline,
                    'res_model_id': model_id,
                    'res_id': self._origin.id,
                    'user_id': userObj.id,

                }
                activities = self.env['mail.activity'].create(create_vals)

            if self.stage_id.name == 'Qualified':

                act_type_xmlid = 'mail.mail_activity_data_todo'
                date_deadline = datetime.now().strftime('%Y-%m-%d')
                summary = 'Qualified Lead Notification'
                note = 'Your Lead is Qualified, Please take follow-up.'

                if act_type_xmlid:
                    activity_type = self.sudo().env.ref(act_type_xmlid)

                model_id = self.env['ir.model']._get(self._name).id

                create_vals = {
                    'activity_type_id': activity_type.id,
                    'summary': summary or activity_type.summary,
                    'automated': True,
                    'note': note,
                    'date_deadline': date_deadline,
                    'res_model_id': model_id,
                    'res_id': self._origin.id,
                    'user_id': self.user_id.id,

                }

                activities = self.env['mail.activity'].create(create_vals)

            else:
                pass

    @api.model
    def create(self, values):
        company = super(Lead, self).create(values)
        company._create_function()
        return company

    @api.multi
    def _create_function(self):

            groupObj = self.env['res.groups'].search([('name', '=', "User: Own Documents Only")])

            for i in groupObj.users:
                userObj = self.env['res.users'].search([('id', '=', i.id)])
                act_type_xmlid = 'mail.mail_activity_data_todo'
                date_deadline = datetime.now().strftime('%Y-%m-%d')
                summary = 'New Lead Notification'
                note = 'New Lead is created, Please take follow-up.'

                if act_type_xmlid:
                    activity_type = self.sudo().env.ref(act_type_xmlid)

                model_id = self.env['ir.model']._get(self._name).id

                create_vals = {
                    'activity_type_id': activity_type.id,
                    'summary': summary or activity_type.summary,
                    'automated': True,
                    'note': note,
                    'date_deadline': date_deadline,
                    'res_model_id': model_id,
                    'res_id': self.id,
                    'user_id': userObj.id,

                }

                activities = self.env['mail.activity'].create(create_vals)



    @api.multi
    def action_set_lost(self):
        """ Lost semantic: probability = 0, active = False """

        self.probability=0
        self.active=False

        groupObj = self.env['res.groups'].search([('name', '=', "User: Own Documents Only")])

        for i in groupObj.users:
            userObj = self.env['res.users'].search([('id', '=', i.id)])

            act_type_xmlid = 'mail.mail_activity_data_todo'
            date_deadline = datetime.now().strftime('%Y-%m-%d')
            summary = 'Lost Lead Notification'
            note = 'Your Lead is Lost, Please take follow-up.'

            if act_type_xmlid:
                activity_type = self.sudo().env.ref(act_type_xmlid)

            model_id = self.env['ir.model']._get(self._name).id

            create_vals = {
                'activity_type_id': activity_type.id,
                'summary': summary or activity_type.summary,
                'automated': True,
                'note': note,
                'date_deadline': date_deadline,
                'res_model_id': model_id,
                'res_id': self.id,
                'user_id': userObj.id,

            }
            activities = self.env['mail.activity'].create(create_vals)

#
# class SaleOrder_lead(models.Model):
#     _inherit = "sale.order"
#
#     @api.multi
#     def action_confirm(self):
#
#         groupObj = self.env['res.groups'].search([('name', '=', "User: Own Documents Only")])
#
#
#
#         for i in groupObj.users:
#             print(i.name)
#             userObj = self.env['res.users'].search([('id', '=', i.id)])
#
#             act_type_xmlid = 'mail.mail_activity_data_todo'
#             date_deadline = datetime.now().strftime('%Y-%B-%d')
#             summary = 'Quotation Lead Notification'
#             note = 'Quotation is sent, Please take follow-up.'
#
#             if act_type_xmlid:
#                 activity_type = self.sudo().env.ref(act_type_xmlid)
#
#             model_id = self.env['ir.model']._get(self._name).id
#
#             create_vals = {
#                 'activity_type_id': activity_type.id,
#                 'summary': summary or activity_type.summary,
#                 'automated': True,
#                 'note': note,
#                 'date_deadline': date_deadline,
#                 'res_model_id': model_id,
#                 'res_id': self.id,
#                 'user_id': userObj.id,
#
#             }
#             activities = self.env['mail.activity'].create(create_vals)
#
#
#
#
#
