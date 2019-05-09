var express = require('express');
var router = express.Router();
var WAF = require('../WAF')
var RES = require('../RES')


/* GET home page. */
router.get('/', function(req, res, next) {

  req = WAF(req);
  //str 代表给 res 传递的内容，若发现内容中含有 flag，则流量另存
  str = 'flag'
  RES(req, str);
  
  res.render('index', { title: 'Express' });
});

router.post('/', function(req, res, next) {

  req = WAF(req);
  //str 代表给 res 传递的内容，若发现内容中含有 flag，则流量另存
  str = 'flag'
  RES(req, str);

  res.render('index', { title: 'Express' });
  
});

module.exports = router;
