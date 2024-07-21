{
    "name": "Clarity Backend Theme for community",
    "version": "17.0.1.0.1",
    'author': "Terabits Technolab",
    'summary': """   
        Clarity backend theme  
        Odoo Backend Theme, Odoo Community Backend Theme, Web backend Theme, Web Responsive Odoo Theme, New theme design, New design, Multi Level Menu,
        Web Responsive , Odoo Theme, Odoo Modern Theme, Odoo Modern Backend Theme Odoo, Advance Theme Backend Advanced, Left sidebar menu,
        All in one, New advanced Odoo Menu, Sidebar apps, Web menu, Odoo backend menu, Web Responsive menu, Sidebar dark,
        Advance Menu Odoo App Menu Apps, Advanced Apps Menu, Elegant Menu, Web App Menu Backend, Menu Odoo Backend, Collapse Menu, Light Sidebar,
        Expand Menu, Collapsed Menu, Expanded Menu, New Style Menus, Advanced Sidebar Menu, Advance Sidebar Menu, Responsive Menu Sidebar, Sidebar Theme,
        Responsive Sidebar, Hide menu, Show Menu, Hide Sidebar, Show Sidebar, Toggle Menu, Toggle Sidebar, Menu Theme,
        Quick Backend Menu, Dropdown Menu, Parent Menus, Shortcut Menus, Menu Icons, Collapsible menu Odoo,
        Menu Dynamic Sidebar, Advanced Menu, Backend Odoo Web, Elegant Theme Simple, Advance List View Manager, 
        Arc Backend Theme, Fully Functional Theme, Flexible Backend Theme, Fast Backend Theme, Advance Material Backend Theme, Customizable Backend Theme, 
        Attractive Theme for Backend, Elegant Backend Theme, Responsive Web Client, Backend UI, Mobile Responsive for Odoo Community, 
        Flexible Enterprise Theme, Enterprise Backend Theme
    """,
    'description': """ 
        Clarity backend theme
        Odoo Backend Theme, Odoo Community Backend Theme, Web backend Theme, Web Responsive Odoo Theme, New theme design, New design, Multi Level Menu,
        Web Responsive , Odoo Theme, Odoo Modern Theme, Odoo Modern Backend Theme Odoo, Advance Theme Backend Advanced, Left sidebar menu,
        All in one, New advanced Odoo Menu, Sidebar apps, Web menu, Odoo backend menu, Web Responsive menu, Sidebar dark,
        Advance Menu Odoo App Menu Apps, Advanced Apps Menu, Elegant Menu, Web App Menu Backend, Menu Odoo Backend, Collapse Menu, Light Sidebar,
        Expand Menu, Collapsed Menu, Expanded Menu, New Style Menus, Advanced Sidebar Menu, Advance Sidebar Menu, Responsive Menu Sidebar, Sidebar Theme,
        Responsive Sidebar, Hide menu, Show Menu, Hide Sidebar, Show Sidebar, Toggle Menu, Toggle Sidebar, Menu Theme,
        Quick Backend Menu, Dropdown Menu, Parent Menus, Shortcut Menus, Menu Icons, Collapsible menu Odoo,
        Menu Dynamic Sidebar, Advanced Menu, Backend Odoo Web, Elegant Theme Simple, Advance List View Manager, 
        Arc Backend Theme, Fully Functional Theme, Flexible Backend Theme, Fast Backend Theme, Advance Material Backend Theme, Customizable Backend Theme, 
        Attractive Theme for Backend, Elegant Backend Theme, Responsive Web Client, Backend UI, Mobile Responsive for Odoo Community, 
        Flexible Enterprise Theme, Enterprise Backend Theme
    """,
    "sequence": 7,
    "license": "OPL-1",
    "category": "Themes/Backend",
    "website": "https://www.terabits.xyz",
    "depends": ["web"],
    "data": [ 
        'views/res_config_setting.xml',
        'views/res_users.xml',
        'views/webclient_templates.xml'
    ],
    "assets": {
        "web.assets_frontend": [
            'clarity_backend_theme_bits/static/src/scss/login.scss'
        ],
        "web.assets_backend": [   
            'clarity_backend_theme_bits/static/src/xml/WebClient.xml',
            'clarity_backend_theme_bits/static/src/xml/navbar/sidebar.xml', 
            'clarity_backend_theme_bits/static/src/xml/systray_items/user_menu.xml',
            'clarity_backend_theme_bits/static/src/js/SidebarBottom.js',  
            'clarity_backend_theme_bits/static/src/js/WebClient.js', 
            'clarity_backend_theme_bits/static/src/scss/layout.scss',
            'clarity_backend_theme_bits/static/src/scss/navbar.scss', 
            'clarity_backend_theme_bits/static/src/js/navbar.js',  
        ],
    }, 
    'installable': True,
    'application': True,
    'auto_install': False,  
    'images': [
        'static/description/logo.gif',
        'static/description/theme_screenshot.gif',
    ],
}
