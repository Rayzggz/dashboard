var inst = new mdui.Tab('#tab');
var i = 0;
setInterval('run()', 3000);
function run(){
	if(i < 4){
		inst.next();
		i++
	} else {
		inst.show(0);
		i = 0;
	}
}