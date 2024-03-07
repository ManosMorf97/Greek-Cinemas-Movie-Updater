# GreekCinemasMoviesUpdater

## tools
* Python
* flask
* flask-sqlalchemy
* HTML
* CSS

## instalation
* python -m pip install -r requrements.txt

## app runing
1) python -m flask --app MovieUpdate run
2) open localhost:5000


## Relational Tables
* Movie
 * movie_id (PK)
 * title
 * original_title
 * description
*Director
 * director_id (PK)
 * name
 * movie_id (PK) (FK) Movie(movie_id)

