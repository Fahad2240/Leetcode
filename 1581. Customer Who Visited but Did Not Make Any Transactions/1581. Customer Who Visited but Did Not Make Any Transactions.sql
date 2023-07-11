SELECT Visits.customer_id,COUNT(Visits.visit_id) as count_no_trans  FROM Visits left join  Transactions  ON Visits.visit_id=Transactions.visit_id where Transactions.visit_id IS NULL group by Visits.customer_id order by count_no_trans