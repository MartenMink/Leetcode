-- 177. Nth Highest Salary

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set N=N-1;
  RETURN (
      case
            when n > (select count(*) from Employee) then Null
            when n <= (select count(*) from Employee) then (select (select distinct Salary from Employee order by Salary                                                                desc limit 1 offset N))
      end
  );
END
;