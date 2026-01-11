
-- not working


select (
SELECT salary 
FROM Employee 
ORDER BY salary desc
LIMIT 1 OFFSET 1
) as SecondHighestSalary ;



-- working 

select Max(salary) AS SecondHighestSalary
FROM Employee 
Where salary < ( SELECT MAX(salary) FROM Employee );