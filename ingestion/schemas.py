# """
# Expected schemas for all datasets.

# These schemas are used to validate incoming data before it enters the
# platform. They represent the minimum required columns.
# """

SCHEMAS = {
    "customers": {
        "columns": [
            "customer_id",
            "customer_unique_id",
            "customer_zip_code_prefix",
            "customer_city",
            "customer_state",
        ],
        "primary_key": ["customer_id"],
        "datetime_columns": [],
        "numeric_columns": [
            "customer_zip_code_prefix",
        ],
        "not_null": [
            "customer_id",
            "customer_unique_id"
        ]
    },

    "orders": {
        "columns": [
            "order_id",
            "customer_id",
            "order_status",
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        ],
        "primary_key": ["order_id"],
        "datetime_columns": [
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        ],
        "numeric_columns": [],
        "not_null": [
            "order_id",
            "customer_id"
        ]
    },

    "order_items": {
        "columns": [
            "order_id",
            "order_item_id",
            "product_id",
            "seller_id",
            "shipping_limit_date",
            "price",
            "freight_value",
        ],
        "primary_key": ["order_id", "order_item_id"],
        "datetime_columns": [
            "shipping_limit_date",
        ],
        "numeric_columns": [
            "price",
            "freight_value",
        ],
        "not_null": [
            "order_id",
            "order_item_id",
            "product_id",
            "seller_id"
        ]
    },

    "payments": {
        "columns": [
            "order_id",
            "payment_sequential",
            "payment_type",
            "payment_installments",
            "payment_value",
        ],
        "primary_key": ["order_id", "payment_sequential"],
        "datetime_columns": [],
        "numeric_columns": [
            "payment_installments",
            "payment_value",
        ],
        "not_null": [
            "order_id",
            "payment_sequential"
        ]
    },

    "reviews": {
        "columns": [
            "review_id",
            "order_id",
            "review_score",
            "review_comment_title",
            "review_comment_message",
            "review_creation_date",
            "review_answer_timestamp",
        ],
        "primary_key": ["review_id"],
        "datetime_columns": [
            "review_creation_date",
            "review_answer_timestamp",
        ],
        "numeric_columns": [
            "review_score",
        ],
        "not_null": [
            "review_id",
            "order_id",
            "review_score"
        ]
    },

    "products": {
        "columns": [
            "product_id",
            "product_category_name",
            "product_name_lenght",
            "product_description_lenght",
            "product_photos_qty",
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm",
        ],
        "primary_key": ["product_id"],
        "datetime_columns": [],
        "numeric_columns": [
            "product_name_lenght",
            "product_description_lenght",
            "product_photos_qty",
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm",
        ],
        "not_null": [
            "product_id"
        ]
    },

    "sellers": {
        "columns": [
            "seller_id",
            "seller_zip_code_prefix",
            "seller_city",
            "seller_state",
        ],
        "primary_key": ["seller_id"],
        "datetime_columns": [],
        "numeric_columns": [
            "seller_zip_code_prefix",
        ],
        "not_null": [
            "seller_id"
        ]
    },

    "geolocation": {
        "columns": [
            "geolocation_zip_code_prefix",
            "geolocation_lat",
            "geolocation_lng",
            "geolocation_city",
            "geolocation_state",
        ],
        "primary_key": ["geolocation_zip_code_prefix", "geolocation_lat", "geolocation_lng"],
        "datetime_columns": [],
        "numeric_columns": [
            "geolocation_zip_code_prefix",
            "geolocation_lat",
            "geolocation_lng",
        ],
    },

    "category_translation": {
        "columns": [
            "product_category_name",
            "product_category_name_english",
        ],
        "primary_key": ["product_category_name"],
        "datetime_columns": [],
        "numeric_columns": [],
        "not_null": [
            "product_category_name"
        ]
    },
}
