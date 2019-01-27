var player

function startImport() {
	var str = document.getElementById("network-import").innerText
	
	player = remotePlayer()
	player.controller.importNetwork(str)
	
	tickHandler.beginTick()
}

var manualControl = false;

var terrainTable1 = terrainTableClass();

terrainTable1.rows.push("1000000001");
terrainTable1.rows.push("1000000001");
terrainTable1.rows.push("1100000011");
terrainTable1.rows.push("1110000111");
terrainTable1.rows.push("1110001111");
terrainTable1.rows.push("1110011111");
terrainTable1.rows.push("1110011111");
terrainTable1.rows.push("1111001111");
terrainTable1.rows.push("1000000001");
terrainTable1.rows.push("1111101111");
terrainTable1.rows.push("1000000001");
terrainTable1.rows.push("1000000001");
terrainTable1.rows.push("1000000001");
terrainTable1.rows.push("1111011111");
terrainTable1.rows.push("1000000001");
terrainTable1.rows.push("1000000001");
terrainTable1.rows.push("1000000001");
terrainTable1.rows.push("1000100001");
terrainTable1.rows.push("1111111111");

var terrainTable2 =  terrainTableClass();

terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000100001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1110000111");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1010000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1111110011");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1100000011");
terrainTable2.rows.push("1110000111");
terrainTable2.rows.push("1110001111");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1110011111");
terrainTable2.rows.push("1110011111");
terrainTable2.rows.push("1111001111");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1111101111");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1111011111");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000000001");
terrainTable2.rows.push("1000100001");
terrainTable2.rows.push("1111111111");

var terrainTable3 =  terrainTableClass();

terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1111011111");
terrainTable3.rows.push("1111011111");
terrainTable3.rows.push("1111011111");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1111111001");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1001111111");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1000000001");
terrainTable3.rows.push("1110000001");
terrainTable3.rows.push("1111111111");

var activeTerrainTable = terrainTable2;

var terrain = terrainClass(activeTerrainTable);

tickHandler.stopTick()
tickHandler.tick()