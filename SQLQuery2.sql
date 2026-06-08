use demodb;

select * from sales;
select * from menu;
select * from members;

SELECT 
    s.customer_id,
    SUM(m.price) AS total_spent
FROM sales s
JOIN menu m
  ON s.product_id = m.product_id
GROUP BY s.customer_id
ORDER BY s.customer_id;

SELECT 
    customer_id,
    COUNT(DISTINCT order_date) AS visit_days
FROM sales
GROUP BY customer_id
ORDER BY customer_id;


WITH ranked_sales AS (
    SELECT 
        s.customer_id,
        s.order_date,
        m.product_name,
        ROW_NUMBER() OVER (
            PARTITION BY s.customer_id 
            ORDER BY s.order_date
        ) AS rn
    FROM sales s
    JOIN menu m
      ON s.product_id = m.product_id
)
SELECT 
    customer_id,
    product_name AS first_item
FROM ranked_sales
WHERE rn = 1;

SELECT 
    m.product_name,
    COUNT(*) AS total_purchases
FROM sales s
JOIN menu m
  ON s.product_id = m.product_id
GROUP BY m.product_name
ORDER BY total_purchases DESC;

WITH item_counts AS (
    SELECT 
        s.customer_id,
        m.product_name,
        COUNT(*) AS purchase_count,
        RANK() OVER (
            PARTITION BY s.customer_id 
            ORDER BY COUNT(*) DESC
        ) AS rnk
    FROM sales s
    JOIN menu m
      ON s.product_id = m.product_id
    GROUP BY s.customer_id, m.product_name
)
SELECT 
    customer_id,
    product_name,
    purchase_count
FROM item_counts
WHERE rnk = 1;

WITH first_after_membership AS (
    SELECT 
        s.customer_id,
        s.order_date,
        m.product_name,
        ROW_NUMBER() OVER (
            PARTITION BY s.customer_id 
            ORDER BY s.order_date
        ) AS rn
    FROM sales s
    JOIN members mem
      ON s.customer_id = mem.customer_id
    JOIN menu m
      ON s.product_id = m.product_id
    WHERE s.order_date >= mem.join_date
)
SELECT 
    customer_id,
    product_name
FROM first_after_membership
WHERE rn = 1;


WITH last_before_membership AS (
    SELECT 
        s.customer_id,
        s.order_date,
        m.product_name,
        ROW_NUMBER() OVER (
            PARTITION BY s.customer_id 
            ORDER BY s.order_date DESC
        ) AS rn
    FROM sales s
    JOIN members mem
      ON s.customer_id = mem.customer_id
    JOIN menu m
      ON s.product_id = m.product_id
    WHERE s.order_date < mem.join_date
)
SELECT 
    customer_id,
    product_name
FROM last_before_membership
WHERE rn = 1;


SELECT 
    s.customer_id,
    COUNT(*) AS total_items,
    SUM(m.price) AS total_spent
FROM sales s
JOIN members mem
  ON s.customer_id = mem.customer_id
JOIN menu m
  ON s.product_id = m.product_id
WHERE s.order_date < mem.join_date
GROUP BY s.customer_id;


SELECT 
    s.customer_id,
    SUM(
        CASE 
            WHEN m.product_name = 'sushi' THEN m.price * 20
            ELSE m.price * 10
        END
    ) AS total_points
FROM sales s
JOIN menu m
  ON s.product_id = m.product_id
GROUP BY s.customer_id;