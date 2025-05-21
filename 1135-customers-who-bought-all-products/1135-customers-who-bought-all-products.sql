select Customer_Id
  from Customer
 group by Customer_Id
having count(distinct Product_Key) = (select count(distinct Product_Key)
                                        from Product);
