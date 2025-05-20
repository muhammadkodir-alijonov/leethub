select s.Product_Id, s.Year first_year, s.Quantity, s.Price
  from Sales s
  join (select Product_Id, min(year) as First_Year
          from Sales
         group by Product_Id) First_Sale
    on s.Product_Id = First_Sale.Product_Id
   and s.Year = First_Sale.First_Year;
