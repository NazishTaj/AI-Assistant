
import os
from groq import Groq
from database import get_schema
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_sql(question):

    schema = get_schema()

    prompt = f"""
You are an expert MySQL data analyst.

DATABASE SCHEMA
{schema}

TABLE RELATIONSHIPS
orders.customer_id = customers.customer_id
orders.order_id = payments.order_id
orders.order_id = order_items.order_id
order_items.product_id = products.product_id
order_items.seller_id = sellers.seller_id
customers.customer_zip_code_prefix = geolocation.geolocation_zip_code_prefix
sellers.seller_zip_code_prefix = geolocation.geolocation_zip_code_prefix

DATASET SEMANTICS
customer_unique_id = real unique customer
customer_id = order level customer record

city columns:
customers.customer_city
geolocation.geolocation_city

revenue column:
payments.payment_value

JOIN EXAMPLES

Example 1: orders → customers
SELECT
o.order_id,
c.customer_unique_id,
c.customer_city
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
LIMIT 10;

Example 2: orders → payments
SELECT
o.order_id,
p.payment_type,
p.payment_value
FROM orders o
JOIN payments p
ON o.order_id = p.order_id
LIMIT 10;

Example 3: orders → order_items
SELECT
o.order_id,
oi.product_id,
oi.seller_id,
oi.price
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
LIMIT 10;

Example 4: order_items → products
SELECT
oi.order_id,
oi.product_id,
p.product_category_name
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
LIMIT 10;

Example 5: order_items → sellers
SELECT
oi.order_id,
oi.seller_id,
s.seller_city
FROM order_items oi
JOIN sellers s
ON oi.seller_id = s.seller_id
LIMIT 10;

Example 6: customers → geolocation
SELECT
c.customer_id,
c.customer_city,
g.geolocation_city
FROM customers c
JOIN geolocation g
ON c.customer_zip_code_prefix = g.geolocation_zip_code_prefix
LIMIT 10;

Example 7: sellers → geolocation
SELECT
s.seller_id,
s.seller_city,
g.geolocation_city
FROM sellers s
JOIN geolocation g
ON s.seller_zip_code_prefix = g.geolocation_zip_code_prefix
LIMIT 10;

Example 8: full ecommerce join
SELECT
o.order_id,
c.customer_unique_id,
g.geolocation_city,
p.payment_value,
oi.product_id,
pr.product_category_name
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
JOIN payments p
ON o.order_id = p.order_id
JOIN order_items oi
ON o.order_id = oi.order_id
JOIN products pr
ON oi.product_id = pr.product_id
JOIN geolocation g
ON c.customer_zip_code_prefix = g.geolocation_zip_code_prefix
LIMIT 10;

Example 9: 
SELECT
g.geolocation_city,
SUM(p.payment_value) AS revenue
FROM orders o
JOIN payments p 
ON o.order_id = p.order_id
JOIN customers c 
ON o.customer_id = c.customer_id
JOIN geolocation g
ON c.customer_zip_code_prefix = g.geolocation_zip_code_prefix
GROUP BY g.geolocation_city
ORDER BY revenue DESC
LIMIT 1;

RULES
- Only use tables and columns present in schema
- customer_id should only be used for joins
- when counting customers use customer_unique_id
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
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    sql_query = response.choices[0].message.content.strip()

    # remove markdown formatting
    sql_query = sql_query.replace("```sql", "").replace("```", "")

    # keep only first SQL statement
    if ";" in sql_query:
        sql_query = sql_query.split(";")[0] + ";"
import os
from groq import Groq
from database import get_schema
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_sql(question):

    schema = get_schema()

    prompt = f"""
You are an expert MySQL data analyst.

DATABASE SCHEMA
{schema}

TABLE RELATIONSHIPS
orders.customer_id = customers.customer_id
orders.order_id = payments.order_id
orders.order_id = order_items.order_id
order_items.product_id = products.product_id
order_items.seller_id = sellers.seller_id
customers.customer_zip_code_prefix = geolocation.geolocation_zip_code_prefix
sellers.seller_zip_code_prefix = geolocation.geolocation_zip_code_prefix

DATASET SEMANTICS
customer_unique_id = real unique customer
customer_id = order level customer record

city columns:
customers.customer_city
geolocation.geolocation_city

revenue column:
payments.payment_value

JOIN EXAMPLES

Example 1: orders → customers
SELECT
o.order_id,
c.customer_unique_id,
c.customer_city
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
LIMIT 10;

Example 2: orders → payments
SELECT
o.order_id,
p.payment_type,
p.payment_value
FROM orders o
JOIN payments p
ON o.order_id = p.order_id
LIMIT 10;

Example 3: orders → order_items
SELECT
o.order_id,
oi.product_id,
oi.seller_id,
oi.price
FROM orders o
JOIN order_items oi
ON o.order_id = oi.order_id
LIMIT 10;

Example 4: order_items → products
SELECT
oi.order_id,
oi.product_id,
p.product_category_name
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
LIMIT 10;

Example 5: order_items → sellers
SELECT
oi.order_id,
oi.seller_id,
s.seller_city
FROM order_items oi
JOIN sellers s
ON oi.seller_id = s.seller_id
LIMIT 10;

Example 6: customers → geolocation
SELECT
c.customer_id,
c.customer_city,
g.geolocation_city
FROM customers c
JOIN geolocation g
ON c.customer_zip_code_prefix = g.geolocation_zip_code_prefix
LIMIT 10;

Example 7: sellers → geolocation
SELECT
s.seller_id,
s.seller_city,
g.geolocation_city
FROM sellers s
JOIN geolocation g
ON s.seller_zip_code_prefix = g.geolocation_zip_code_prefix
LIMIT 10;

Example 8: full ecommerce join
SELECT
o.order_id,
c.customer_unique_id,
g.geolocation_city,
p.payment_value,
oi.product_id,
pr.product_category_name
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
JOIN payments p
ON o.order_id = p.order_id
JOIN order_items oi
ON o.order_id = oi.order_id
JOIN products pr
ON oi.product_id = pr.product_id
JOIN geolocation g
ON c.customer_zip_code_prefix = g.geolocation_zip_code_prefix
LIMIT 10;

Example 9: 
SELECT
g.geolocation_city,
SUM(p.payment_value) AS revenue
FROM orders o
JOIN payments p 
ON o.order_id = p.order_id
JOIN customers c 
ON o.customer_id = c.customer_id
JOIN geolocation g
ON c.customer_zip_code_prefix = g.geolocation_zip_code_prefix
GROUP BY g.geolocation_city
ORDER BY revenue DESC
LIMIT 1;

RULES
- Only use tables and columns present in schema
- customer_id should only be used for joins
- when counting customers use customer_unique_id
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
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    sql_query = response.choices[0].message.content.strip()

    # remove markdown formatting
    sql_query = sql_query.replace("```sql", "").replace("```", "")

    # keep only first SQL statement
    if ";" in sql_query:
        sql_query = sql_query.split(";")[0] + ";"

    return sql_query
