# Write your MySQL query statement below

SELECT name
FROM Customer
WHERE ( referee_id != 2 OR referee_id IS NULL )
-- ORDER BY c.name DESC


---------


# Write your MySQL query statement below
SELECT product_id
FROM Products 
WHERE low_fats = "Y" and recyclable = "Y"
ORDER BY product_id ASC


-------------