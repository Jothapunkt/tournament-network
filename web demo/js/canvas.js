var canvas = document.getElementsByClassName("screen")[0];
var ctx = canvas.getContext("2d");

var canvasWidth = canvas.clientWidth;
var canvasHeight = canvas.clientHeight;

log("Canvas Width: " + canvasWidth);
log("Canvas Height: " + canvasHeight);

function clearCanvas() {
	ctx.clearRect(0,0,canvasWidth,canvasHeight);
}
