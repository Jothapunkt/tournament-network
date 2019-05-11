var playerLeft
var playerRight

var scoreLeft = 0
var scoreRight = 0

var ball = Ball()
var ball2 = SecondBall()

var paused = false

var lastScore = "left"

var scoreDraw = scoreDrawer()

function startGame() {
	if (typeof ball != "undefined") {
		ball.kill()
	}
	
	if (typeof ball2 != "undefined") {
		ball2.kill()
	}
	
	ball = Ball()
	ball2 = SecondBall()
	
	ball2.color = "SteelBlue"
	
	scoreLeft = 0
	scoreRight = 0
	
	playerLeft.resetPlayer()
	playerRight.resetPlayer()
	
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

function startImportLeft() {
	if (typeof playerLeft != "undefined") {
		playerLeft.kill()
	}
	
	var str = document.getElementById("network-import-left").innerText
	
	playerLeft = RemotePlayer()
	playerLeft.controller.importNetwork(str)
	playerLeft.alignLeft()
}

function spawnPlayerLeft() {
	if (typeof playerLeft != "undefined") {
		playerLeft.kill()
	}
	
	playerLeft = Player()
	playerLeft.setKeys("w","s")
	playerLeft.alignLeft()
}

function spawnProgrammedPlayerLeft() {
	if (typeof playerLeft != "undefined") {
		playerLeft.kill()
	}
	
	playerLeft = ProgrammedPlayer()
	playerLeft.alignLeft()
}

function startImportRight() {
	if (typeof playerRight != "undefined") {
		playerRight.kill()
	}
	
	var str = document.getElementById("network-import-right").innerText
	
	playerRight = RemotePlayer()
	playerRight.controller.importNetwork(str)
	playerRight.alignRight()
}

function spawnPlayerRight() {
	if (typeof playerRight != "undefined") {
		playerRight.kill()
	}
	
	playerRight = Player()
	playerRight.setKeys("o","l")
	playerRight.alignRight()
}

function spawnProgrammedPlayerRight() {
	if (typeof playerRight != "undefined") {
		playerRight.kill()
	}
	
	playerRight = ProgrammedPlayer()
	playerRight.alignRight()
}

spawnPlayerLeft()
spawnProgrammedPlayerRight()
