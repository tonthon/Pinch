// let websocket = require('websocket').server;
let express = require('express')();
let http = require('http').Server(express);
let io = require('socket.io')(http);


express.get('/', function(req, res){
  res.sendFile(__dirname+'/index.html');
})

io.sockets.on('connection', function(socket) {

  socket.emit('start', 'Hello you connected to me, Server')
  socket.on('start', function(response){
    console.log('client send :'+ response)
  })

})
setInterval(function(){
  let data = 'datatest'
  // io.emit('event', data)
}, 10)

http.listen(5000)
