-- 596. Classes More Than 5 Students

select class as class
from courses
group by class
having count(distinct student)>=5
;