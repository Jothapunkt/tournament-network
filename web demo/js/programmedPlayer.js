function ProgrammedPlayer() {
	var obj = {}
	
	obj.width = 10
	obj.height = 75
	
	obj.neutralY = ((0.5 * window["canvasHeight"]) - (0.5 * obj.height))
	
	obj.x = 0
	obj.y = obj.neutralY
	
	obj.ticksAlive = 0
	
	obj.upKey = "w"
	obj.downKey = "s"

	obj.color = "white";
	
	obj.lastMove = "neutral"
	
	obj.vspeed = 4
	
	tickHandler.register(obj)
	
	obj.kill = function() {
		tickHandler.unregister(obj)
		obj.color = "crimson"
	}
	
	obj.tick = function() {
		obj.ticksAlive++
		obj.move()
		obj.draw()
	}
	
	obj.alignLeft = function() {
		obj.x = 0
	}
	
	obj.alignRight = function() {
		obj.x = window["canvasWidth"] - obj.width
	}
	
	obj.setKeys = function(up,down) {
		obj.upKey = up
		obj.downKey = down
	}
	
	obj.draw = function() {
		ctx.save();
		ctx.fillStyle = obj.color;
		ctx.beginPath();
		ctx.rect(obj.x,obj.y,obj.width,obj.height);
		ctx.fill();
		ctx.restore();
	}
	
	obj.move = function() {
		obj.lastMove = "neutral"
		
		sign = 1
		
		if (playerLeft === obj) {
			sign = -1
		}
		
		if (Math.sign(ball.hspeed) == sign) { //Ball 1 needs to be caught
			if ((Math.sign(ball2.hspeed) == sign)) { //Both balls need to be caught
				
				delta1 = 0
				delta2 = 0
				
				currentX1 = ball.x
				currentX2 = ball2.x
				
				while(currentX1 > 0 && currentX1 < window["canvasWidth"]) {
					currentX1 += ball.hspeed
					delta1++
				}
				
				while(currentX2 > 0 && currentX2 < window["canvasWidth"]) {
					currentX2 += ball2.hspeed
					delta2++
				}
				
				if (delta1 < delta2) { //Prioritise the ball that will hit first
					if (obj.y + 70 < ball.predictY) {
						obj.y += obj.vspeed
					} else if (obj.y - 5 > ball.predictY) {
						obj.y -= obj.vspeed
					}
				} else {
					if (obj.y + 70 < ball2.predictY) {
						obj.y += obj.vspeed
					} else if (obj.y - 5 > ball2.predictY) {
						obj.y -= obj.vspeed
					}
				}
				
			} else { //Catch ball1 because ball2 moves to the other direction
				if (obj.y + 70 < ball.predictY) {
					obj.y += obj.vspeed
				} else if (obj.y - 5 > ball.predictY) {
					obj.y -= obj.vspeed
				}
			}
		} else { //Ball 1 doesn't need to be caught
			if ((Math.sign(ball2.hspeed) == sign)) { //Catch ball2 because ball1 moves to the other direction
				if (obj.y + 70 < ball2.predictY) {
					obj.y += obj.vspeed
				} else if (obj.y - 5 > ball2.predictY) {
					obj.y -= obj.vspeed
				}
			} else { //Neither ball needs to be caught, so move back to center position
				if (obj.y < obj.neutralY) {
					obj.y += obj.vspeed
				} else if (obj.y > obj.neutralY) {
					obj.y -= obj.vspeed
				}
			}
		}	
		
		if (obj.y < 0) { obj.y = 0 }
		if (obj.y > window["canvasHeight"] - obj.height) { obj.y = window["canvasHeight"] - obj.height }
		
	}
	
	return obj
}
