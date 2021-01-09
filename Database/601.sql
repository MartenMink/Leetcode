-- 601. Human Traffic of Stadium

select id, visit_date, people
from (select id, visit_date, people,
      LAG(people,2) over (order by visit_date) as lag2,
      LAG(people,1) over (order by visit_date) as lag1,
      LEAD(people,2) over (order by visit_date) as lead2,
      LEAD(people,1) over (order by visit_date) as lead1
from stadium) a
where (a.people >= 100
       and a.lead1 >= 100
       and a.lead2 >= 100)
       or (a.people >= 100 and a.lag2 >= 100 and a.lag1 >= 100)
       or (a.people >= 100 and a.lag1 >= 100 and a.lead1 >= 100)
;