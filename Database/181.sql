-- 181. Employees Earning More Than Their Managers

select e.Name as Employee
from Employee e
join Employee p
    on e.ManagerId = p.Id
and e.Salary > p.salary
;