

var elem=document.getElementById("popup");
var x=0;

/* Function to make the box appear */
function moreVisible()
{
    if(x==1)clearInterval(t);
    x+=0.05;
    elem.style.opacity=x;
    elem.style.filter="alpha(opacity="+(x*100)+")";
}

/* SetInterval determines how fast the box appears */
/* setTimeout determines when the box must start appearing */
setTimeout("setInterval(moreVisible,220)", 5000);
