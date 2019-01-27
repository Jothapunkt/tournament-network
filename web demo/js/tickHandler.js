/**
	tickHandler Class
	Keeps a list of objects and regularly calls their tick methods
*/

function tickHandlerClass() {
	console.log("New Tick Handler");

	var obj = {};

	obj.tickCount = 0;

	//List of objects to call per tick
	obj.subjects = [];

	//Calls tick methods of all subjects
	obj.tick = function() {
		//console.log("Tick No " + obj.tickCount);
		obj.tickCount++;

		//Removes drawn objects from previous tick
		ctx.setTransform(1,0,0,1,0,0);//reset the transform matrix as it is cumulative
		ctx.clearRect(0,0,canvasWidth,canvasHeight);

		obj.subjects.forEach(function(x) {
			x.tick();
		});
	};

	//Adds new subject
	obj.register = function(x) {
		obj.subjects.push(x);
	};

	//Deletes subject by value
	obj.unregister = function(x) {
		for (var i=0; i < obj.subjects.length; i++) {
			if (obj.subjects[i] == x) {
				obj.subjects.splice(i, 1);
				return;
			}
		}
	};


	//Milliseconds between ticks
	obj.tickInterval = 60;

	obj.beginTick = function() {
		window.clearInterval(obj.intervalID);
		obj.intervalID = window.setInterval(obj.tick, obj.tickInterval);
	}

	obj.stopTick = function() {
		window.clearInterval(obj.intervalID);
	}

	obj.beginTick();

	return obj;
}

var tickHandler = tickHandlerClass();
