-- Creates a table id_not_null with a default value of 1 for id
-- Create table id_not_null if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256) NOT NULL);
