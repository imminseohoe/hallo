var script_array = ['Is it your first time to see a talking pumpkin?', 'How about sending candy to your friends?', 'The scariest pumpkin is me!', 'Are you provoking a quarrel?', "You scared me, didn't you?", "I am the strongest pumpkin", 'Halloween parties are always wonderful!'];
var click = 0;
var tt = true;
var ttt = true;
function myFunction() {
  var csrftoken = getCookie('csrftoken');

  $.ajax({
    url: '/mypage/<str:username>/update_click_count/',
    type: 'POST',
    dataType: 'json',
    beforeSend: function(xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    },
    success: function(response) {
      if (response.success) {
        console.log('클릭 횟수가 업데이트되었습니다.');
      } else {
        console.error('클릭 횟수 업데이트 실패');
      }
    },
    error: function(xhr, textStatus, error) {
      console.error('AJAX 요청이 실패했습니다.');
    }
  });

  if (click >= 30) {
    document.querySelector(".speech-bubble").innerText = "don't hit me...";
  } else {
    click += 1;
    var index = Math.floor(Math.random() * 7);
    document.querySelector(".speech-bubble").innerText = script_array[index];
  }
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