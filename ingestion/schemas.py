# """
# Expected schemas for all datasets.

# These schemas are used to validate incoming data before it enters the
# platform. They represent the minimum required columns.
# """

# SCHEMAS = {
#     "customers": [
#         "customer_id",
#         "customer_unique_id",
#         "customer_zip_code_prefix",
#         "customer_city",
#         "customer_state",
#     ],

#     "orders": [
#         "order_id",
#         "customer_id",
#         "order_status",
#         "order_purchase_timestamp",
#         "order_approved_at",
#         "order_delivered_carrier_date",
#         "order_delivered_customer_date",
#         "order_estimated_delivery_date",
#     ],

#     "order_items": [
#         "order_id",
#         "order_item_id",
#         "product_id",
#         "seller_id",
#         "shipping_limit_date",
#         "price",
#         "freight_value",
#     ],

#     "payments": [
#         "order_id",
#         "payment_sequential",
#         "payment_type",
#         "payment_installments",
#         "payment_value",
#     ],

#     "reviews": [
#         "review_id",
#         "order_id",
#         "review_score",
#         "review_comment_title",
#         "review_comment_message",
#         "review_creation_date",
#         "review_answer_timestamp",
#     ],

#     "products": [
#         "product_id",
#         "product_category_name",
#         "product_name_lenght",
#         "product_description_lenght",
#         "product_photos_qty",
#         "product_weight_g",
#         "product_length_cm",
#         "product_height_cm",
#         "product_width_cm",
#     ],

#     "sellers": [
#         "seller_id",
#         "seller_zip_code_prefix",
#         "seller_city",
#         "seller_state",
#     ],

#     "geolocation": [
#         "geolocation_zip_code_prefix",
#         "geolocation_lat",
#         "geolocation_lng",
#         "geolocation_city",
#         "geolocation_state",
#     ],

#     "category_translation": [
#         "product_category_name",
#         "product_category_name_english",
#     ],
# }


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
    },
}