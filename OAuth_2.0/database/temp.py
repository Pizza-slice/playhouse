import requests
import hashlib
username ="alonf"
password = "212729065"
response = requests.get("http://localhost:3000/authorize",params={"client_id":"75e94364aa12469082f0a43e611d034d", "response_type":"code", "redirect_uri":"localhost:3635"}).json()
print(response)
cookie = response["cookie"]
has = hashlib.sha256(password.encode()).hexdigest()
response = requests.post("localhost:3000/log_in/"+cookie , data={"username":username, "hashpassword":has }).json()
code = response["code"]
response = requests.post("localhost:3000/api/token", data={"grant_type":"authorization_code", "code":code, "redirect_uri":"localhost:3635", "client_id":"75e94364aa12469082f0a43e611d034d", "client_secret":"66b789261f394818a6ad2446bc68ec58"}).json()
print(response)