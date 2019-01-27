function Player() {
	var obj = {}
	obj.x = 0
	obj.y = 0
	
	obj.ticksAlive = 0
	
	obj.width = 30
	obj.height = 150
	
	obj.upKey = "w"
	obj.downKey = "s"

	obj.color = "white";
	
	obj.vspeed = 6
	
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
	
	obj.draw = function() {
		ctx.save();
		ctx.fillStyle = obj.color;
		ctx.beginPath();
		ctx.rect(obj.x,obj.y,obj.width,obj.height);
		ctx.fill();
		ctx.restore();
	}
	
	obj.move = function() {
		if (window["keyDown"][obj.upKey]) { obj.y -= obj.vspeed }
		if (window["keyDown"][obj.downKey]) { obj.y += obj.vspeed }
	}
	
	return obj
}
