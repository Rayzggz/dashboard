document.getElementById('graph_1_d1').innerHTML = '<h1 class="mdui-center">78,315.07<span class="unit-opacity">kBTU</span></h1>';

document.getElementById('graph_1_d2').innerHTML = '<h1 class="mdui-center"><span class="unit-opacity">$</span>9,639.94</h1>';

document.getElementById('graph_1_a2').innerHTML = '<h1 class="mdui-center"><span class="mdui-text-color-red-300"><i class="mdui-icon material-icons">arrow_upward</i>6.72</span><span class="unit-opacity">%</span></h1>';


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
        label:{
            fontSize:9,
            position: 'inner'
        },
      data: [{value: 14633.196933200003, name:'Steam'},{value: 19183.481092299997, name:'Electricity'},{value: 13892.874210294001, name:'Chilled Water'},{value: 30605.515624999993, name:'Hot Water'}],
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
    data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
	name: 'time(hour)',
  },
  yAxis: {
	  name: 'total energy comsumptiomption (kBTU)'
  },
  series: [
    {
      name: 'graph_1_a1',
      type: 'bar',
      data: [4212.716575, 3536.782234, 2676.031847, 2304.48116, 1882.4017, 1663.47745, 1671.938667, 3259.671872, 1597.258871, 1545.38757, 1610.882471, 2276.251525, 4726.125226, 5353.532805, 3489.088096, 3826.361899, 4101.601044, 4156.892938, 4065.205921, 4067.711521, 4135.428857, 4091.578513, 4076.445136, 3987.813965]
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
          label:{
            fontSize:9,
            position: 'inner'
          },
          data: [{value: 1147.1392844221107, name:'Steam'},{value: 462.755553661278, name:'Electricity'},{value: 6455.733435541663, name:'Chilled Water'},{value: 1238.244092615084, name:'Hot Water'},{value: 336.06572906642884, name:'Natural Gas'}]
        }
    ]
};
graph_1_b2.setOption(option);


