# -*- coding: utf-8 -*-

{
    'name': 'Utu chemical invoice create',
    'category': '',
    'sequence': 5,
    'summary': 'utu billing',
    'version': '15.0.1',
    'license': 'LGPL-3',
    'price': '18.00',
    'currency': 'EUR',
    'author': 'Alphdevinfotech india pvt ltd',
    'website': 'https://alphadevinfotech.com/',
    'description': """
        """,
    'depends': ['account','website','web', 'mail','utm','sale_management'],
    'data': [
        'security/hrms_security_rule.xml',
        'views/all_menuitem_hide.xml',
        'reports/invoice_inherit_view.xml',

    ],
    'installable': True,
    'application': True,
}
