var script_array = ['Is it your first time to see a talking pumpkin?', 'How about sending candy to your friends?', 'The scariest pumpkin is me!', 'Are you provoking a quarrel?', "You scared me, didn't you?", "I am the strongest pumpkin", 'Halloween parties are always wonderful!'];
var click = 0;
var tt = true;
var ttt = true;

function myfunction() {
  if (click >= 30) {
    document.querySelector(".speech-bubble").innerText = "don't hit me...";
  } else {
    click += 1;
    var index = Math.floor(Math.random() * 7);
    document.querySelector(".speech-bubble").innerText = script_array[index];
  }
}
