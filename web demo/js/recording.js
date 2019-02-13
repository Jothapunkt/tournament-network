var paused = false

var scoreLeft = 0
var scoreRight = 0

var scoreDraw = scoreDrawer()

var recorder

function Playback(str) {
	var obj = {}
	
	tickHandler.register(obj)
	obj.data = JSON.parse(str)
	
	obj.playerLeftX = 0
	obj.playerLeftY = 0
	obj.playerRightX = 0
	obj.playerRightY = 0
	obj.ballX = 0
	obj.ballY = 0
	
	obj.color = "white";
	
	obj.playerHeight = 75
	obj.playerWidth = 10
	
	obj.ballRadius = 5
	
	obj.index = -1
	
	obj.tick = function() {
		obj.index++
		
		if (obj.index < 0) {
			obj.index = 0
		}
		
		if (obj.index >= obj.data.length) {
			obj.index = obj.data.length - 1
		}
		
		obj.parseTickData(obj.data[obj.index])
		scoreDraw.tick()
		
		//Draw left player
		ctx.save();
		ctx.fillStyle = obj.color;
		ctx.beginPath();
		ctx.rect(obj.playerLeftX,obj.playerLeftY,obj.playerWidth,obj.playerHeight);
		ctx.fill();
		ctx.restore();
		
		//Draw right player
		ctx.save();
		ctx.fillStyle = obj.color;
		ctx.beginPath();
		ctx.rect(obj.playerRightX,obj.playerRightY,obj.playerWidth,obj.playerHeight);
		ctx.fill();
		ctx.restore();
		
		//Draw ball
		ctx.save();
		ctx.fillStyle = obj.color;
		ctx.beginPath();
		ctx.arc(obj.ballX,obj.ballY,obj.ballRadius,0,2 * Math.PI);
		ctx.fill();
		ctx.restore();
	}
	
	obj.previousTick = function() {
		obj.index -= 2
		obj.tick()
	}
	
	
	obj.parseTickData = function(data) {
		obj.playerLeftX = data[0]
		obj.playerLeftY = data[1]
		
		obj.ballX = data[2]
		obj.ballY = data[3]
		
		obj.playerRightX = data[4]
		obj.playerRightY = data[5]
		
		scoreLeft = data[6]
		scoreRight = data[7]
	}
	
	obj.kill = function() {
		tickHandler.unregister(obj)
	}
	
	return obj
}

function importRecording() {
	if (typeof recorder != "undefined") {
		recorder.kill()
	}
	recorder = Playback(document.getElementById("recording-data").innerText)
	if (paused) {
		togglePause()
	}
}

function togglePause() {
	paused = !paused
	if (paused) {
		tickHandler.stopTick()
		document.getElementById("pause-button").innerText = "Resume"
	} else {
		tickHandler.stopTick()
		tickHandler.beginTick()
		document.getElementById("pause-button").innerText = "Pause"
	}
}


