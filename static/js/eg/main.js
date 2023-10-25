var script_array = ['Is it your first time to see a talking pumpkin?', 'How about sending candy to your friends?','The scariest pumpkin is me!', 'Are you provoking a quarrel?',"You scared me, didn't you?","I am the strongest pumpkin",'Halloween parties are always wonderful!']
var click = 0
var tt = true
var ttt = true
function myFunction() {
  if (click >= 100) {
    document.querySelector(".speech-bubble").innerText = 'dsadja'
    ttt = false
  } else if (click >= 30 && ttt) {
    document.querySelector(".speech-bubble").innerText = "Don't hit me... its hurt.."
    document.querySelector(".speech-bubble").innerText = script_array[index]
  }
}