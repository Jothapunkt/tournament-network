function scoreDrawer() {
	var obj = {}
	tickHandler.register(obj)
	
	obj.tick = function() {
		ctx.save();
		ctx.fillStyle = "#dddddd";
		ctx.beginPath();
		ctx.font = "30px Helvetica";
		ctx.textAlign = "center"; 
		
		ctx.fillText(scoreLeft, 0.3 * canvasWidth, 0.5 * canvasHeight);
		ctx.fillText(scoreRight, 0.7 * canvasWidth, 0.5 * canvasHeight);
		
		ctx.restore();
	}
	
	return obj
}