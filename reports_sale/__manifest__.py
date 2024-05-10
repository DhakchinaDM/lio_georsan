{
    'name': 'Reports Sale Order',
    'version': '17.0.1.0.1',
    'license': 'LGPL-3',
    'depends': [
        'sale','sale_crm',
    ],
    'data': [
        'views/sale_report.xml',
        'views/ir_sequence.xml',
        'views/crm_actual_value.xml',
        'views/sale_order_sequencs.xml',

    ],
    # 'images': [
    #     'static/description/banner.png',
    # ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
