const express = require("express");
const bodyParser = require("body-parser");
const day = require(__dirname +"/day.js")

const app = express();

app.set("view engine", "ejs");

app.use(express.static("public"));

app.use(bodyParser.urlencoded({extended:true}));

const dailyKaKaam = ["Eat", "Code"];
const workListKaKaam = [];

app.get("/", (req, res) => {
    const din = day.dateChahia();
    res.render("template",{listKaNaam : din, kaam: dailyKaKaam});
});

app.post("/", (req, res) => {
    if(req.body.add === "Work"){
        workListKaKaam.push(req.body.kaam)
        res.redirect("/work");
    }
    else{
        
    dailyKaKaam.push(req.body.kaam);
    res.redirect("/");
    }
});

app.get("/work", (req,res)=>{
    res.render("template", {listKaNaam: "Work", kaam: workListKaKaam});
});


app.listen(3000);