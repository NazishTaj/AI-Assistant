import os
from groq import Groq
from database import run_query
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------------------
# MANUAL DATABASE SCHEMA
# ---------------------------

SCHEMA = """
DATABASE SCHEMA

orders
- order_id
- customer_id
- order_status
- order_purchase_timestamp
- order_approved_at
- order_delivered_carrier_date
- order_delivered_customer_date
- order_estimated_delivery_date

customers
- customer_id
- customer_unique_id
- customer_zip_code_prefix
- customer_city
- customer_state

order_items
- order_id
- order_item_id
- product_id
- seller_id
- shipping_limit_date
- price
- freight_value

products
- product_id
- product_category_name
- product_name_lenght
- product_description_lenght
- product_photos_qty
- product_weight_g
- product_length_cm
- product_height_cm
- product_width_cm

sellers
- seller_id
- seller_zip_code_prefix
- seller_city
- seller_state

payments
- order_id
- payment_sequential
- payment_type
- payment_installments
- payment_value

order_reviews
- review_id
- order_id
- review_score
- review_comment_title
- review_comment_message
- review_creation_date
- review_answer_timestamp

geolocation
- geolocation_zip_code_prefix
- geolocation_lat
- geolocation_lng
- geolocation_city
- geolocation_state

product_category_name_translation
- product_category_name
- product_category_name_english
"""

RELATIONSHIPS = """
TABLE RELATIONSHIPS

orders.customer_id = customers.customer_id

order_items.order_id = orders.order_id
order_items.product_id = products.product_id
order_items.seller_id = sellers.seller_id

order_payments.order_id = orders.order_id
order_reviews.order_id = orders.order_id

products.product_category_name = product_category_name_translation.product_category_name

customers.customer_zip_code_prefix = geolocation.geolocation_zip_code_prefix
sellers.seller_zip_code_prefix = geolocation.geolocation_zip_code_prefix
"""

SEMANTICS = """
DATASET SEMANTICS

customer_unique_id = real unique customer
customer_id = order level customer record

revenue column:
order_payments.payment_value

item price column:
order_items.price

city columns:
customers.customer_city
sellers.seller_city
geolocation.geolocation_city
"""


# ---------------------------
# GENERATE SQL
# ---------------------------

def generate_sql(question):

    prompt = f"""
You are an expert MySQL data analyst working with the Olist E-commerce dataset.

{SCHEMA}

{RELATIONSHIPS}

{SEMANTICS}

RULES
- Only use tables and columns present in schema
- customer_id should only be used for joins
- when counting customers use customer_unique_id
- revenue must use order_payments.payment_value
- prefer simple joins instead of nested queries
- prefer ORDER BY + LIMIT for top results
- never create columns that do not exist
- output only SQL query
- start query with SELECT
- end query with semicolon

USER QUESTION
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        messages=[{"role": "user", "content": prompt}]
    )

    sql_query = response.choices[0].message.content.strip()

    sql_query = sql_query.replace("```sql", "").replace("```", "")

    if ";" in sql_query:
        sql_query = sql_query.split(";")[0] + ";"

    return sql_query


# ---------------------------
# FIX SQL
# ---------------------------

def fix_sql(question, bad_sql, error_message):

    prompt = f"""
You are a MySQL expert.

{SCHEMA}

{RELATIONSHIPS}

The following SQL query failed.

USER QUESTION
{question}

SQL QUERY
{bad_sql}

MYSQL ERROR
{error_message}

Fix the SQL query using correct tables and columns.

Return ONLY the corrected SQL query.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        messages=[{"role": "user", "content": prompt}]
    )

    fixed_sql = response.choices[0].message.content.strip()

    fixed_sql = fixed_sql.replace("```sql", "").replace("```", "")

    if ";" in fixed_sql:
        fixed_sql = fixed_sql.split(";")[0] + ";"

    return fixed_sql


# ---------------------------
# EXECUTE SQL WITH RETRY
# ---------------------------

def execute_with_retry(question, sql_query, max_retry=2):

    attempt = 0

    while attempt <= max_retry:

        try:

            result = run_query(sql_query)

            print("\nGenerated SQL:\n")
            print(sql_query)

            return result

        except Exception as e:

            print("\nSQL Error:", e)

            if attempt == max_retry:
                raise Exception("Failed after retries")

            print("\nTrying to fix SQL...\n")

            sql_query = fix_sql(question, sql_query, str(e))

            attempt += 1


# ---------------------------
# MAIN ENTRY
# ---------------------------

def ask_database(question):

    sql_query = generate_sql(question)

    result = execute_with_retry(question, sql_query)

    return result