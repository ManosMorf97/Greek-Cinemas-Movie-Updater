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
  &nbsp; * movie_id (PK)
  &nbsp;- title
  &nbsp; - original_title
  &nbsp; - description
* Director
  &nbsp; - director_id (PK)
  &nbsp; - name
  &nbsp; - movie_id (PK) (FK) Movie(movie_id)

