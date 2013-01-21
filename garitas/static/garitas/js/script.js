
function selectCity() {
    var shadow_screen = document.getElementById("shadow_screen");
    if(shadow_screen === null) {
        var layer = document.createElement('div');
        layer.id = "shadow_screen";
        layer.style.width = '100%';
        layer.style.height ='100%';
        layer.style.position = 'fixed';
        layer.style.top = 0;
        layer.style.left = 0;
        layer.style.padding = 0;
        layer.style.margin = 0;
        layer.style.zIndex = 2;
        layer.innerHTML = "<img src='/static/garitas/img/background-alpha.png' width='100%' height='100%'>";
        document.body.appendChild(layer);
	} else {
		document.getElementById("shadow_screen").style.visibility = "visible";
	}
    $('#box_popup').show("slow");
}

function closeSelectCity()
{
	$('#box_popup').hide("slow");
	document.getElementById("shadow_screen").style.visibility = "hidden";
}
