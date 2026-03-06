# SQL more queries

## 0-privileges
A script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the server.

## 1-create_user
A script that creates the MySQL server user `user_0d_1` with all privileges on all databases.

## 2-create_read_user
A script that creates the database `hbtn_0d_2` and the user `user_0d_2` with SELECT privilege on that database.

## 3-force_name
A script that creates a table `force_name` with an `id` (INT) column and a `name` (VARCHAR 256) column that cannot be null.

## 4-never_empty
A script that creates a table `id_not_null` with an `id` column defaulting to 1 and a `name` column that cannot be null.

## 5-unique_id
A script that creates a table `unique_id` with a unique `id` column defaulting to 1 and a `name` column that cannot be null.

## 6-states
A script that creates the database `hbtn_0d_usa` and a table `states` inside it with an auto-increment primary key `id` and a non-null `name` column.

## 7-cities
A script that creates the database `hbtn_0d_usa` and a table `cities` inside it with an auto-increment primary key `id`, a foreign key `state_id` referencing `states`, and a non-null `name` column.

## 8-cities_of_california_subquery
A script that lists all cities of California from the database `hbtn_0d_usa` using a subquery, ordered by `cities.id`.

## 9-cities_by_state_join
A script that lists all cities contained in the database `hbtn_0d_usa` with their state name using a JOIN, ordered by `cities.id`.

## 10-genre_id_by_show
A script that lists all shows from `hbtn_0d_tvshows` that have at least one genre linked, displaying the title and genre id, ordered by title and genre id.

## 11-genre_id_all_shows
A script that lists all shows from `hbtn_0d_tvshows` with their genre id, displaying NULL if a show has no genre linked, ordered by title and genre id.

## 12-no_genre
A script that lists all shows from `hbtn_0d_tvshows` that have no genre linked, ordered by title and genre id.

## 13-count_shows_by_genre
A script that lists all genres from `hbtn_0d_tvshows` and the number of shows linked to each, ordered by the number of shows (descending).

## 14-my_genres
A script that lists all genres of the show `Dexter` from `hbtn_0d_tvshows`, ordered by genre name.

## 15-comedy_only
A script that lists all Comedy shows from `hbtn_0d_tvshows`, ordered by show title.

## 16-shows_by_genre
A script that lists all shows and all genres linked to each show from `hbtn_0d_tvshows`, ordered by show title and genre name.