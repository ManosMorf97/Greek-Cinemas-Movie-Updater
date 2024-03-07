let spanners=document.getElementsByTagName("span");

/*
<div class="external-div">
                <h1>Batman Begins</h1>
                <h2>2005</h2>
                <img src="img1.jpg" alt="none" width="200" height="200" />
                <br>
                <div class="bottom">
                    <a href="" id="more" >more..</a>
                </div>
                <br>
            </div>
            <div class="external-div">
                <h1>Batman Begins</h1>
                <h2>2005</h2>
                <img src="img1.jpg" alt="none" width="200" height="200" />
                <br>
                <h3>Movie</h3>
                <h3>tt0372784</h3>
                <button class="buttonS">LIKE</button>
                <div class="bottom">
                    <a href="" >less</a>
                </div>
                <br>
            </div>




*/
if(localStorage.getItem("LoggedIn")===null||localStorage.getItem("LoggedIn")===undefined){
    let body=document.getElementsByTagName("body")[0].style;
    body.opacity="0.3";
    body["pointer-events"]="none";
}

function changeindexedcolor(i){
    return function changecontentcolor(e){
        console.log("WWWWWWWWWWW")
        spanners[i].classList.add("hoveredspan");
    }
    
}
for(let i=0; i<spanners.length; i++){
    spanners[i].addEventListener("mouseover",changeindexedcolor(i));
}

function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}


async function getMovies(url){
    const response=await fetch(url)
    return response.json()

}

async function getMoviesJson(url){
    const response_json=await getMovies(url)
    return response_json.Search
}

async function getBlob(url){
    const response=await fetch(url)
    return response.blob()
}

async function getImageURL(url){
    const blob=await getBlob(url)
    return URL.createObjectURL(blob)
}

document.onreadystatechange(async ()=>{
    let movie_at=document.getElementsByClassName("movies")[0]
    removeAllChildNodes(movie_at)
    let search_value=document.getElementById("inputSearch").value
    let url="https://api.themoviedb.org/3/movie/now_playing?region=gr&api_key=bbb0e77b94b09193e6f32d5fac7a3b9c"
    if(search_value===undefined || search_value==="")
    return -1;
    let movies=await getMoviesJson(url)
    console.log(movies)
    if(movies===undefined)
    return -1;
    for(let movie of movies){
    let external_div=document.createElement("div")
    external_div.classList.add("external-div")
    let attributes=["h1","h2"]
    let properties=[movie.Title,movie.Year]
    for(let i=0; i<2; i++){
        let element=document.createElement(attributes[i])
        let text=document.createTextNode(properties[i])
        element.appendChild(text)
        external_div.appendChild(element)
    }
    let imageURL=await getImageURL(movie.Poster)
    let img_el=document.createElement("img")
    img_el.setAttribute("src",imageURL)
    img_el.setAttribute("alt","none") //make it better
    img_el.setAttribute("width","200")
    img_el.setAttribute("height","200")
    external_div.appendChild(img_el)
    external_div.appendChild(document.createElement("br"))
    let bottom_div=document.createElement("div")
    bottom_div.classList.add("bottom")
    let a_bottom=document.createElement("a")
    a_bottom.setAttribute("href","")
    a_bottom.setAttribute("id","more"+movie.imdbId)
    a_bottom.appendChild(document.createTextNode("more.."))
    bottom_div.appendChild(a_bottom)
    external_div.appendChild(bottom_div)
    external_div.appendChild(document.createElement("br"))
    movie_at.appendChild(external_div)
}

})





