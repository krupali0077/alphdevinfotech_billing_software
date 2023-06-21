# -*- coding: utf-8 -*-

{
    'name': 'Only invoice billing create',
    'category': '',
    'sequence': 5,
    'summary': '',
    'version': '15.0.1',
    'license': 'LGPL-3',
    'currency': 'EUR',
    'author': 'Alphdevinfotech india pvt ltd',
    'website': 'http://alphadevinfotech.com',
    'description': """
        """,
    'depends': ['account','website','web', 'mail','utm'],
    'data': [
        'security/hrms_security_rule.xml',
        'views/all_menuitem_hide.xml',

    ],
    'installable': True,
    'application': True,
}
