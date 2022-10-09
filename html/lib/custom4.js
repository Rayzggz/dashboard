var graph_4_c2 = echarts.init(document.getElementById('graph_4_c2'));	
window.onresize = function() {
    graph_4_c2.resize();
  };
var option = {
	legend: {
    // Try 'horizontal'
    orient: 'vertical',
    right: 10,
    top: 'center'
  },
  xAxis: {
	type: 'category',
	name: 'month',
    data: {{ graph_4_c2_names }}
  },
  yAxis: {
	  type: 'value',
	  name: 'temperature(Farenheit)'
  },
  series: [
      {{ <h1> }}
  ]
};
graph_4_c2.setOption(option);