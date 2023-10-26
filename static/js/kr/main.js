var script_array = ['말하는 호박 처음봐?', '친구한테 사탕한번 보내봐','가장 무서운 호박은 나야! ', '시비거는 거냐?','나 엄청 무섭지? 겁먹었지?','나는 최강의 호박이다','할로윈 파티는 언제나 짜릿해'];
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

  if (click >= 100) {
    document.querySelector(".speech-bubble").innerText = '나삐짐';
    ttt = false;
  } else if (click >= 30 && ttt) {
    document.querySelector(".speech-bubble").innerText = '그만 때려.. 아파..';
    tt = false;
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