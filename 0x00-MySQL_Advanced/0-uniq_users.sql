-- Task Description: Create a table 'users' with specified attributes
-- If the table already exists, the script should not fail

-- Create the 'users' table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

-- Example INSERT statements (optional)
-- INSERT INTO users (email, name) VALUES ('bob@dylan.com', 'Bob');
-- INSERT INTO users (email, name) VALUES ('sylvie@dylan.com', 'Sylvie');
-- INSERT INTO users (email, name) VALUES ('bob@dylan.com', 'Jean');
