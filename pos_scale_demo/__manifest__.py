# @author: Sylvain LE GAL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Point Of Sale - Scale Demo",
    "summary": "Install dependencies and add demo data",
    "version": "16.0.1.0.0",
    "category": "Point of Sale",
    "author": "GRAP, OCA France",
    "website": "https://github.com/oca-france/l10n-france-scale-certification",
    "license": "AGPL-3",
    "maintainers": ["legalsylvain"],
    "depends": [
        # Odoo
        "point_of_sale",
        # https://github.com/OCA/pos/
        "pos_scale_usability",
        "pos_tare",
        # https://gitlab.com/odoo-driver/odoo-addons-driver
        "pos_driver_device_list",
        "pos_driver_display",
        "pos_driver_payment",
        "pos_driver_scale",
    ],
    "demo": [
        "demo/pos_category.xml",
        "demo/pos_config.xml",
        "demo/product_product.xml",
    ],
}
