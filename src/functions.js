const host = "127.0.0.1";
const port = "8000";
const base_url = `http://${host}:${port}`;

function login(){
  var name = document.getElementById("name").value;
  var password = document.getElementById("password").value;

  const xhr = new XMLHttpRequest();
  xhr.open("POST", `${base_url}/api/ticket`);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
  const body = JSON.stringify({
    name: name,
    password: password
  });
  xhr.onload = () => {
    if (xhr.status == 201) {
      var res = JSON.parse(xhr.responseText);
      var tic = res.ticket; 

      const xhr2 = new XMLHttpRequest();
      xhr2.open("GET", `${base_url}/api/auth?ticket=${tic}`);
      xhr2.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      xhr2.setRequestHeader('Access-Control-Allow-Origin', '*');
      xhr2.onload = () => {
        if (xhr2.status == 200) {
          var res2 = JSON.parse(xhr2.responseText);
          var name = res2.username;
          alert("Good day, " + name);
          sessionStorage.setItem('ticket', tic);
          location.href = "home.html";
        }else if (xhr2.status == 401){
          alert("Unauthorized access! Please login again.");
        }
      }
      xhr2.send();
    } else {
      console.log(`Error: ${xhr.status}`);
    }
  };
  xhr.send(body);
}

function home(){
  const ticket = sessionStorage.getItem('ticket');

  if (ticket != null){
      const xhr2 = new XMLHttpRequest();
      xhr2.open("GET", `${base_url}/api/auth?ticket=${ticket}`);
      xhr2.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      xhr2.setRequestHeader('Access-Control-Allow-Origin', '*');
      xhr2.onload = () => {
        if (xhr2.status == 200) {
          var res2 = JSON.parse(xhr2.responseText);
          document.getElementById("username").innerHTML = res2.username; 
        }else if (xhr2.status == 401){
          alert("Unauthorized access! Please login again.");
          location.href = "index.html";
        }else{
          alert("Unexpected issue occurs.");
          location.href = "index.html";
        }
      }
      xhr2.send();
  }else{
      location.href = "index.html";
  }
}