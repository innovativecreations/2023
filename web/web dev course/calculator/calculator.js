const express = require("express");

const app = express();

app.get("/", function(req, res){
    res.sendFile(__dirname + "/index.html")
});
app.post("/", function(res, req){
    console.log(res);
    req.send("You clicked the calculate button");
});
app.listen(3000);