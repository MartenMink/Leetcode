-- 262. Trips and Users

select Request_at as Day ,round((sum(num)*1.0)/sum(count_all),2) as "Cancellation Rate"
from
(select Request_at,
    case
        when t.status in ('cancelled_by_client','cancelled_by_driver') then 1
        else 0
    end as num,
        1 as count_all
from Trips t
join Users u on t.Client_id=u.Users_id and u.Banned='No'
and Request_at between '2013-10-01' and '2013-10-03') t
group by Request_at
;