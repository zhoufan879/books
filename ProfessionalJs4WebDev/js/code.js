var ready = function () {
	var divCode = document.createElement("div");
	var _code = document.createElement("code");
	divCode.style.margin = '10px';
	divCode.style.borderWidth = '1px';
	divCode.style.borderColor = '#ccc';
	divCode.style.borderStyle = 'solid';
	divCode.appendChild(_code);
	
	var _p = document.createElement("p");
	_p.style.color = "#eb7350";
	_p.textContent = '* 请查看控制台 （win - F12 / mac - opt+com+i）';
	_code.innerText = document.getElementById("js").innerText;
	
	document.body.appendChild(divCode);
	document.body.appendChild(_p);
}

document.addEventListener("DOMContentLoaded", function () {
	ready();
});
