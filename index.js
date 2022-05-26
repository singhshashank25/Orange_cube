const express = require('express');
const app = express();
const session = require('express-session');



app.use(express.static('static'));
app.set('view engine', 'ejs');


app.get('/', function(req, res) {
    res.render('home');
  });


app.listen(process.env.PORT || 3002, function() {
console.log('Server started at port 3002')
// console.log(data);
})


