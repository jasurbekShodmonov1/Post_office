{
    'name': 'UIC POST Service',
    'version': '1.0',
    'summary': 'Postal Service Management System',
    'description': 'Module to manage postal services including order creation, delivery process, and status tracking.',
    'category': 'Operations/Inventory',
    'author': 'Jasurbek Shodmonov',
    'depends': ['base', 'website', 'sale', 'stock', 'loyalty'],
    'data': [
        'security/ir.model.access.csv',
        'views/postal_order_views.xml',
        'views/postal_order_menu.xml',
        'views/website_postal_status.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
