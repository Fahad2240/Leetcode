SELECT Users.name,SUM(Transactions.amount)as balance FROM Users,Transactions WHERE Users.account=Transactions.account group by Transactions.account HAVING SUM(Transactions.amount)>10000
