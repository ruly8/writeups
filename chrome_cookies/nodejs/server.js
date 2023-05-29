'use strict';

const express = require('express');
const cookieParser = require("cookie-parser");

// Constants
const PORT = 9090;
const HOST = '0.0.0.0';

// App
const app = express();
app.use(cookieParser());
app.use(express.static(__dirname));
app.get('/', (req, res) => {
  res.send('Hello World');
});
app.get('/set', (req, res) => {
    //var input = 'D800';
    //var decimalValue = parseInt(input, 16); // Base 16 or hexadecimal
    //var key = String.fromCharCode(decimalValue);
    //res.cookie(c, 'set via node/express');
    //var key = decodeURI("\ud800");
    var value = "set via response doc inline";
    var html = `<p id="demo"></p>\n`;
    html += `<script src="/script.js">\n`;
    html += `document.getElementById("demo").innerHTML = document.cookie;</script>`;
    res.send(html);
});
app.get('/read', (req, res) => {
    res.send(req.cookies);
    console.log(req.cookies);
})

app.listen(PORT, HOST, () => {
  console.log(`Running on http://${HOST}:${PORT}`);
});
