function Ball() {
	var obj = {}
	
	obj.radius = 5
	obj.acceleration = 1.001
	obj.minSpeed = 4
	obj.speedCapUpper = 100
	obj.speedCapLower = 1
	
	obj.color = "white";
	
	tickHandler.register(obj)
	
	obj.kill = function() {
		tickHandler.unregister(obj)
		obj.color = "crimson"
	}
	
	obj.tick = function() {
		obj.ticksSinceReset++
		obj.move()
		obj.draw()
	}
	
	obj.resetBall = function() {
		obj.ticksSinceReset = 0
		
		obj.x = 0.5 * window["canvasWidth"]
		obj.y = 0.5 * window["canvasHeight"]
		
		obj.vspeed = 0.3 * obj.minSpeed
		obj.hspeed = obj.minSpeed
		
		if (lastScore == "right") { obj.hspeed = -obj.hspeed }
		
	}
	
	obj.resetBall()
	
	obj.draw = function() {
		ctx.save();
		ctx.fillStyle = obj.color;
		ctx.beginPath();
		ctx.arc(obj.x,obj.y,obj.radius,0,2 * Math.PI);
		ctx.fill();
		ctx.restore();
	}
	
	obj.move = function() {
		targetX = obj.x + obj.hspeed
		targetY = obj.y + obj.vspeed
		
		obj.hspeed *= obj.acceleration
		obj.vspeed *= obj.acceleration
		
		if (targetY < 0) {
			obj.y = 0
			obj.vspeed = -obj.vspeed
		} else if(targetY > window["canvasHeight"]) {
			obj.y = window["canvasHeight"]
			obj.vspeed = -obj.vspeed
		} else {
			obj.y = targetY
		}
		
		if (targetX < playerLeft.width) {
			if (targetY + obj.radius >= playerLeft.y && targetY - obj.radius <= playerLeft.y + playerLeft.height) { //Did the ball hit the left paddle?
				obj.x = playerLeft.width
				obj.hspeed = -obj.hspeed
				
				if (playerLeft.lastMove == "up") {
					obj.vspeed = obj.vspeed * (obj.vspeed < 0 ? 0.5 : 1.5)
				} else if (playerLeft.lastMove == "down") {
					obj.vspeed = obj.vspeed * (obj.vspeed > 0 ? 0.5 : 1.5)
				}
				
			} else if (targetX < 0) {
				scoreRight++
				lastScore = "right"
				obj.resetBall()
			} else {
				obj.x = targetX
			}
		} else if (targetX > window["canvasWidth"] - playerRight.width) {
			if (targetY + obj.radius >= playerRight.y && targetY - obj.radius <= playerRight.y + playerRight.height) {//Did the ball hit the right paddle?
				obj.x = window["canvasWidth"] - playerRight.width
				obj.hspeed = -obj.hspeed
				
				if (playerRight.lastMove == "up") {
					obj.vspeed = obj.vspeed * (obj.vspeed < 0 ? 0.5 : 1.5)
				} else if (playerRight.lastMove == "down") {
					obj.vspeed = obj.vspeed * (obj.vspeed > 0 ? 0.5 : 1.5)
				}
			} else if (targetX > window["canvasWidth"]) {
				scoreLeft++
				lastScore = "left"
				obj.resetBall()
			} else {
				obj.x = targetX
			}
		} else {
			obj.x = targetX
		}
		
		if (obj.vspeed > obj.speedCapUpper) { obj.vspeed = obj.speedCapUpper }
		if (obj.vspeed < -obj.speedCapUpper) { obj.vspeed = -obj.speedCapUpper }
		
		if (obj.hspeed > obj.speedCapUpper) { obj.hspeed = obj.speedCapUpper }
		if (obj.hspeed < -obj.speedCapUpper) { obj.hspeed = -obj.speedCapUpper }
		
		if (obj.vspeed > -obj.speedCapLower && obj.vspeed <= 0) { obj.vspeed = -obj.speedCapLower }
		if (obj.vspeed < obj.speedCapLower && obj.vspeed > 0) { obj.vspeed = obj.speedCapLower }
	}
	
	return obj
}
