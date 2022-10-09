var graph_4_c2 = echarts.init(document.getElementById('graph_4_c2'));	
window.onresize = function() {
    graph_4_c2.resize();
  };
var option = {
    tooltip: {
      trigger: 'item',
      formatter: '{c}'
    },
	legend: {
    // Try 'horizontal'
    orient: 'vertical',
    right: 10,
    top: 'center'
  },
  xAxis: {
	type: 'category',
	name: 'month',
    data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  },
  yAxis: {
	  type: 'value',
	  name: 'temperature(Farenheit)'
  },
  series: [
      {name: '2021',data:[23.0, 11.5, 29.0, 30.5, 36.5, 54.5, 66.0, 67.0, 53.5, 50.0, 30.0, 24.0, 43.0], type: 'line'},{name: '2020',data:[17.0, 17.3, 31.5, 37.0, 39.0, 45.525, 73.0, 58.0, 51.0, 45.0, 32.0, 14.0, 13.0], type: 'line'},{name: '2019',data:[5.0, 2.0, 13.0, 32.0, 52.0, 60.0, 68.0, 65.3, 54.525, 38.725, 17.0, 20.0, 36.0], type: 'line'},{name: '2018',data:[4.0, 18.0, 29.0, 33.0, 61.0, 62.0, 69.0, 67.0, 59.0, 41.0, 29.0, 23.0, 35.0], type: 'line'}
  ]
};
graph_4_c2.setOption(option);