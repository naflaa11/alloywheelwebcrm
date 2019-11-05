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


    @api.onchange('stage_id')
    def _onchange_stage_id(self):
        values = self._onchange_stage_id_values(self.stage_id.id)
        self.update(values)
        # print(self._origin.id)
        groupObj = self.env['res.groups'].search([('name', '=', "User: Own Documents Only")])

        if self.stage_id.name == 'Qualified':

            act_type_xmlid = 'mail.mail_activity_data_todo'
            date_deadline = datetime.now().strftime('%Y-%B-%d')
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
            # print("Hello 2")
            activities = self.env['mail.activity'].create(create_vals)

            # print(create_vals)

        for i in groupObj.users:
            userObj = self.env['res.users'].search([('id', '=', i.id)])
            # print(userObj.name)

            if self.stage_id.name == 'Won':

                act_type_xmlid = 'mail.mail_activity_data_todo'
                date_deadline = datetime.now().strftime('%Y-%B-%d')
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
                # print("Hello 2")
                activities = self.env['mail.activity'].create(create_vals)

                # print(create_vals)

        for i in groupObj.users:
            userObj = self.env['res.users'].search([('id', '=', i.id)])
            # print(userObj.name)

            if self.stage_id.name == 'Qualified':

                act_type_xmlid = 'mail.mail_activity_data_todo'
                date_deadline = datetime.now().strftime('%Y-%B-%d')
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
                    'user_id': userObj.id,

                }
                # print("Hello 2")
                activities = self.env['mail.activity'].create(create_vals)

                # print(create_vals)



    @api.multi
    def action_set_lost(self):
        """ Lost semantic: probability = 0, active = False """

        self.probability=0
        self.active=False

        groupObj = self.env['res.groups'].search([('name', '=', "User: Own Documents Only")])

        print(self.id)

        for i in groupObj.users:
            userObj = self.env['res.users'].search([('id', '=', i.id)])




            act_type_xmlid = 'mail.mail_activity_data_todo'
            date_deadline = datetime.now().strftime('%Y-%B-%d')
            summary = 'Lost Lead Notification'
            note = 'Your Lead is Lost, Please take follow-up.'

            if act_type_xmlid:
                activity_type = self.sudo().env.ref(act_type_xmlid)

            model_id = self.env['ir.model']._get(self._name).id
            print(model_id)

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

    # @api.model
    # def group_b_users(self):
    #
    #     groupObj = self.env['res.groups'].search([('name', '=', "User: Own Documents Only")])
    #
    #     print(self.id)
    #
    #     for i in groupObj.users:
    #         userObj = self.env['res.users'].search([('id', '=', i.id)])
    #
    #         user_id=i.id


class SaleOrder_lead(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_confirm(self, vals):

        groupObj = self.env['res.groups'].search([('name', '=', "User: Own Documents Only")])



        for i in groupObj.users:
            print(i.name)
            userObj = self.env['res.users'].search([('id', '=', i.id)])

            act_type_xmlid = 'mail.mail_activity_data_todo'
            date_deadline = datetime.now().strftime('%Y-%B-%d')
            summary = 'Quotation Lead Notification'
            note = 'Quotation is sent, Please take follow-up.'

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





