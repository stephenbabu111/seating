document.write("hello world")
setTimeout(navfunction,5000);
function navfunction()
{
//document.write("this next statement")
document.getElementById('navbar1').style.direction='ltr';
document.getElementById("head").innerHTML='this is modified';
}
