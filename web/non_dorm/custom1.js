document.getElementById('graph_1_d1').innerHTML = '<h1 class="mdui-center">154,451.4<span class="unit-opacity">kBTU</span></h1>';

document.getElementById('graph_1_d2').innerHTML = '<h1 class="mdui-center"><span class="unit-opacity">$</span>23,130.07</h1>';

document.getElementById('graph_1_a2').innerHTML = '<h1 class="mdui-center"><span class="mdui-text-color-red-300"><i class="mdui-icon material-icons">arrow_upward</i>5.08</span><span class="unit-opacity">%</span></h1>';


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
        stillShowZeroSum: false,
        label:{
            fontSize:9,
            position: 'inner'
        },
      data: [{value: 67898.40000099999, name:'Steam'},{value: 30270.686762100002, name:'Electricity'},{value: 56282.309746, name:'Chilled Water'},{value: 0.0, name:'Natural Gas'}],
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
      data: [6009.504508, 5957.123151, 5620.003197, 5482.717442, 5428.528946, 5859.26975, 6313.796257, 6046.661656, 5975.956462, 5669.168697, 5694.80796, 5543.275975, 6730.285214, 7113.924237, 7302.525932, 7590.066293, 7189.588561, 6922.371826, 6939.804191, 6938.433065, 6999.48092, 6959.522893, 7039.601288, 7124.978087]
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
          stillShowZeroSum: false,
          label:{
            fontSize:9,
            position: 'inner'
          },
          data: [{value: 1536.4827883643375, name:'Steam'},{value: 957.2705456127169, name:'Electricity'},{value: 18940.440846401234, name:'Chilled Water'},{value: -0.08912800000000001, name:'Hot Water'},{value: 1695.9629698376996, name:'Natural Gas'}]
        }
    ]
};
graph_1_b2.setOption(option);


