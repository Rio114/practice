const http = require('http');
const fs = require('fs');
const ejs = require('ejs');
const url = require('url');
const qs = require('querystring');

const index_page = fs.readFileSync('./index.ejs', 'utf8');
const other_page = fs.readFileSync('./other.ejs', 'utf8');
const style_css = fs.readFileSync('./style.css', 'utf8');

var server = http.createServer(getFromClient);

server.listen(3000);
console.log('Server is running.');

function getFromClient(request, response){
    var url_parts = url.parse(request.url, true);
    switch (url_parts.pathname){
        case '/':

            response_index(request, response);
            break;

        case '/other':
            response_other(request, response);
            break;

        case '/style.css':
            response.writeHead(200, {'Content-Type': 'text/css'});
            response.write(style_css);
            response.end();
            break;

        default:
            response.writeHead(200, {'Content-Type': 'text/plain'});
            response.end('no page....');
            break;
    }
}

var data = {
    'Taro': '090-9999-9999',
    'Hanako': '080-8888-8888',
    'Sachiko': '070-7777-7777',
    'Ishiro': '060-6666-6666'
};


function response_index(request, response){
    var msg = 'This is index page.';
    var content = ejs.render(index_page, {
        title:'Index',
        content:msg,
        data:data,
    });
    response.writeHead(200, {'Content-Type': 'text/html'});
    response.write(content);
    response.end();
}

function response_other(request, response){
    var msg = 'This is other page.\n'
    if (request.method == 'POST'){
        var body = '';
        request.on('data', (data)=>{
            body += data;
        });

        request.on('end', ()=> {
            var post_data = qs.parse(body);
            msg += 'you have written [' + post_data.msg + ']';
            var content = ejs.render(other_page, {
                title:'Other',
                content: msg,
            });
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write(content);
            response.end();
        });
    }else{
        var msg = 'this page does not exist'
        var content = ejs.render(other_page, {
            title:'Other',
            content: msg,
        });

        response.writeHead(200, {'Content-Type': 'text/html'});
        response.write(content);
        response.end();
    }
}