const express = require('express');
const bodyParser = require('body-parser')
const fs = require('fs');
const https = require('https');
const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
const sqlite3 = require('sqlite3').verbose();
const user_db = new sqlite3.Database('database\\users.db');
const code_db = new sqlite3.Database('database\\codes.db');
const port = 3000;

app.get('/authorize', (req, res) => {
    if (isClientIdExsist(req.query.clIent_id)) {
        if (req.query.response_type != "code"){
            if(check_redirect_uri(req.query.client_id, req.query.redirect_uri)){
                res.json({"cookie":create_cookie(req.query)});
            }
            else{
                res.json({"error":"redirect_uri isn't acceptable"});
            }
        }
        else{
            res.json({"error":"response_type need to be code"});
        }
    }
    else{
        res.json({"error":"client_id not found"});
    }
});
app.post("/log_in/:cookie", (req, res) =>{
    let cookie = req.params.userid;
    if (cookie != "")
    {
        let user_id = check_login(req.body.username, req.body.hashpassword)
        if( user_id != ""){
            let code = create_code(get_info_by_cookie(cookie, user_id));
            res.json({"code":code})
        }
        else{
            res.json({"error":"username or password doesn't match"})
        }

    }
    else{
        res.json({"error":"no cookie was given"})
    }
        

});
app.post("/api/token",(req, res) =>{
    if(req.body.grant_type == "authorization_code"){
        if(!is_code_available(req.body.code)){
            let redirect_uri = get_redirect_uri(req.body.code)
            if(redirect_uri != ""){

            }
            else{
                res.json({"error": "redirect_uri need to be the same one that used to get the code"})
            }
        }
        else{
            res.json({"error":"code not found"})
        }
    }
    else{
        res.json({"error":"grant_type need to be authorization_code"})
    }
});
function get_redirect_uri(code){
    code_db.each("SELECT code,redirect_uri FROM code_table", function(err, rows) {
        rows.forEach((row) =>{
            if(row.code == code)
                return row.redirect_uri;
        });
        return "";
    });
}
}
function create_code(json_data, user_id){
    is_done = false;
    while(is_done){
        temp_code = makeid(10);
        if(is_code_available(temp_code))
            is_done= true;
    }
    let stmt = code_db.prepare("INSERT INTO code_table VALUES (?,?,?,?,?)");
    stmt.run(temp_code, json_data.client_id, json_data.scope, user_id, json_data.redirect_uri);
    stmt.finalize();
    return temp_code;
}

function is_code_available(temp_code){
    code_db.each("SELECT code FROM code_table", function(err, rows) {
        rows.forEach((row) =>{
            if(row.code == temp_code)
                return false;
        });
        return true;
    });
}
function get_info_by_cookie(file_name){
    let rawdata = fs.readFileSync('student.json');
    let json_data = JSON.parse(rawdata);
    return json_data;
}
function isClientIdExsist(client_id) {
    fs.readdirSync("apps").forEach(file => {
        if(file == client_id){
            return true;
        }
    });
    return false;
}
function check_redirect_uri(client_id, redirect_uri){
    let rawdata = fs.readFileSync(`apps\\${client_id}`);
    let app = JSON.parse(rawdata);
    return (app.redirect_uri ==redirect_uri)
}
function create_cookie(req_query){
    let cookie = makeid(7);
    let json_data = {"client_id":req_query.client_id, "redirect_uri": req_query.redirect_uri, "scope": req_query.scope.split(" ")};
    fs.writeFile(`cookies\\${cookie}.json`, JSON.stringify(json_data), 'utf8', function (err) {
        console.log(err);
    });
    return cookie;
}

function makeid(length) {
    let result           = '';
    let characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let charactersLength = characters.length;
    for ( let i = 0; i < length; i++ ) {
       result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
 }
 function check_login(username, hashpassword){
    user_db.each("SELECT user_id, username, hashpassword FROM users", function(err, rows) {
        rows.forEach((row) =>{
            if(row.username == username && row.hashpassword == hashpassword)
                return row.user_id;
        });
        return "";
    });
}
app.listen(port, () => console.log(`Example app listening on port ${port}!`))