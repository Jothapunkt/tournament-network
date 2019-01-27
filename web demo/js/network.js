function networkClass() {
	var obj = {}
	obj.score = 0
	obj.inputs = []
	obj.layers = []
	obj.generation = 0
	
	obj.sigmoidFunction = function(x) {
    return (Math.exp(x)/(Math.exp(x) + 1))
  }
  
  obj.calcNetwork = function() {
	var lastResult = obj.inputs
	obj.layers.forEach(function(l) {
		currentResult = []
		l.forEach(function(node) {
			sum = 0
			node["weights"].forEach(function(w, i) {
				sum += w * lastResult[i]
			})
			sum -= node["bias"]
			currentResult.push(obj.sigmoidFunction(sum))
		})
		lastResult = currentResult
	})
	return lastResult
  }
  
  obj.importNetwork = function(str) {
	var jsonObj = JSON.parse(str)
	obj.score = jsonObj.score
	obj.inputs = jsonObj.inputs
	obj.layers = jsonObj.layers
	obj.generation = jsonObj.generation
  }
	
	return obj
}