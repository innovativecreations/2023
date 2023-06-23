const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.urlencoded({extended:true}));

app.get("/", function(req, res){
    res.send("<h1>Nachhhhoooo!</h1>");
})

app.get("/contact", function(req, res){
    res.send("innovativecreations195@gmail.com");
})

app.get("/about", function(req, res){
    res.send("<h2>YO! This is Awesome Mayank, Feeling nice to meet me,  right?, I know. I'm an awesome guy from India. Who is trying to figure out how the things work.</h1>");
})

app.get("/bmicalculator", function(req, res){
    h = Number(req.body.height);
    w = Number(req.body.weight);
    bmi = w / h * h;
    res.sendFile(__dirname + "/bmi.html");
});
app.post("/bmicalculator" , function(req, res){
    var h = parseFloat(req.body.height);
    var w = parseFloat(req.body.weight);
    var bmi = w / (h * h);

    res.send("Your BMI is : " + bmi);
});
app.listen(3000, function(){
    console.log("Nacho, your server has been started on localhost:3000");
})