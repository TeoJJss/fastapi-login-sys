function login(){

    var host = "127.0.0.1";
    var port = "8000";
    var base_url = `http://${host}:${port}`;

    var name = document.getElementById("name").value;
    var password = document.getElementById("password").value;

    const xhr = new XMLHttpRequest();
    xhr.open("POST", `${base_url}/ticket`);
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
        xhr2.open("GET", `${base_url}/auth?ticket=${tic}`);
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