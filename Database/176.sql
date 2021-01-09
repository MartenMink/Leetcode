-- 176. Second Highest Salary

select max(e.Salary) as SecondHighestSalary
from Employee e
where e.Salary not in (select max(Salary) from Employee)
;