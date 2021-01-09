-- 183. Customers Who Never Order

select c.Name as Customers
from Customers c
left join Orders o
    on c.Id = o.CustomerId
where o.CustomerId is Null
;