const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.urlencoded({extended:true}))

app.get("/", function(req, res){
    res.sendFile(__dirname + "/signup.html");
});

app.get("/", function(req, res){
    if(pass){
        res.send("Registed successfully");
    }
    else{
        res.send("SOme issue occured");
    }
});

app.listen("3000");

