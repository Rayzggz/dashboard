document.getElementById('graph_1_d1').innerHTML = '<h2>{{ graph_1_d1_data }} kBTU</h2>';

document.getElementById('graph_1_d2').innerHTML = '<h2>{{ graph_1_d2_data }} $</h2>';



var graph_1_a2 = echarts.init(document.getElementById('graph_1_a2'));	
window.onresize = function() {
    graph_1_a2.resize();
  };
var option = {
  xAxis: {
    data: {{ graph_1_a2_names }}
  },
  yAxis: {
	  name: 'dollar($)'
  },
  series: [
    {
      name: '销量',
      type: 'bar',
      data: {{ graph_1_a2_data }}
	  label: {
        normal: {
          position: 'top',
          distance: 10,
          show: true,
          formatter: ['{{ graph_1_a2_growthrate }}'].join('\n'),
          backgroundColor: '#eee',
          borderColor: '#555',
          borderWidth: 2,
          borderRadius: 5,
          padding: 10,
          fontSize: 18,
          shadowBlur: 3,
          shadowColor: '#888',
          shadowOffsetX: 0,
          shadowOffsetY: 3,
          textBorderColor: '#000',
          textBorderWidth: 3,
          color: '#992233'
        }
      }
    }
  ]
};
graph_1_a2.setOption(option);


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


