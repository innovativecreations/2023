const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.use(express.static("public/"))

app.use(bodyParser.urlencoded({extended:true}))

app.get("/", function(req, res){
    res.sendFile(__dirname + "/signup.html");
});

app.post("/", function(req, res){
    
    var fName = req.body.fName;
    var lName = req.body.lName;
    var email = req.body.email;
     console.log(fName, lName, email);
    // if(pass){
    //     res.send("Registed successfully");
    // }
    // else{
    //     res.send("SOme issue occured");
    // }
    res.send("YO! I got you");
});

app.listen("3000");

