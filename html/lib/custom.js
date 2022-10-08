var myChart = echarts.init(document.getElementById('graph1'));	
window.onresize = function() {
    myChart.resize();
  };
var option = {
  xAxis: {
    data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: [5, 20, 36, 10, 10, 20]
    }
  ]
};
myChart.setOption(option);