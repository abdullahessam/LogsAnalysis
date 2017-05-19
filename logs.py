import psycopg2


def getPopularArticles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    q = """
create or replace view posts as  select log.path ,count(log.path) as num
from log  inner join (select slug from articles) as slug
on path like '%' || slug.slug   group by log.path order by num desc ;
  select * from posts order by num desc limit 3;
    """
    c.execute(q)
    articles = c.fetchall()
    db.close()
    print "_______________________________________________________________________________"
    print "Popular articles "
    print "Path                 |count"
    for article in articles:
        print "{0}  | {1}".format(article[0],article[1])



getPopularArticles()

def getPopularAuther():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    q="""
  
select name , count(slug),sum(num) from authors, articles, posts
where articles.author=authors.id  and
posts.path like '%' || articles.slug
 group by name
 order by sum desc limit 3 ;

    """
    c.execute(q)
    authors = c.fetchall()
    db.close()
    print "_______________________________________________________________________________"
    print "Popular Authors "
    print "Author         |articles        |views"
    for author in authors:
        print "{0}  | {1}   | {2}".format(author[0], author[1],author[2])

getPopularAuther()


def getdaterrors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    q = """
  create  or replace view allreq as select date(time),count(status) as num  from log   group by date(time)   ;
  create  or replace view fail as select date(time),count(status)  as num from log   where status!='200 OK' group by date(time) , status  ;

    select f.date as day , f.num as fail ,a.num  as all,(cast(f.num as float)/cast(a.num as float)) *100  as percent
 from allreq as a inner join fail as f on a.date=f.date
  where (cast(f.num as float)/cast(a.num as float)) *100 > 1
   order by percent desc
    limit 1 ;

        """
    c.execute(q)
    errors = c.fetchall()
    db.close()
    print "_______________________________________________________________________________"
    print "day has more than 1% errors"
    print "day         |    fail requests       |   all requests | percent"
    for error in errors:
        print "{0}  | {1}   | {2}   |{3} %".format(error[0], error[1], error[2],error[3])

getdaterrors()