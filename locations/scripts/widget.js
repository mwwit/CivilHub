!function(){"use strict";function n(n,t){var e=new XMLHttpRequest;e.open("GET",n,!0),e.onload=function(){4===e.readyState&&200===e.status&&t.call(null,e.responseText)},e.send(null)}var t="{div_id}",e="{url}",d="{width}px";window.addEventListener("load",function(){var i=document.getElementById(t);n(e,function(n){i.innerHTML=n}),i.style.width=d})}();
