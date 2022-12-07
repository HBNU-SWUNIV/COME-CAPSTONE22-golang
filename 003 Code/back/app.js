var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

const passport = require('passport');
const session = require('express-session');
// const zmq = require("zeromq")

require('dotenv').config();
require('./passport').config(passport);

//route
var indexRouter = require('./routes/index');
var memberRouter = require('./routes/member');
var loginRouter = require('./routes/login');
var productRouter = require('./routes/product');
var warehousingRouter = require('./routes/warehousing');

var salesRouter = require('./routes/sales');
var shipmentRouter = require('./routes/shipment');

var monitoringRouter = require('./routes/monitoring');

var statisticsRouter = require('./routes/statistics');

var inventoryRouter = require('./routes/inventory');
var commuRouter = require('./routes/commu');


var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));


//passport
app.use(session({
  resave: false,
  saveUninitialized: false,
  secret: process.env.COOKIE_SECRET,
  cookie: {
    httpOnly: true,
    secure: false,
  }
}));
app.use(passport.initialize());
app.use(passport.session());




//route
app.use('/', indexRouter);
app.use('/api/member',memberRouter);
app.use('/api/product',productRouter);
app.use('/api/login',loginRouter);
app.use('/api/warehousing',warehousingRouter);
app.use('/api/sales',salesRouter);
app.use('/api/shipment',shipmentRouter);
app.use('/api/inventory',inventoryRouter);
app.use('/api/monitoring',monitoringRouter);
app.use('/api/statistics',statisticsRouter);
app.use('/api/community',commuRouter);




// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});


// zeromq
// async function run() {
//   const sock = new zmq.Request

//   sock.connect("tcp://127.0.0.1:3000")
//   console.log("Producer bound to port 3000")

//   await sock.send("4")
//   const [result] = await sock.receive()

//   console.log(result)
// }

// run()




module.exports = app;