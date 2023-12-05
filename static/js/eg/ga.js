
document.addEventListener("DOMContentLoaded", function () {
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
    
    const canvas = document.getElementById("game-canvas");
    const context = canvas.getContext("2d");
    let isGameOver = false;
    var sc = 0
    const presentImage = new Image();
    presentImage.src = "/static/img/present.png";
    const playerImage = new Image();
    playerImage.src = "/static/img/stand.png";
    const poopImage = new Image();
    poopImage.src = "/static/img/snow.png";

    const maxPoopInterval = 600; 
    let poopInterval = maxPoopInterval; 
    function updateScore() {
      if(!isGameOver){
        sc++;
        document.querySelector('#score').innerText = sc;}
    }
    const player = {
      x: canvas.width / 2 - 25,
      y: 330,
      width: 50,
      height: 66,
      image: playerImage,
      speed: 5, 
      dx: 0, 
    };
  
    const poops = [];
    const presents = [];
    function drawPlayer() {
      context.drawImage(player.image, player.x, player.y, player.width, player.height);
    }
    function drawPresents() {
      for (let i = 0; i < presents.length; i++) {
        const present = presents[i];
        context.drawImage(present.image, present.x, present.y, present.width, present.height);
      }
    }
    function drawPoops() {
      for (let i = 0; i < poops.length; i++) {
        const poop = poops[i];
        context.drawImage(poop.image, poop.x, poop.y, poop.width, poop.height);
      }
    }
  
    function updatePlayerPosition() {
      player.x += player.dx;
  

      if (player.x < 0) {
        player.x = 0;
      } else if (player.x + player.width > canvas.width) {
        player.x = canvas.width - player.width;
      }
    }
    function generatePresent(){
      const presnt = {
        x: Math.random() * (canvas.width - 50),
        y: 0,
        width: 30,
        height: 30,
        image: presentImage,
      };
      presents.push(presnt);
    }
    function generatePoop() {
        const poop = {
          x: Math.random() * (canvas.width - 50),
          y: 0,
          width: 30,
          height: 30,
          image: poopImage,
        };
        poops.push(poop);
      

        poopInterval = 1000
      

      }
    function updatePresentPosition(){
      for (let i = 0; i < presents.length; i++) {
        const presnt = presents[i];
        presnt.y += 5;
  
        if (presnt.y > canvas.height) {
          presents.splice(i, 1); 
        }
        if (checkCollision(player, presnt)) {
          updateScore()
          
        }
      }
    }
    function updatePoopPosition() {
      for (let i = 0; i < poops.length; i++) {
        const poop = poops[i];
        poop.y += 5;
  
        if (poop.y > canvas.height) {
          poops.splice(i, 1); 
        }
  
        if (checkCollision(player, poop)) {
          gameOver();
        }
      }
    }

    function checkCollision(rect1, rect2) {
      return (
        rect1.x < rect2.x + rect2.width &&
        rect1.x + rect1.width > rect2.x &&
        rect1.y < rect2.y + rect2.height &&
        rect1.y + rect1.height > rect2.y
      );
    }
    function gameOver() {
        var csrftoken = getCookie('csrftoken');
        isGameOver = true;
      
        context.font = "40px Arial";
        context.fillStyle = "red";
        context.textAlign = "center";
        context.fillText("Game Over", canvas.width / 2, canvas.height / 2);
        $.ajax({
            url: '/mypage/<str:username>/update_score/',
            type: 'POST',
            dataType: 'json',
            data: {
              'score': sc
            },
            beforeSend: function(xhr, settings) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            success: function(response) {
        
            },
            error: function(xhr, textStatus, error) {
        
            }
        });
        const retryButton = document.createElement("button");
        retryButton.innerText = "Retry";
        retryButton.classList.add("retry-button"); 
        retryButton.addEventListener("click", resetGame);
        document.body.appendChild(retryButton);
      }
    function resetGame() {
        isGameOver = false;
        sc = 0;
        poops.length = 0;
        presents.length = 0;
        document.querySelector('#score').innerText = sc;
        document.body.removeChild(document.querySelector("button"));
        gameLoop();
      }
  
    function gameLoop() {
        context.clearRect(0, 0, canvas.width, canvas.height);
      
        drawPlayer();
        drawPoops();
        drawPresents()
        
      ;
        updatePlayerPosition();
        updatePoopPosition();
        updatePresentPosition();
      
        if (!isGameOver) {
          requestAnimationFrame(gameLoop);
        }
      }

    document.addEventListener("keydown", function (event) {
      if (event.key === "ArrowLeft") {
        player.dx = -player.speed;
      } else if (event.key === "ArrowRight") {
        player.dx = player.speed;
      }
    });
  
    document.addEventListener("keyup", function (event) {
      if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
        player.dx = 0;
      }
    });
  
    setInterval(generatePoop, 500);
    
    setInterval(generatePresent, 331)
    gameLoop();
  });