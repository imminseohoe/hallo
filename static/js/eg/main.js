var click = 0;


function myFunction() {
  var imageElement = document.getElementById("pumpkin");
  var elee = document.getElementById("interior");
  var csrftoken = getCookie('csrftoken');
  var eeee = document.getElementById("페이지")
  $.ajax({
    url: '/mypage/<str:username>/update_click_count/',
    type: 'POST',
    dataType: 'json',
    beforeSend: function(xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    },
    success: function(response) {

    },
    error: function(xhr, textStatus, error) {

    }
  });
  click += 1

  if (click >= 1) {
    document.querySelector(".speech-bubble").innerText = "don't hit me...";
    document.querySelector(".speech-bubble").style.display = "none";
  }
  var maxX = window.innerWidth - imageElement.clientWidth; 
  var minusX = elee.clientWidth;
  var maxY = window.innerHeight - imageElement.clientHeight; 
  var minusY = eeee.clientHeight;
  var randomX = Math.floor((Math.random() * (maxX - minusX))+ minusX);
  var randomY = Math.floor((Math.random() * (maxY - minusY))+ minusY+10);

  imageElement.style.position = "absolute";
  imageElement.style.left = randomX + "px";
  imageElement.style.top = randomY + "px";
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
