# platforming_framework Pre-Alpha version 0.1

<h1 id = "header" >A platforming framework in pygame</h1>

<h2 id="TODO">
  <p>Current Goals:<br>support sprites for platforms and goals<br>spritesheets and animations<br>more configurable jumping, movmement, and gravity<br>platform side-specific collision detection<br>more configurable win conditions</p>
</h2>

<h2>Classes and Functions</h2>
  <div id = "game objects">
    <p><a href="#player_explanation">player</a></p>
    <p><a href="#platform_explanation">platform</a></p>
    <p><a href="#goal_explanation">goal</a></p>
  </div>
  
  <br>
  <br>
  
  <div id = "player_explanation">
    <h3>Player</h3>
    <p>player = platforming_framework.player(sprite, x, y): creates a new player sprite</p>
    <p>player.go(x, y): moves the player in the x & y direction by the specified amounts</p>
    <p>player.jump(): makes the player jump</p>
    <p>player.refresh(): should be called every frame, handles rendering, movement, jumping, and gravity</p>
  </div>
  
  <br>
  <br>
  
   <div id = "platform_explanation">
      <h3>Platform</h3>
    <p>platform = platforming_framework.platform(color, x, y, w, h): creates a new platform sprite</p>
    <p>platform.go(x, y): moves the platform in the x & y direction by the specified amounts</p>
    <p>platform.refresh(): should be called every frame, handles rendering, movement, and gravity</p>
   </div>

<br>
<br>

   <div id = "goal_explanation">
    <h3>Goal</h3>
    <p>goal = platforming_framework.goal(color, x, y, w, h): creates a new platform sprite</p>
    <p>goal.refresh(): should be called every frame, handles rendering, movement, and gravity</p>
   </div>
