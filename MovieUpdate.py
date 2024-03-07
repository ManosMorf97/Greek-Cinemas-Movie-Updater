#https://api.themoviedb.org/3/movie/now_playing?region=gr&api_key=bbb0e77b94b09193e6f32d5fac7a3b9c
#https://api.themoviedb.org/3/movie/792307/credits?api_key=bbb0e77b94b09193e6f32d5fac7a3b9c

#TIPS
#object.__dict__
from flask import Flask , request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as mc
import requests as http_requests
from helpfull_functions import TheaterSet,usefull_keys,directors_to_add,Movie_dict
   
mysql_db=mc.connect(username="root",passwd="x#9kQL4X",host="localhost",port="3306")
cursor=mysql_db.cursor()
cursor.execute("Create database if not exists greektheater")
mysql_db.commit()
cursor.close()
mysql_db.disconnect()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql+mysqlconnector://root:x#9kQL4X@localhost:3306/greektheater"
db=SQLAlchemy(app)
app.app_context().push()
    
class Movie(db.Model):
    movie_id=db.Column(db.Integer(),primary_key=True,)
    title=db.Column(db.String(60))
    overview=db.Column(db.String(1500))
    original_title=db.Column(db.String(80))
    directed_by=db.relationship("Director",cascade='all, delete, delete-orphan')
    
    def __init__(self,movie_id,title,overview,original_title):
        self.movie_id=movie_id
        self.title=title
        self.overview=overview
        self.original_title=original_title
    
    def __repr__(self):
        answer="movie_id:"
        answer+=str(self.movie_id)+","
        answer+="title:"+self.title+","
        answer+="original title:"+self.original_title+","
        answer+="overview:"+self.overview+","
        return answer

class Director(db.Model):
    #director_movie_ids=db.Column(db.String(30))
    director_id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(30))
    movie_id=db.Column(db.Integer(),db.ForeignKey('movie.movie_id',ondelete='cascade'),primary_key=True)
    
    
    def __init__(self,director_id,name,movie_id):
        self.director_id=director_id
        self.name=name
        self.movie_id=movie_id
        
    def __repr__(self):
        answer="Director ID: "+str(self.director_id)+" Director Name: "+self.name
        answer+=" Movie ID: "+str(self.movie_id)
        return answer

db.create_all()


def Movies_Directors():
    movies_to_html=[]
    MovDir=Movie.query.join(Director,Movie.movie_id==Director.movie_id)\
        .add_column(Director.name)\
        .order_by(Movie.movie_id).all()
    for i in range(len(MovDir)):
        last_index=len(movies_to_html)-1
        print(MovDir[i][0].title)
        if(i==0 or MovDir[i][0].movie_id!=MovDir[i-1][0].movie_id):
            keys=['title','original_title','overview']
            values=[MovDir[i][0].title,MovDir[i][0].original_title,MovDir[i][0].overview]
            movie_dict=Movie_dict(keys,values)
            movies_to_html.append(movie_dict)
            last_index=len(movies_to_html)-1
            movies_to_html[last_index]["directors"]=[]
            movies_to_html[last_index]["directors"].append({'name':MovDir[i][1]})
        else:
            movies_to_html[last_index]["directors"].append({'name':MovDir[i][1]})
    return movies_to_html


@app.route("/",methods=["POST","GET"])
def TheaterTable():        
    params={
        "region":"gr",
        "api_key":"bbb0e77b94b09193e6f32d5fac7a3b9c"
    }
    answer=http_requests.get("https://api.themoviedb.org/3/movie/now_playing",params=params)
    sql_movie_attributes=['movie_id','title','overview','original_title']
    json_movie_attributes=['id','title','overview','original_title']
    TMDB_rows=answer.json()['results']
    #TMDB_rows=TMDB_rows[0:len(TMDB_rows)-2]
    SQL_movies=list(map(usefull_keys,Movie.query.all()))
    SQL_movies=TheaterSet(SQL_movies,sql_movie_attributes)
    TMDB_movies=TheaterSet(TMDB_rows,json_movie_attributes)
    ONLY_TMDB_movies=TMDB_movies-SQL_movies
    ONLY_SQL_movies=SQL_movies-TMDB_movies
    deleted_ids=tuple(map(lambda row:int(row[0]),ONLY_SQL_movies))
    #print(deleted_ids)
    if(len(deleted_ids)!=0): 
        Movie.query.filter(Movie.movie_id.in_(deleted_ids)).delete()
        db.session.commit()
    added_movies=[]
    added_directors=[]
    for row in ONLY_TMDB_movies:
        added_movies.append(Movie(*row))
        for director in directors_to_add(row[0]):
            added_directors.append(Director(director['id'],director['name'],row[0]))
    for added in [added_movies,added_directors]:
        db.session.add_all(added)
        db.session.commit()
    
    return render_template("Welcome.html",movies=Movies_Directors())
    
    #json_movies=request.args.get("greek_movies")




if __name__=="Main":
    app.run(debug=True)