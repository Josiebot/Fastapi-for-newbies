# Not Null
# What you wrote in words

# Product name → NOT NULL = Yes (must always have a value).

# Price → NOT NULL = Yes (must always have a value).

# ID → NOT NULL = No (can be empty).

# 🔹 About Primary Keys

# A primary key is a column (or set of columns) that:
# ✅ Must be unique for each row.
# ✅ Must never be NULL.

# QUERY EDITORS
# A query editor is a tool that allows you to write and execute SQL queries against a database.
# It provides a user-friendly interface for interacting with the database, making it easier to manage and
# manipulate data.
# select * from products; -- select all columns from products table
# select product_name, price from products; -- select specific columns from products table  
# select distinct category from products; -- select unique categories from products table
# SELECT * FROM products WHERE name LIKE 'TVs'; -- select all columns from products table where name is 'TVs'
# SELECT * FROM products WHERE price > 500; -- select all columns from products table where price is greater than 500
# SELECT * FROM products WHERE price BETWEEN 100 AND 500; -- select all columns from
# products table where price is between 100 and 500
# SELECT * FROM products ORDER BY price;
# SPECIFY THE ORDER BY SAYING asc
# SELECT * FROM products ORDER BY price ASC;
# SELECT * FROM products ORDER BY price DESC;
# SELECT * FROM products ORDER BY inventory DESC;
# SELECT * FROM products ORDER BY inventory DESC, price; (Thi sorts by inventory and when it gets to Zero it switches to price and starts ordering by price descending)
# SELECT * FROM products WHERE category IN ('TVs', 'Laptops'); -- select all columns from products table where category is either 'TVs' or 'Laptops'
# SELECT * FROM products WHERE name LIKE  S%'; -- select all columns from products table where name starts with 'S'
# SELECT * FROM products WHERE name LIKE '%s'; -- select all columns from products table where name ends with 's'
# SELECT * FROM products WHERE name LIKE '%phone%'; -- select all columns from products table where name contains 'phone'
# SELECT * FROM products ORDER BY created_at DESC; (Starts with the )
# SELECT * FROM products WHERE price >20 ORDER BY created_at; (You sort all products with a price greater than 20 then sort them according to the date they were created)

# SELECT * FROM products WHERE price IS NULL; -- select all columns from products table where price is NULL
# SELECT * FROM products WHERE price IS NOT NULL; -- select all columns from products table where
# SELECT * FROM products WHERE price WHERE name NOT LIKE 'T%'; -- select all columns from products table where name does not start with 'T'.
# SELECT *FROM products WHERE name LIKE '%en%'; -- select all columns from products table where name contains 'en'.
# SELECT * FROM products where id = 1 or id =2 or id =3; -- select all columns from products table where id is 1, 2 or 3.
# SELECT * FROM products where id IN (1,2,3); -- select all columns from products table where id is 1, 2 or 3.
# SELECT * FROM products ORDER BY price DESC; -- select all columns from products table ordered by price in descending order.
# SELECT *FROM products ORDER by inventory desc, price ASC; -- select all columns from products table ordered by inventory in descending order and price in ascending order.
# SELECT *FROM products ORDER by createdAt; -- select all columns from products table ordered by createdAt in ascending order.
# SELECT *FROM products ORDER by createdAt DESC; -- select all columns from products table ordered
# LIMI
# SELECT * FROM products LIMIT 10; (Limit the nbumber of rows or items you are getting back)

# SELECT * FROM products ORDER By id LIMIT 10;  (This gives with the ids and upto 10)

# SKIP SOME ROWS (OFFSET)
# select * from products order by name LIMIT 11 offset 10; (Skps the first 10)


# When using SQL
# INSERT INTO Products{name, price}VALUES ()
# insert into products(name, price, id) values ('radio', 30, 10); Make sure the order matches
# select * from products where name = 'tortilla';
# insert into products(name, price, id) values ('microwave', 30, 9) returning *;

# RENAMING COLUMNS
# SELECT ID AS products_id from products;
# SELECT ID AS products_id, is_sale as is_sale_products from products;

# SPECIFIC
# select * from products where id = 10;
# /insert into products (name, price, id) values ('book', 20, 5),('salt', 15, 4), ('pen2', 19, 11) ;

# DELETE

# DELETE from products where price=19 returning *;
# select * from products;

# UPDATE
# update products SET name = 'tortilla', price = 49 where id = 9; 
# UPDATE products SET is_sale = true where id = 2 returning *;