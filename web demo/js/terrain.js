function terrainTableClass() {
	var obj = {}
	obj.rows = []
	return obj
}

function terrainClass(terrainTable) {
	var obj = {}
	
	tickHandler.register(obj)
	
	obj.blockWidth = 50
	obj.blockHeight = 50
	
	obj.yOffset = 0
	obj.firstPlayerTick = 0
	
	obj.boolTable = []
	/*
	Terrain Table is an Array of String Arrays, Example:
	[["1000000001"],
	["1000000001"],
	["1000000001"],
	["1000000001"],
	["1000000001"]]
	*/
	terrainTable.rows.forEach(function(row) {
		var boolRow = []
		for(var i = 0; i < row.length; i++) {
			if (row[i] == "1") { 
				boolRow.push(true)
			} else {
				boolRow.push(false)
			}
		}
		obj.boolTable.push(boolRow)
	})
	
	obj.collidesAt = function(x,y) {
		var xIndex = Math.floor(x/obj.blockWidth)
		var yIndex = Math.floor(y/obj.blockHeight)
		
		if (yIndex >= obj.boolTable.length) { return true }
		if (xIndex >= obj.boolTable[yIndex].length) { return true }
		
		return obj.boolTable[yIndex][xIndex]
	}
	
	obj.hasCollision = function(p) {
		if (obj.collidesAt(p.x,p.y)) { return true }
		if (obj.collidesAt(p.x + p.width,p.y)) { return true }
		if (obj.collidesAt(p.x,p.y + p.height)) { return true }
		if (obj.collidesAt(p.x + p.width,p.y + p.height)) { return true }
		
		return false
	}
	
	obj.draw = function() {
		obj.boolTable.forEach(function(row, rowY) {
			row.forEach(function(block, rowX) {
				if (block) {
					ctx.save();
					ctx.fillStyle = "#999999";
					ctx.beginPath();
					ctx.rect(rowX * obj.blockWidth, (rowY * obj.blockHeight) + obj.yOffset, obj.blockWidth, obj.blockHeight);
					ctx.fill();
					ctx.restore();
				}
			})
		})
	}
	
	obj.tick = function() {
		obj.yOffset = 50 + (tickHandler.tickCount - obj.firstPlayerTick) * -6
		obj.draw()
	}
	
	return obj
}