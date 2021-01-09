-- 184. Department Highest Salary

select d.Name as Department, e.Name as Employee, e.Salary as Salary
from Employee e
join Department d
    on d.ID=e.DepartmentId
where (e.Salary, e.DepartmentId) in (select max(Salary), DepartmentId
                                     from Employee
                                     group by DepartmentId)
;