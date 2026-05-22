-- USERS
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- PRODUCTS
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name_product VARCHAR(150) NOT NULL,
    description TEXT,
    price NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    stock INT DEFAULT 0 CHECK (stock >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- BILLS (Invoices)
CREATE TABLE bills (
    bill_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total NUMERIC(12,2) DEFAULT 0,

    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);

-- BILL ITEMS (junction table)
CREATE TABLE bill_items (
    bill_item_id SERIAL PRIMARY KEY,
    bill_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(10,2) NOT NULL CHECK (unit_price >= 0),
    subtotal NUMERIC(12,2) GENERATED ALWAYS AS (quantity * unit_price) STORED,

    CONSTRAINT fk_bill
        FOREIGN KEY (bill_id)
        REFERENCES bills(bill_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
        ON DELETE RESTRICT
);

ALTER TABLE bills
ADD COLUMN IF NOT EXISTS status VARCHAR(20) DEFAULT 'Activa';