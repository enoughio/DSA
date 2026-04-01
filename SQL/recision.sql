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


# Write your MySQL query statement below
SELECT name, population, area 
FROM World 
WHERE area >= 3000000 OR population >= 25000000 ; 



-------------
-- 1148. Article Views I

# Write your MySQL query statement below
select DISTINCT author_id  as id
from Views 
where viewer_id = author_id 
order by author_id ASC


-------------

-- 1683. Invalid Tweets
select tweet_id 
from Tweets
where LENGTH(content) > 15;



------------\
--  1581. Customer Who Visited but Did Not Make Any Transactions

select distinct customer_id, count(customer_id) as count_no_trans
FROM Visits v
Left Join Transactions t
on v.visit_id = t.visit_id
where amount is NULL 
group by customer_id
