-- 185. Department Top Three Salaries

select d.Name as Department, ee.Name as Employee, ee.Salary
from (select e.*, dense_rank() over (partition by DepartmentId order by Salary desc) as DeptPayRank
      from Employee e) ee
join Department d
    on ee.DepartmentId = d.Id
where DeptPayRank <= 3
;