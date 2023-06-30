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

    apiKey = "56684e5e2e39c107f953e139fa0ea82d-us21";

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

