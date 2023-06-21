from odoo import fields, models, api
from lxml import etree, html


class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(HrEmployee, self).fields_view_get(view_id, view_type, toolbar=toolbar, submenu=False)
        doc = etree.XML(res['arch'])
        print("doc.................",doc)
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
            if view_type == 'form':
                from_nodes = doc.xpath("//form")
                for form in from_nodes:
                    form.set('create', '0')
                    form.set('edit', '0')
                    form.set('delete', '0')
                    form.set('inactive', '1')
            if view_type == 'kanban':
                from_nodes = doc.xpath("//kanban")
                for form in from_nodes:
                    form.set('create', '0')
                    form.set('edit', '0')
                    form.set('delete', '0')
            res['arch'] = etree.tostring(doc)
        return res






