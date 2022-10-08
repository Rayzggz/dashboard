var graph_3_c1 = echarts.init(document.getElementById('graph_3_c1'));	
window.onresize = function() {
    graph_3_c1.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_3_c1_names }}
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_3_c1_data }}
    }
  ]
};
graph_3_c1.setOption(option);



var graph_3_d2 = echarts.init(document.getElementById('graph_3_d2'));	
window.onresize = function() {
    graph_3_d2.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_3_d2_names }}
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_3_d2_data }}
    }
  ]
};
graph_3_d2.setOption(option);

var graph_3_b1 = echarts.init(document.getElementById('graph_3_b1'));	
window.onresize = function() {
    graph_3_b1.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_3_b1_names }}
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_3_b1_data }}
    }
  ]
};
graph_3_b1.setOption(option);


var graph_3_b2 = echarts.init(document.getElementById('graph_3_b2'));	
window.onresize = function() {
    graph_3_b2.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_3_b2_names }}
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_3_b2_data }}
    }
  ]
};
graph_3_b2.setOption(option);


var graph_3_c2 = echarts.init(document.getElementById('graph_3_c2'));	
window.onresize = function() {
    graph_3_c2.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_3_c2_names }}
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_3_c2_data }}
    }
  ]
};
graph_3_c2.setOption(option);
