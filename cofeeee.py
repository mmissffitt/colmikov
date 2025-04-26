import sqlite3

con = sqlite3.Connection('coffee.db')

cur = con.cursor()


clients = '''CREATE TABLE IF NOT EXISTS clients (
  id INT PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL, 
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR NOT NULL
  )'''

cur.execute(clients)

categories_of_dishes = '''CREATE TABLE IF NOT EXISTS categories_of_dishes (
  id INT PRIMARY KEY,
  category_name VARCHAR(255) NOT NULL
  )'''

cur.execute(categories_of_dishes)

dishes = '''CREATE TABLE IF NOT EXISTS dishes (
  id INT PRIMARY KEY,
  category_of_dish_id INT, 
  name VARCHAR(255) NOT NULL,
  price DECIMAL NOT NULL,
   FOREIGN KEY(category_of_dish_id) REFERENCES categories_of_dishes(id))
  '''

cur.execute(dishes)

employees = '''CREATE TABLE IF NOT EXISTS employees (
  id INT PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL, 
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR NOT NULL)'''

cur.execute(employees)

loyalty_cards = '''CREATE TABLE IF NOT EXISTS loyalty_cards (id INT PRIMARY KEY, client_id INT NOT NULL, balance DECIMAL(10,2), FOREIGN KEY(client_id) REFERENCES clients(id))'''

cur.execute(loyalty_cards)

tables = '''CREATE TABLE IF NOT EXISTS "tables"(
  id INT PRIMARY KEY,
  capacity INT NOT NULL
  )'''

cur.execute(tables)

orders = '''CREATE TABLE IF NOT EXISTS orders (
  id INT PRIMARY KEY,
  client_id INT, 
  employee_id INT,
  table_id INT,
  order_time TIMESTAMP NOT NULL,
  total_amount DECIMAL NOT NULL,
   FOREIGN KEY(client_id) REFERENCES clients(id),
   FOREIGN KEY(employee_id) REFERENCES employees(id),
   FOREIGN KEY(table_id) REFERENCES "tables"(id)
  )'''

cur.execute(orders)

dishes_in_orders = '''CREATE TABLE IF NOT EXISTS dishes_in_orders (
  id INT PRIMARY KEY,
  dish_id INT, 
  order_id INT,
  FOREIGN KEY(dish_id) REFERENCES dishes(id),
  FOREIGN KEY(order_id) REFERENCES orders(id)
  )'''

cur.execute(dishes_in_orders)

clients_data = [
    (1, 'Иван', 'Иванов', 'ivan@example.com'),
    (2, 'Петр', 'Петров', 'petr@example.com'),
    (3, 'Анна', 'Сидорова', 'anna@example.com'),
    (4, 'Мария', 'Кузнецова', 'maria@example.com'),
    (5, 'Алексей', 'Смирнов', 'alex@example.com')
]

cur.executemany('INSERT INTO clients VALUES (?, ?, ?, ?)', clients_data)

categories_data = [
    (1, 'Кофе'),
    (2, 'Десерты'),
    (3, 'Завтраки'),
    (4, 'Сэндвичи'),
    (5, 'Напитки')
]

cur.executemany('INSERT INTO categories_of_dishes VALUES (?, ?)', categories_data)

dishes_data = [
    (1, 1, 'Эспрессо', 120),
    (2, 1, 'Американо', 150),
    (3, 1, 'Капучино', 180),
    (4, 1, 'Латте', 190),
    (5, 2, 'Чизкейк', 250),
    (6, 2, 'Тирамису', 280),
    (7, 3, 'Омлет с овощами', 320),
    (8, 4, 'Куриный сэндвич', 270),
    (9, 5, 'Свежевыжатый сок', 200)
]

cur.executemany('INSERT INTO dishes VALUES (?, ?, ?, ?)', dishes_data)

employees_data = [
    (1, 'Ольга', 'Васильева', 'olga@coffee.com'),
    (2, 'Дмитрий', 'Николаев', 'dmitry@coffee.com'),
    (3, 'Елена', 'Федорова', 'elena@coffee.com')
]

cur.executemany('INSERT INTO employees VALUES (?, ?, ?, ?)', employees_data)

loyalty_cards_data = [
    (1, 1, 500),
    (2, 2, 1200),
    (3, 3, 300),
    (4, 5, 750)
]

cur.executemany('INSERT INTO loyalty_cards VALUES (?, ?, ?)', loyalty_cards_data)

tables_data = [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 2),
    (5, 4)
]

cur.executemany('INSERT INTO "tables" VALUES (?, ?)', tables_data)

orders_data = [
    (1, 1, 1, 2, '2023-05-10 10:30:00', 450),
    (2, 2, 2, 3, '2023-05-10 11:15:00', 630),
    (3, 3, 1, 1, '2023-05-10 12:00:00', 370),
    (4, 5, 3, 4, '2023-05-10 14:20:00', 190)
]

cur.executemany('INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?)', orders_data)

dishes_in_orders_data = [
    (1, 3, 1),
    (2, 5, 1),
    (3, 1, 2),
    (4, 6, 2),
    (5, 9, 2),
    (6, 4, 3),
    (7, 8, 3),
    (8, 2, 4)
]

cur.executemany('INSERT INTO dishes_in_orders VALUES (?, ?, ?)', dishes_in_orders_data)


con.commit()
con.close()