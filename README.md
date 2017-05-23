i made 4 function to execute queries
 just call the function and it will execute the query
 the output should be on the terminal
 i used 3 views it's included to the function you don't have to run it
 here is the commands for the views
 for setup use command psql -d news -f newsdata.sql
 to install  database in the psql
 create python file
 and import psycopg2 module
 then connect database by db = psycopg2.connect("dbname=news")
 create object     c = db.cursor()
 and for execute queries use c.execute('query')

i used function named createviews() to execute the views first  

 create or replace view posts as  select log.path ,count(log.path) as num
from log  inner join (select slug from articles) as slug
on path like '%' || slug.slug   group by log.path order by num desc ;

create  or replace view allreq as select date(time),count(status) as num  from log   group by date(time)   ;

create  or replace view fail as select date(time),count(status)  as num from log   where status!='200 OK' group by date(time) , status  ;
  to run the code use command python logs.py in vagrant terminal
  and the output should be in the terminal



  regards
   Abdullah Essam

