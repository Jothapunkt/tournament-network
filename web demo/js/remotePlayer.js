function remotePlayer() {
	var obj = {}
	obj.startX = 150
	obj.x = obj.startX
	obj.y = 0
	
	obj.ticksAlive = 0
	
	obj.width = 30
	obj.height = 30
	
	obj.rcol = Math.round(random(20,230));
	obj.gcol = Math.round(random(20,230));
	obj.bcol = Math.round(random(20,230));

	obj.color = "rgb(" + obj.rcol + "," + obj.gcol + "," + obj.bcol + ")";
	
	obj.hspeed = 6
	obj.vspeed = 6
	
	tickHandler.register(obj)
	
	obj.controller = networkClass()
	
	obj.kill = function() {
		tickHandler.unregister(obj)
		tickHandler.stopTick()
		
		obj.color = "crimson"
		console.log("Dead at (" + obj.x + "/" + obj.y + "); Tick #" + obj.ticksAlive)
	}
	
	obj.tick = function() {
		if (obj.ticksAlive == 0) {
			terrain.firstPlayerTick = tickHandler.tickCount
		}
		obj.ticksAlive++
		obj.move()
		if(terrain.hasCollision(obj)) {
			obj.kill()
		}
		obj.draw()
	}
	
	obj.draw = function() {
		ctx.save();
		ctx.fillStyle = obj.color;
		ctx.beginPath();
		ctx.rect(obj.x,50,obj.width,obj.height);
		ctx.fill();
		ctx.restore();
	}
	
	obj.makeInput = function() {
		var newInput = []
		var minY = Math.floor(obj.y/terrain.blockHeight);
		for (var i = 0; i < 5; i++) {
			if (minY + i >= terrain.boolTable.length) {
				newInput.push(1,1,1,1,1,1,1,1,1,1)
			} else {
				terrain.boolTable[minY+i].forEach(function(isBlock) {
					if(isBlock){
						newInput.push(1)
					} else {
						newInput.push(0)
					}
				})
			}
		}
		
		newInput.push((obj.y%50)/50)
		newInput.push(obj.x/(10*terrain.blockWidth))
		
		obj.controller.inputs = newInput
	}
	
	obj.move = function() {
		obj.makeInput()
		movements = obj.controller.calcNetwork()
		console.log(movements)
		
		hdiff = 0
		if (movements[0] > movements[1] && movements[0] >= movements[2]) { hdiff = -obj.hspeed }
		if (movements[2] > movements[1] && movements[2] >= movements[0]) { hdiff = obj.hspeed }
			
		obj.x += hdiff
		obj.y += obj.vspeed
	}
	
	return obj
}
