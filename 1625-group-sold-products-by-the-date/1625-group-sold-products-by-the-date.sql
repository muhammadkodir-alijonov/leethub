select to_char(sell_date) sell_date,
       count(1) num_sold,
       LISTAGG(product, ',') within group(order by product) products
  from (select distinct * from Activities)
 group by sell_date
 order by sell_date
