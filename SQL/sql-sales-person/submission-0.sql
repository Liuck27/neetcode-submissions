-- Write your query below
WITH crimson_table AS (
    SELECT DISTINCT sales_id FROM orders
    JOIN company ON orders.com_id = company.com_id
    WHERE company.name = 'CRIMSON'
)

SELECT sales_person.name FROM sales_person
LEFT JOIN crimson_table ON sales_person.sales_id = crimson_table.sales_id
WHERE crimson_table.sales_id IS NULL
