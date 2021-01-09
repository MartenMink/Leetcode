-- 196. Delete Duplicate Emails

delete
from Person
where Id not in (select *
                 from
                    (select min(Id)
                     from Person
                     group by Email) as p)
;