-- 197. Rising Temperature

select w.Id as Id
from Weather w
left join Weather ww
    on datediff(w.RecordDate, ww.RecordDate) = 1
where w.Temperature > ww.Temperature
;