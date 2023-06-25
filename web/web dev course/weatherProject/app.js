const express = require("express");
const bodyParser = require("body-parser");


const https = require("https");

const app = express();

app.use(bodyParser.urlencoded({extended:true}));
app.get("/", function(req, res){
    res.sendFile(__dirname + "/index.html");
});

app.post("/", function(req, res){
    var city = req.body.city;
    console.log(city);
    const appId = "bbc186e6f89739be484947f5c6a176da";
    const units = "metric"
    const url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+appId+"&units="+units;
    console.log(url);
    https.get(url , function(resp){
        console.log(resp.statusCode)
        
        resp.on("data", function(data){
              
                const da = JSON.parse(data);
                console.log(da);
                const weatherDes= da.weather[0].description;
                const temp = da.main.temp;
                const icon = da.weather[0].icon;
                const imgUrl = "https://openweathermap.org/img/wn/"+icon+"@2x.png"
                res.write("<p> Weather would be more like: " + weatherDes +"</p>");
                res.write("<h1> The temperature  in "+ city +" is : "+temp+"</h1>");
                res.write("<img src="+imgUrl+">");
                res.send();
        });
    });

    // res.sendFile(__dirname + "/index.html");
});

app.listen(3000);
