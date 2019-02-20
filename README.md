# Order-Loader

Assume I have .zip files containing retail order data in the raw JSON format. I created a ETL that runs daily to load the data into Postgres database.

I created three tables using `create_user_table.py`, `create_order_table.py`, and `create_user_order_table.py`.

`user_table` will include the following info
```json
{
    "user_id": 110585347,
    "user_info": "Other user info we don't have right now."
}
```

`order_table` will include the following info
```json
{
    "order_id": 11748933635,
    "user_id": 110585347,
    "created_at": "2017-10-30T19:58:29-04:00",
    "updated_at": "2017-10-30T19:59:30-04:00",
    "gateway": "cash",
    "subtotal_price": "120.0",
    "total_weight": 6,
    "total_tax": "10.649999999999999",
    "taxes_included": false,
    "currency": "USD",
    "total_discounts": "0.00",
    "total_line_items_price": "120.0",
    "buyer_accepts_marketing": false,
    "referring_site": null,
    "landing_site": null,
    "cancelled_at": null,
    "cancel_reason": null,
    "total_price_usd": "130.64999999999998",
    "location_id": 371291,
    "device_id": 37,
    "customer_locale": null,
    "app_id": 129785,
    "browser_ip": "127.0.0.1",
    "landing_site_ref": null,
    "source_name": "pos",
    "tags": "",
    "total_discount": null
}
```

`item_table` will include the following info
```json
{
    "item_id": 23495245827,
    "order_id": 11748933635,
    "product_id": 9096535107,
}
```

`product_table` will include the following info
```json
{
    "product_id": 9096535107,
    "product_info": "Other product info we don't have right now."
}
```
