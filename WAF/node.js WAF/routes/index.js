var express = require('express');
var router = express.Router();
var WAF = require('../WAF')
var RES = require('../RES')


/* GET home page. */
router.get('/', function(req, res, next) {
  req = WAF(req);
  res.render('index', { title: 'Express' });
});

router.post('/', function(req, res, next) {
  req = WAF(req);
  str = 'flag'
  RES(req, str);
  res.render('index', { title: 'Express' });
  
});

module.exports = router;
