const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.urlencoded({extended:true}));

app.get("/", function(req, res){
    res.sendFile(__dirname + "/index.html")
});
app.post("/", function(res, req){
    var n1 = Number(res.body.num1);
    var n2 = Number(res.body.num2);
    result = n1 + n2;
    console.log(res.body.num1);
    req.send("You clicked the calculate button and your ans is " + result);
});
app.listen(3000);