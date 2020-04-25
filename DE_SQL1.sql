select userID, avg(duration) as duration from sessions group by userID having count (duration) >1;
