{
    'name': 'Sale round_off',
    'version': '17.0.1.0.0',
    'summary': 'Sale Extended module contains quotation types and Actual weight '
               'based shipping methods applied to the customer to charge the amounts to confirm the orders.',
    'sequence': 1,
    'description': """ Actual weight '
               'based shipping methods applied to the customer to charge """,
    'author': "AppsComp",
    'license': 'LGPL-3',
    'website': "http://www.appscomp.com",
    'category': 'sale quotation',
    'depends': ['sale'],
    'data': [
        'views/sale_view.xml',

    ],

    # 'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
