document.getElementById('graph_1_d1').innerHTML = '<h1 class="mdui-center">{{ graph_1_d1_data }}<span class="unit-opacity">kBTU</span></h1>';

document.getElementById('graph_1_d2').innerHTML = '<h1 class="mdui-center"><span class="unit-opacity">$</span>{{ graph_1_d2_data }}</h1>';

document.getElementById('graph_1_a2').innerHTML = '<h1 class="mdui-center">{{ graph_1_a2_data }}<span class="unit-opacity">%</span></h1>';


var graph_1_b1 = echarts.init(document.getElementById('graph_1_b1'));
window.onresize = function() {
    graph_1_b1.resize();
  };
var option = {
  tooltip: {
      trigger: 'item',
      formatter: '{d}%'
    },
  series: [
    {
      type: 'pie',
      data: {{ graph_1_b1_data }},
    }
  ]
};
graph_1_b1.setOption(option);


var graph_1_a1 = echarts.init(document.getElementById('graph_1_a1'));
window.onresize = function() {
    graph_1_a1.resize();
  };
var option = {
    tooltip: {
      trigger: 'item',
      formatter: '{c}'
    },
  xAxis: {
    data: {{ graph_1_a1_names }},
	name: 'time(hour)',
  },
  yAxis: {
	  name: 'total energy comsumptiomption (kBTU)'
  },
  series: [
    {
      name: 'graph_1_a1',
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
    tooltip: {
      trigger: 'item',
      formatter: '{d}%'
    },
    series: [
        {
          type: 'pie',
          dataLabels: {
                style: {
                    fontSize: 1
                }
            },
            data: {{ graph_1_b2_data }}
        }
    ]
};
graph_1_b2.setOption(option);


