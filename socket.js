// let websocket = require('websocket').server;
let express = require('express')();
let http = require('http').Server(express);
let io = require('socket.io')(http);


express.get('/', function(req, res){
  res.sendFile(__dirname+'/index.html');
})
io.on('connection', function(req, res) {
  console.log('A new co etablished : ', res)
})
setInterval(function(){
  let data = 'datatest'
  io.emit('event', data)

}, 10)
http.listen(5000, function(){
  console.log('Listening ')
})
