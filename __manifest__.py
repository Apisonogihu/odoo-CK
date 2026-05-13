{
    'name': 'Library Portal',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Library Portal for Book Borrowing',
    'description': 'Module for library website, providing public routes and APIs for borrowing books.',
    'author': 'Group 7',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
