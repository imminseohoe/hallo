var script_array = ['말하는 호박 처음봐?', '친구한테 사탕한번 보내봐','가장 무서운 호박은 나야! ', '시비거는 거냐?','나 엄청 무섭지? 겁먹었지?','나는 최강의 호박이다','할로윈 파티는 언제나 짜릿해']
var click = 0
var tt = true
var ttt = true
function myFunction() {
  if (click >= 100 && ttt) {
    document.querySelector(".speech-bubble").innerText = "흥 나 삐짐!"
    ttt = false
  } else if (click >= 30 && tt && ttt) {
    document.querySelector(".speech-bubble").innerText = '그만 때려.. 아파..'
    tt = false
  } else {
    click += 1
    var index = Math.floor(Math.random() * 7);
    document.querySelector(".speech-bubble").innerText = script_array[index]
  }
}