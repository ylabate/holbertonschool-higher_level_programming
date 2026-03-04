-- Creates a table unique_id with a unique id column with default value 1
-- Creates table unique_id if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256) NOT NULL);
