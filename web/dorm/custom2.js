document.getElementById('graph_2_d1').innerHTML = '<h1 class="mdui-center">2,797,172.45<span class="unit-opacity">kBTU</span></h1>';

document.getElementById('graph_2_d2').innerHTML = '<h1 class="mdui-center"><span class="unit-opacity">$</span>323,037.27</h1>';

document.getElementById('graph_2_d3').innerHTML = '<h1 class="mdui-center"><span class="unit-opacity">$</span>11,831.35</h1>';


var graph_2_b1 = echarts.init(document.getElementById('graph_2_b1'));	
window.onresize = function() {
    graph_2_b1.resize();
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
      data: [{value: 374129.53147990006, name:'Steam'},{value: 623700.1244877003, name:'Electricity'},{value: 607595.9915635387, name:'Chilled Water'},{value: 1191746.7999769466, name:'Hot Water'}]
    }
  ]
};
graph_2_b1.setOption(option);


var graph_2_a1 = echarts.init(document.getElementById('graph_2_a1'));	
window.onresize = function() {
    graph_2_a1.resize();
  };
var option = {
  tooltip: {
      trigger: 'item',
      formatter: '{c}'
    },
  xAxis: {
    data: [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6],
	name: 'days'
  },
  yAxis: {
	  name: 'kBTU'
  },
  series: [
    {
      name: 'graph_2_a1',
      type: 'bar',
      data: [4762.187359625, 4727.214973541667, 4741.068045166667, 4746.16972675, 4838.891303208334, 4565.644643833333, 4245.382475166667, 4486.100311833333, 4684.916222166667, 4822.108195541667, 4753.77854925, 4847.551208666667, 4804.1144475, 4683.7081206249995, 4671.36282525, 4444.9429265, 3478.325928375, 3953.03894225, 4260.039390416667, 3442.5696865416667, 2628.691527625, 2006.2001822083332, 2791.389707625, 2802.87632375, 2431.1700890458333, 2710.350092, 2569.26714765, 2509.057054125, 2877.6067460416666, 3263.127827625]
    }
  ]
};
graph_2_a1.setOption(option);



var graph_2_b2 = echarts.init(document.getElementById('graph_2_b2'));	
window.onresize = function() {
    graph_2_b2.resize();
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
      data: [{value: 34074.96763819095, name:'Steam'},{value: 11831.353003130487, name:'Electricity'},{value: 209891.08952821424, name:'Chilled Water'},{value: 54153.815536075075, name:'Hot Water'},{value: 13086.048348412236, name:'Natural Gas'}]
    }
  ]
};
graph_2_b2.setOption(option);


