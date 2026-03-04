select tv_shows.title, tv_show_genres.genre_id
from tv_shows
inner join tv_show_genres on tv_show_genres.show_id = tv_shows.id
order by tv_shows.title, tv_show_genres.genre_id