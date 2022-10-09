var inst = new mdui.Tab('#tab');
var i = 0;
setInterval('run()', 30000);
loadAnimate();

function loadAnimate() {
    const loadingDiv = document.getElementById("loading");
    loadingDiv.style.zIndex = 10;
    let tmp = 100;
    let timer = setInterval(function () {
        if (tmp <= 0) {
            clearInterval(timer);
            loadingDiv.style.filter = 'alpha(opacity=0)';
            loadingDiv.style.opacity = 0;
            loadingDiv.style.zIndex = 0;
        } else {
            tmp = tmp - 2;
            loadingDiv.style.filter = 'alpha(opacity=' + tmp + ')';
            loadingDiv.style.opacity = tmp / 100;
        }
    }, 5);
}

document.getElementById("tab").addEventListener("change", function (event) {
    loadAnimate();
});

function run() {
    loadAnimate();
    if (i < 4) {
        inst.next();
        i++
    } else {
        inst.show(0);
        i = 0;
    }
}