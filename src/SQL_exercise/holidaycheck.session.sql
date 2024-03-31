-- This query joins dates from the 'dates' table with the count of articles per date from the 'justin_trudeau_articles' table.
create table no_articles_by_date as
SELECT d.date AS Date,
       COALESCE(j.C, 0) AS Count
FROM dates d
LEFT JOIN (
    SELECT DATE_FORMAT(STR_TO_DATE(webPublicationDate, '%Y-%m-%dT%H:%i:%sZ'), '%Y-%m-%d') AS article_date,
           COUNT(id) AS C
    FROM justin_trudeau_articles
    GROUP BY article_date
    ORDER BY article_date ASC
) j ON d.date = j.article_date;
