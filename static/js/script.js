function addUser() {
  var user = document.getElementById("user").value;
  var password = document.getElementById("password").value;
  var xhr = new XMLHttpRequest();
  xhr.open("POST", '/add-user', true);
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
            // Reload the page to display the new user
      location.reload();
    }
  };
  var userdata = JSON.stringify({"user": user,"password": password});
  xhr.send(userdata);
}

function deleteUser() {
  var user = document.getElementById("del_user").value;
  var password = document.getElementById("del_password").value;
  var xhr = new XMLHttpRequest();
  xhr.open("DELETE", '/delete-user', true);
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
            // Reload the page to display the new user
      location.reload();
    }
  };
  var deluserdata = JSON.stringify({"user": user,"password": password});
  xhr.send(deluserdata);
}

