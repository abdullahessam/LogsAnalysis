i made 3 function to execute queries
 just call the function and it will execute the query
 the output should be on the terminal
 i used 3 views it's inculded to the function you don't have to run it
 here is the commands for the views

 create or replace view posts as  select log.path ,count(log.path) as num
from log  inner join (select slug from articles) as slug
on path like '%' || slug.slug   group by log.path order by num desc ;

create  or replace view allreq as select date(time),count(status) as num  from log   group by date(time)   ;

create  or replace view fail as select date(time),count(status)  as num from log   where status!='200 OK' group by date(time) , status  ;
  to run the code use command python logs.py in vagrant terminal
  and the output should be in the terminal



  regards
   Abdullah Essam

