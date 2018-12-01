const http = require('http');
const fs = require('fs');

var server = http.createServer(getFromClient);

server.listen(3000);
console.log('Server is running.');

function getFromClient(req, res){
    request = req;
    response = res;
    fs.readFile('./index.html', 'UTF-8',
        (error, data)=> {
            var content = data.
                replace(/dummy_title/g, 'this is title').
                replace(/dummy_content/g, 'this is content');

            response.writeHead(200, {"Content-Type": 'text/html'});
            response.write(data);
            response.end();
        }
    );
}