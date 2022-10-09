document.getElementById('graph_2_d1').innerHTML = '<h1 class="mdui-center">{{ graph_2_d1_data }}<span class="unit-opacity">kBTU</span></h1>';

document.getElementById('graph_2_d2').innerHTML = '<h1 class="mdui-center"><span class="unit-opacity">$</span>{{ graph_2_d2_data }}</h1>';

document.getElementById('graph_2_d3').innerHTML = '<h1 class="mdui-center"><span class="unit-opacity">$</span>{{ graph_2_d3_data }}</h1>';


var graph_2_b1 = echarts.init(document.getElementById('graph_2_b1'));	
window.onresize = function() {
    graph_2_b1.resize();
  };
var option = {
  series: [
    {
      type: 'pie',
      data: {{ graph_2_b1_data }}
    }
  ]
};
graph_2_b1.setOption(option);


var graph_2_a1 = echarts.init(document.getElementById('graph_2_a1'));	
window.onresize = function() {
    graph_2_a1.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_2_a1_names }},
	name: 'days'
  },
  yAxis: {
	  name: 'kBTU'
  },
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_2_a1_data }}
    }
  ]
};
graph_2_a1.setOption(option);



var graph_2_b2 = echarts.init(document.getElementById('graph_2_b2'));	
window.onresize = function() {
    graph_2_b2.resize();
  };
var option = {
  series: [
    {
      type: 'pie',
      data: {{ graph_2_b2_data }}
    }
  ]
};
graph_2_b2.setOption(option);


