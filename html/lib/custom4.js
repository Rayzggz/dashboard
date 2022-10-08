var graph_4_c2 = echarts.init(document.getElementById('graph_4_c2'));	
window.onresize = function() {
    graph_4_c2.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_4_c2_names }}
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_4_c2_data }}
    }
  ]
};
graph_4_c2.setOption(option);