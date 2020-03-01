const sqlite3 = require('sqlite3').verbose();
const user_db = new sqlite3.Database('database\\users.db');
function check_login() {
    return new Promise((resolve, reject) => {
      user_db.all("SELECT * FROM users", [], (err, rows) => {
        if (err) reject(err);
        else resolve(rows);
      });
    })
}
async function test(){
    try{
        const user_row = await check_login();
        console.log(user_row)
    }catch(e){
        console.log(e)
    }
}
test();
