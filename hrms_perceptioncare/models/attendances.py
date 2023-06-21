from odoo import fields, models, api
from lxml import etree, html
from datetime import datetime,time


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(HrAttendance, self).fields_view_get(view_id, view_type, toolbar=toolbar, submenu=False)
        doc = etree.XML(res['arch'])
        context = self._context
        current_uid = context.get('uid')
        user = self.env['res.users'].browse(current_uid)
        if user.id != 2:
            if view_type == 'tree':
                tree_nodes = doc.xpath("//tree")
                for tree in tree_nodes:
                    tree.set('create', '0')
                    tree.set('edit', '0')
                    tree.set('delete', '0')
            if view_type == 'kanban':
                from_nodes = doc.xpath("//kanban")
                for form in from_nodes:
                    form.set('create', '0')
                    form.set('edit', '0')
                    form.set('delete', '0')

            res['arch'] = etree.tostring(doc)
        return res

    def pc_hr_attendance_closed(self):
        emp_attendance = self.env['hr.attendance'].search([('check_out', '=', False)])
        print(">>>>>>>>>>>>>self",emp_attendance)
        for emp_attn in emp_attendance:
            if emp_attn:
                current_datetime = datetime.now()
                time_obj = time(20, 0)
                date = datetime.now()
                datetime_obj = datetime.combine(datetime.today().date(), time_obj)
                formatted_datetime = datetime_obj.strftime("%Y-%m-%d %I:%M:%S")
                datetime_obj = current_datetime.strftime("%Y-%m-%d %I:%M:%S")
                print("demo1==================",formatted_datetime == datetime_obj)
                print("demo2==================",formatted_datetime)
                print("demo3==================",datetime_obj)
                if formatted_datetime == datetime_obj:
                    print(">>>>>>>>>>>>>>>>>>>>>>>>if if if")
                    emp_attn.write({
                        'check_out': date.strftime("%Y-%m-%d %I:%M:%S"),
                    })

