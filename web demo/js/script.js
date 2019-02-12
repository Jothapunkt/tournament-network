var playerLeft
var playerRight

var ball = Ball()

var paused = false

var scoreLeft = 0
var scoreRight = 0
var lastScore = "left"

var scoreDraw = scoreDrawer()

function startGame() {
	if (typeof ball != "undefined") {
		ball.kill()
	}
	
	ball = Ball()
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

function debug() {
	
}

spawnPlayerLeft()
spawnPlayerRight()
