var ready = function () {
	// title
	document.title = document.querySelector("h1").textContent;
	
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
	_code.innerText = document.querySelector("script").innerText;
	
	document.body.appendChild(divCode);
	document.body.appendChild(_p);
}

/**
 * onload 事件，在页面中一切元素（DOM、图片、JS、CSS...）都加载完毕 才触发
 * 
 * DOMContentLoaded 事件，在形成完整DOM树之后触发
 * 
 */
document.addEventListener("DOMContentLoaded", function () {
	ready();
});

// 另一个 DOM ready 解决方案
setTimeout(function () {
	// ...
}, 0);
