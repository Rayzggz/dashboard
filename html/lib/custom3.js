var graph_3_c1 = echarts.init(document.getElementById('graph_3_c1'));	
window.onresize = function() {
    graph_3_c1.resize();
  };
var option = {
  tooltip: {
      trigger: 'item',
      formatter: '{c}'
    },
  xAxis: {
	type: 'category',
	name: 'Year',
    data: {{ graph_3_c1_names }}
  },
  yAxis: {
	  name: 'kBTU',
	  type: 'value'
  },
  series: [
    {
      type: 'line',
      data: {{ graph_3_c1_data }}
    }
  ]
};
graph_3_c1.setOption(option);

	
document.getElementById('graph_3_d2').innerHTML = '<h1 class="mdui-center"><span class="unit-opacity">$</span>{{ graph_3_d2_data }}</h1>';

var graph_3_b1 = echarts.init(document.getElementById('graph_3_b1'));	
window.onresize = function() {
    graph_3_b1.resize();
  };
var option = {
  tooltip: {
      trigger: 'item',
      formatter: '{d}%'
    },
  series: [
    {
      type: 'pie',
        label:{
            fontSize:9,
            position: 'inner'
        },
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
  tooltip: {
      trigger: 'item',
      formatter: '{d}%'
    },
  series: [
    {
      type: 'pie',
        label:{
            fontSize:9,
            position: 'inner'
        },
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
  tooltip: {
      trigger: 'item',
      formatter: '{c}'
    },
  xAxis: {
	type: 'category',
    data: {{ graph_3_c2_names }}
  },
  yAxis: {
	  type: 'value',
	  name: 'total energy usage for a month(kBTU)'
  },
  series: [
    {
      type: 'line',
      data: {{ graph_3_c2_data }}
    }
  ]
};
graph_3_c2.setOption(option);
