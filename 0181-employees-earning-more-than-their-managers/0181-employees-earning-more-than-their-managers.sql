# Write your MySQL query statement below
select emp2.name as Employee from Employee emp1 inner join Employee emp2 on emp1.id = emp2.managerId where emp1.salary <= emp2.salary