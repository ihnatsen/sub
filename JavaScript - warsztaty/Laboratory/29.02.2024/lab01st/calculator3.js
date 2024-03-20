let display;
		
window.onload = function () {
    setTimeout(function () {
        display = document.getElementById('display')
    }, 5); // Delay in miliseconds
};
		
function appendToDisplay(value) {
	display.value += value;
}

function clearDisplay() {
	display.value = '';
}

function calculate() {
	try {
		display.value = eval(display.value);
	} catch (error) {
		display.value = 'Error';
	}
}
		
function calculateSquareRoot() {
	const value = parseFloat(display.value);
	if (!isNaN(value)) {
		display.value = Math.sqrt(value);
	}
}

function clearEntry() {
	display.value = '';
}

function backspace() {
	display.value = display.value.slice(0, -1);
}