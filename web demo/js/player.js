function Player() {
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
		
		if (window["keyDown"][obj.upKey]) {
			obj.y -= obj.vspeed
			obj.lastMove = "up"
		} else if (window["keyDown"][obj.downKey]) {
			obj.y += obj.vspeed
			obj.lastMove = "down"
		}
		
		if (obj.y < 0) { obj.y = 0 }
		if (obj.y > window["canvasHeight"] - obj.height) { obj.y = window["canvasHeight"] - obj.height }
		
	}
	
	return obj
}
