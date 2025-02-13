-- Insert data into first_name table
INSERT INTO first_name (name) VALUES
('John'),
('Jane'),
('Alice'),
('Bob'),
('Charlie');

-- Insert data into last_name table
INSERT INTO last_name (name) VALUES
('Doe'),
('Smith'),
('Brown'),
('Johnson'),
('Davis');

-- Insert data into car_brand table
INSERT INTO car_brand (name) VALUES
('Toyota'),
('Honda'),
('Ford'),
('BMW'),
('Audi');

-- Insert data into car_model table
INSERT INTO car_model (name) VALUES
('Corolla'),
('Civic'),
('Focus'),
('X5'),
('A4');

-- Insert data into customer table
INSERT INTO customer (first_name, last_name, licence_number) VALUES
(1, 1, 'ABC12345'),
(2, 2, 'XYZ67890'),
(3, 3, 'LMN45678'),
(4, 4, 'PQR78912'),
(5, 5, 'DEF34567');

-- Insert data into car table
INSERT INTO car (brand_id, model_id, plate_number) VALUES
(1, 1, 'XYZ123'),
(2, 2, 'ABC789'),
(3, 3, 'LMN456'),
(4, 4, 'PQR678'),
(5, 5, 'DEF901');

-- Insert data into rent_car table
INSERT INTO rent_car (car_id, customer_id, rented_on, returned_on) VALUES
(1, 1, '2024-02-01', '2024-02-05'),
(2, 2, '2024-02-03', NULL),
(3, 3, '2024-02-04', '2024-02-10'),
(4, 4, '2024-02-06', NULL),
(5, 5, '2024-02-07', '2024-02-12');
