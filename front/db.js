// Defines de connection to de DB
var mysql      = require('mysql');
var connection = mysql.createPool({
  host     : 'localhost',
  user     : 'user_taller2',
  password : 'taller2.',
  database : 'taller2'
});

module.exports = connection; 