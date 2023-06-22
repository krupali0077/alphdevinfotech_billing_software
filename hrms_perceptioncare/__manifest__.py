# -*- coding: utf-8 -*-

{
    'name': 'HRMS',
    'category': '',
    'sequence': 5,
    'summary': 'HRMS',
    'version': '15.0.1',
    'license': 'LGPL-3',
    'price': '18.00',
    'currency': 'EUR',
    'author': 'perception care india pvt ltd',
    'website': 'https://perceptioncare.com/',
    'description': """
        """,
    'depends': ['account','website','web', 'mail','utm'],
    'data': [
        'security/hrms_security_rule.xml',
        'views/all_menuitem_hide.xml',
        'reports/invoice_inherit_view.xml',

    ],
    'installable': True,
    'application': True,
}
