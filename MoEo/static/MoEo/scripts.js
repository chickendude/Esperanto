function novaTeksto() {
	var textList = document.getElementById("tekstoj").getElementsByTagName("textarea");
	var num = textList.length+1;
	// find container and create text area
	var container = document.getElementById('tekstoj');
	var div = document.createElement('div');
	var textarea = document.createElement('textarea');
	var p = document.createElement('p');
	// set up p and text area
	p.innerHTML = 'Teksto ' + num + " <a href=\"javascript:forigi( " + num + " )\">forigi</a>";
	textarea.setAttribute('rows', '6');
	textarea.setAttribute('cols', '60');
	textarea.setAttribute('name', 'teksto'+num);
	// insert into div
	div.setAttribute('id', 'teksto'+num);
	div.appendChild(p);
	div.appendChild(textarea);
	// insert div into HTML
	container.appendChild(div);
}

function forigi(num) {
	var textList = document.getElementById("tekstoj");
	var teksto = document.getElementById("teksto"+num);
	textList.removeChild(teksto);
}
