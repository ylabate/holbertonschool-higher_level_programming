# SQL introduction

## 0-list_databases
A script that lists all databases of a MySQL server.

## 1-create_database_if_missing
A script that creates the database `hbtn_0c_0` in a MySQL server if it does not already exist.

## 2-remove_database
A script that deletes the database `hbtn_0c_0` from a MySQL server if it exists.

## 3-list_tables
A script that lists all tables of a database in a MySQL server.

## 4-first_table
A script that creates a table called `first_table` with columns `id` (INT) and `name` (VARCHAR 256) in a MySQL server.

## 5-full_table
A script that prints the full description of the table `first_table` using `SHOW CREATE TABLE`.

## 6-list_values
A script that lists all rows of the table `first_table` in a MySQL server.

## 7-insert_value
A script that inserts a new row with `id = 89` and `name = 'Best School'` into the table `first_table`.

## 8-count_89
A script that displays the number of records with `id = 89` in the table `first_table`.

## 9-full_creation
A script that creates a table `second_table` and adds multiple rows with `id`, `name`, and `score` columns.

## 10-top_score
A script that lists all records of the table `second_table`, ordered by score (top first).

## 11-best_score
A script that lists all records with a score >= 10 in the table `second_table`, ordered by score (top first).

## 12-no_cheating
A script that updates the score of Bob to 10 in the table `second_table`.

## 13-change_class
A script that removes all records with a score <= 5 in the table `second_table`.

## 14-average
A script that computes the score average of all records in the table `second_table`.

## 15-groups
A script that lists the number of records with the same score in the table `second_table`, sorted by the number of records (descending).

## 16-no_link
A script that lists all records of the table `second_table` that have a non-empty `name`, ordered by score (top first).