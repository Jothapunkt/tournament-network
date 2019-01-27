var keyDown = {};
var player;

window.onkeydown = function(e) { keyDown[e.key] = true;}
window.onkeyup = function(e) { keyDown[e.key] = false;}

var logFilters = {};
logFilters["DEBUG"] = true

function setLogFilter(name, log) {
	logFilters[name] = log
}

function log(msg, filter) {
	if (!filter) { filter = "DEBUG" }
	if (typeof logFilters[filter] != "undefined" && logFilters[filter] === true) { console.log(msg); }
}

function random(min, max) {
	return (Math.random() * (max - min)) + min;
}

function altClone(o) {
	return Object.assign({}, o);
}

function clone(o) {
	let target = {};
  for (let prop in o) {
    if (o.hasOwnProperty(prop)) {
      target[prop] = o[prop];
    }
  }
  return target;
}

function cloneArray(arr) {
	var newArray = [];
	arr.forEach(function(v) {
		newArray.push(v)
	})

	return newArray
}

function logPlayer(p) {
	log("Remote Player")
	log("Color - " + p.color)
	log("Original Color - " + p.originalColor)
}

//Picks from a set of weighted options, e.g. [100, 5, 20] gives a big chance of returning 0 (100/125), smallest for 1 (5/125)
function weightedArrayPick(args) {
	var sum = 0
	args.forEach(function(x) {
		sum += x
	})

	var r = Math.random() * sum
	
	var i = 0
	sum = args[0]

	while (sum < r) {
		i++
		sum += args[i]
	}
	return i
}
