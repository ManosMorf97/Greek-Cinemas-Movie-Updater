import requests as http_requests


def TheaterSet(results,attributes):
    if results == None:
        return set()
    results=list(map(lambda result:{attribute:result[attribute] for attribute in attributes},results))
    results=list(map(lambda result:tuple(result.values()),results))
    results=set(results)
    return results

def usefull_keys(movie):
        returned=movie.__dict__
        del returned['_sa_instance_state']
        return returned
    
def directors_to_add(movie_id):
        params={
            "api_key":"bbb0e77b94b09193e6f32d5fac7a3b9c"
        }
        results=http_requests.get("https://api.themoviedb.org/3/movie/"+str(movie_id)+"/credits",params=params)
        results=results.json()['crew']
        directors=list(filter(lambda result:result["job"]=="Director",results))
        return directors

def Movie_dict(keys,values):
    movie_dict={}
    for key,value in zip(keys,values):
        movie_dict[key]=value
    return movie_dict