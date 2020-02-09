const express = require('express')
const fs = require('fs');
const app = express()
const port = 3000

app.get('/authorize', (req, res) => {
    if (isClientIdExsist(req.query.clIent_id)) {
        if (req.query.response_type != "code"){
            if(check_redirect_uri(req.query.client_id, req.query.redirect_uri)){
                res.json({"cookie":create_cookie(req.query)})
            }
            else{
                res.json({"error":"redirect_uri isn't acceptable"})
            }
        }
        else{
            res.json({"error":"response_type need to be code"})
        }
    }
    else{
        res.json({"error":"client_id not found"})
    }
});
app.post("/log_in/:cookie", (req, reponse) =>{
    req.params.userid

})
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
    let json_data = {"client_id":req_query.clIent_id, "redirect_uri": req_query.redirect_uri, "scope": req_query.scope.split(" ")};
    fs.writeFile(`cookies\\${cookie}.json`, JSON.stringify(json_data), 'utf8', function (err) {
        console.log(err);
    });
    return cookie;
}

function makeid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
       result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
 }
app.listen(port, () => console.log(`Example app listening on port ${port}!`))