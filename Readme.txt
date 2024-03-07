The project has been developed with Python and the libraries: flask, flask-sqlalchemy and requests.

Requirement Installation:
First we have to type the command: 
python -m pip install -r requrements.txt

Opening the App:
To open we type the command on cmd :
python -m flask --app MovieUpdate run
Finally, we open our browser at localhost:5000/, and the movies with their info will appear.

Relational Database
There are two tables in database greektheater (MySQL database).
Movie(movie_id(PK), title, orignal_title, description)
Director(director_id(PK), name, movie_id(PK), (FK->Movie.movie_id))

The above tables are created via the library flask-sqlalchemy(which I am learning this library right now).


The logic of application:
There are 2 Sets: TMDB and RelationalDB.
Each time the process runs, the RelationaDB must be updated with the data from TMDB.
To do this we follow the steps afterwards:
1. An API request is sent to TMDB with region=gr to find the movies that are currently in Theaters in Greece.
2. Then the movies that are only in the RelationalDB are stored to be deleted, and the movies that are only in the TMDB are stored to be kept.
3. The movies to be deleted are deleted from Relational DB, and the movies to be kept are inserted in the RelationalDB.
4. Afterwards, on the recently inserted movies we made requests about movie details keeping the movie_id, to acquire details about actors.
5. To present the updated info we join the tables Movie and Director and we order the joined table by movie_id.



Usefull benefits on implementation:
1. Instead reinventing the wheel creating algorithms from scratch to find the intersection,
union, etc the data-type Set is used in order to find the above.
2. To delete the old records the database is queried using keyword IN inseat of many queries with Where.
3. The joined table is sorted via movie_Id attribute, in order to find the directors of each movie faster. 
and represent them with the movie info, instead to search the directors for every movie.
4. Http-request for directors are made only for movies who have been recently inserted on the Relational DB.
5. The table Movie is cascaded so if a movie is deleted, the rows of director having the id of the 
deleted movie will be deleted.


