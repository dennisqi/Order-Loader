product_inseration_query = """
INSERT INTO DMProducts VALUES (%s, %s)
"""

item_inseration_query = """
INSERT INTO DMItems VALUES (%s, %s, %s)
"""

user_inseration_query = """
INSERT INTO DMUsers VALUES (%s, %s)
"""

order_inseration_query = """
INSERT INTO DMOrders VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s
)
"""
