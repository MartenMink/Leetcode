-- 180. Consecutive Numbers

select distinct n1.Num as ConsecutiveNums
from Logs n1
join Logs n2
    on n1.Id=n2.Id-1
join Logs n3
    on n2.Id=n3.Id -1
where n1.Num=n2.Num and n2.Num=n3.Num
;