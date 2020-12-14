DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64),
    contact VARCHAR(32)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64),
    description VARCHAR(255),
    stock INT,
    buy_price INT,
    sell_price INT,
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE
);
