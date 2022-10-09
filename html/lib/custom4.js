var graph_4_c2 = echarts.init(document.getElementById('graph_4_c2'));	
window.onresize = function() {
    graph_4_c2.resize();
  };
var option = {
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
    {
      type: 'line',
      data: {{ graph_4_c2_data }}
    }
  ]
};
graph_4_c2.setOption(option);