--  script that list all shows contained in hbtn_0d_tvshows
--  that have atleast one genre linked
SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
JOIN tv_shows_genres
ON tv_shows.id = tv_shows_genres.shows_id
ORDER BY 1, 2;