var graph_1_d1 = echarts.init(document.getElementById('graph_1_d1'));	
window.onresize = function() {
    graph_1_d1.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_1_d1_names }}
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_1_d1_data }}
    }
  ]
};
graph_1_d1.setOption(option);



var graph_1_d2 = echarts.init(document.getElementById('graph_1_d2'));	
window.onresize = function() {
    graph_1_d2.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_1_d2_names }}
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_1_d2_data }}
    }
  ]
};
graph_1_d2.setOption(option);

var graph_1_d3 = echarts.init(document.getElementById('graph_1_d3'));	
window.onresize = function() {
    graph_1_d3.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_1_d3_names }}
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_1_d3_data }}
    }
  ]
};
graph_1_d3.setOption(option);


var graph_1_b1 = echarts.init(document.getElementById('graph_1_b1'));	
window.onresize = function() {
    graph_1_b1.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_1_b1_names }}
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
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
    data: {{ graph_1_a1_names }}
  },
  yAxis: {},
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
  xAxis: {
    data: {{ graph_1_b2_names }}
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_1_b2_data }}
    }
  ]
};
graph_1_b2.setOption(option);


