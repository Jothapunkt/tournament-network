var testResults = testManager.runTests()

document.getElementById("pass-header").innerHTML = "Passed Tests (" + testResults.passed.length + ")"
document.getElementById("fail-header").innerHTML = "Failed Tests (" + testResults.failed.length + ")"

var failTable = document.getElementById("fail-table")
var passTable = document.getElementById("pass-table")

failTable.innerHTML = ""
passTable.innerHTML = ""

testResults.passed.forEach(function(t) {
	var tr = document.createElement("tr")
	var td = document.createElement("td")
	var b = document.createElement("b")

	var testName = document.createTextNode(t.name)
	b.appendChild(testName)
	td.appendChild(b)

	var testDesc = document.createTextNode(" " + t.desc)
	td.appendChild(testDesc)

	tr.appendChild(td)
	passTable.appendChild(tr)
})

testResults.failed.forEach(function(t) {
	var tr = document.createElement("tr")
	var td = document.createElement("td")
	var b = document.createElement("b")

	var testName = document.createTextNode(t.name)
	b.appendChild(testName)
	td.appendChild(b)

	var testDesc = document.createTextNode(" " + t.desc)
	td.appendChild(testDesc)


	tr.appendChild(td)
	failTable.appendChild(tr)
})

testManager.testLogs.forEach(function(m) {
	var testlogTable = document.getElementById("testlog-table")
	var tr = document.createElement("tr")
	var td = document.createElement("td")

	td.appendChild(document.createTextNode(m))
	tr.appendChild(td)
	testlogTable.appendChild(tr)
})
