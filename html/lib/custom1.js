document.getElementById('graph_1_d1').innerHTML = '<h1 class="mdui-center">{{ graph_1_d1_data }} kBTU</h1>';

document.getElementById('graph_1_d2').innerHTML = '<h1 class="mdui-center">$ {{ graph_1_d2_data }}</h1>';

document.getElementById('graph_1_a2').innerHTML = '<h1 class="mdui-center">{{ graph_1_a2_data }} %</h1>';


var graph_1_b1 = echarts.init(document.getElementById('graph_1_b1'));	
window.onresize = function() {
    graph_1_b1.resize();
  };
var option = {
  series: [
    {
      type: 'pie',
      data: {{ graph_1_b1_data }}
    }
  ]
};
graph_1_b1.setOption(option);


var graph_1_a1 = echarts.init(document.getElementById('graph_1_a1'));	
window.onresize = function() {
    graph_1_a1.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_1_a1_names }},
	name: 'time(hour)'
  },
  yAxis: {
	  name: 'total energy comsumptiomption (kBTV)'
  },
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_1_a1_data }}
    }
  ]
};
graph_1_a1.setOption(option);



var graph_1_b2 = echarts.init(document.getElementById('graph_1_b2'));	
window.onresize = function() {
    graph_1_b2.resize();
  };
var option = {
  series: [
    {
      type: 'pie',
      data: {{ graph_1_b2_data }}
    }
  ]
};
graph_1_b2.setOption(option);


