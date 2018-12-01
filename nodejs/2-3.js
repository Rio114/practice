const http = require('http');

var server = http.createServer(
    (request, response)=> {
        response.setHeader('Content-Type', 'text/html');
        response.write('<!DOCTYPOE html><html land="ja">');
        response.write('<head><met charset="uft-8">');
        response.write('<title>Hello</title></head>');
        response.write('<body><h1>Hello node.js!</h1>');
        response.write('<p>This is Node.js sample page.</p>');
        response.write('</body></html>');
        response.end();
    }
);

server.listen(3000);
console.log('Server is running.');