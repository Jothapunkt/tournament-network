function RemotePlayer() {
	var obj = {}
	
	obj.width = 10
	obj.height = 75
	
	obj.x = 0
	obj.y = ((0.5 * window["canvasHeight"]) - (0.5 * obj.height))
	
	obj.ticksAlive = 0
	
	obj.upKey = "w"
	obj.downKey = "s"

	obj.color = "white";
	
	obj.lastMove = "neutral"
	
	obj.vspeed = 4
	
	obj.controller = networkClass()
	
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
	
	obj.makeInputLeft = function() { //Paddle y, ball position, ball velocity and opponent y
		var inputs = []
		inputs.push(obj.y/canvasHeight)
		inputs.push(ball.x/canvasWidth)
		inputs.push(ball.y/canvasHeight)
		inputs.push(ball.hspeed)
		inputs.push(ball.vspeed)
		
		if (playerLeft === obj) {
			inputs.push(playerRight.y/canvasHeight)
		} else {
			inputs.push(playerLeft.y/canvasHeight)
		}
		
		return inputs
	}
	
	obj.makeInputRight = function() { //Ball x and hspeed are inverted
		var inputs = []
		inputs.push(obj.y/canvasHeight)
		inputs.push((canvasWidth - ball.x)/canvasWidth)
		inputs.push(ball.y/canvasHeight)
		inputs.push(-ball.hspeed)
		inputs.push(ball.vspeed)
		
		if (playerLeft === obj) {
			inputs.push(playerRight.y/canvasHeight)
		} else {
			inputs.push(playerLeft.y/canvasHeight)
		}
		
		return inputs
	}
	
	obj.move = function() {
		obj.lastMove = "neutral"
		var vdiff = 0
		
		inputs = obj.makeInputLeft()
		if (playerRight == obj) {
			inputs = obj.makeInputRight()
		}
		
		obj.controller.inputs = inputs
		console.log(obj.controller.inputs)
		movements = obj.controller.calcNetwork()
		console.log(movements)
		
		if (movements[0] > movements[1] && movements[0] >= movements[2]) {
			vdiff = -obj.vspeed
			obj.lastMove = "up"
		}
		if (movements[2] > movements[1] && movements[2] > movements[0]) {
			vdiff = obj.vspeed
			obj.lastMove = "down"
		}
		
		obj.y += vdiff
		
		if (obj.y < 0) { obj.y = 0 }
		if (obj.y > window["canvasHeight"] - obj.height) { obj.y = window["canvasHeight"] - obj.height }
	}
	
	return obj
}
