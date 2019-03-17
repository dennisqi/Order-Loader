product_table_creation_query = """
CREATE TABLE IF NOT EXISTS DMProducts (
    product_id INTEGER PRIMARY KEY,
    priduct_info VARCHAR (355)
);
"""

user_table_creation_query = """
CREATE TABLE IF NOT EXISTS DMUsers (
    user_id INTEGER PRIMARY KEY,
    user_info VARCHAR (355)
);
"""

order_table_creation_query = """
CREATE TABLE IF NOT EXISTS DMOrders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES DMUsers(user_id),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    gateway VARCHAR (355),
    subtotal_price DOUBLE PRECISION,
    total_weight INTEGER,
    total_tax DOUBLE PRECISION,
    taxes_included BOOLEAN,
    currency VARCHAR (5),
    total_discounts DOUBLE PRECISION,
    total_line_items_price DOUBLE PRECISION,
    buyer_accepts_marketing BOOLEAN,
    referring_site VARCHAR (355),
    landing_site VARCHAR (355),
    cancelled_at TIMESTAMP,
    cancel_reason VARCHAR (355),
    total_price_usd DOUBLE PRECISION,
    location_id INTEGER,
    device_id INTEGER,
    customer_locale VARCHAR (355),
    app_id INTEGER,
    browser_ip VARCHAR (355),
    landing_site_ref VARCHAR (355),
    source_name VARCHAR (355),
    tags VARCHAR (355)
);
"""

item_table_creation_query = """
CREATE TABLE IF NOT EXISTS DMItems (
    item_id INTEGER PRIMARY KEY,
    order_id INTEGER REFERENCES DMOrders(order_id),
    product_id INTEGER REFERENCES DMProducts(product_id)
);
"""
