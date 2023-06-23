const express = require('express');

const app = express();

app.get("/", function(req, res){
    res.send("<h1>Nachhhhoooo!</h1>");
})

app.get("/contact", function(req, res){
    res.send("innovativecreations195@gmail.com");
})

app.get("/about", function(req, res){
    res.send("<h2>YO! This is Awesome Mayank, Feeling nice to meet me,  right?, I know. I'm an awesome guy from India. Who is trying to figure out how the things work.</h1>");
})

app.listen(3000, function(){
    console.log("Nacho, your server has been started on localhost:3000");
})