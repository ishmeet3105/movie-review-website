const URL='http://127.0.0.1:8000/movies/';
const mov=document.querySelector("#movie")
const getmovie= async () => {
    let resp=await fetch(URL);
console.log(resp);
let data= await resp.json();

mov.innerText=data.movies[0]["title"];
};
