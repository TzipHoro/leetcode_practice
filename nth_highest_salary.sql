CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      
      case 
        
          when N > (select count(*) from Employee) then null
          
          else (select * from (select Salary from Employee
                                order by Salary desc
                                limit N 
                              ) as T
                    order by T.Salary
                    limit 1)
      
      end
      
  );
END