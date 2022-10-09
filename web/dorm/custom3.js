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
    data: [2018, 2019, 2020, 2020]
  },
  yAxis: {
	  name: 'kBTU',
	  type: 'value'
  },
  series: [
    {
      type: 'line',
      data: [17099450.82133264, 20830341.464538854, 22754012.985649865, 27269844.36180426]
    }
  ]
};
graph_3_c1.setOption(option);

	
document.getElementById('graph_3_d2').innerHTML = '<h1 class="mdui-center"><span class="unit-opacity">$</span>2,622,153.78</h1>';

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
      data: [{value: 3920473.4014070267, name:'Steam'},{value: 6771004.977916097, name:'Electricity'},{value: 4153342.5057110772, name:'Chilled Water'},{value: 14546945.431377202, name:'Hot Water'}]
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
      data: [{value: 175094.4631557789, name:'Steam'},{value: 119613.50559392481, name:'Electricity'},{value: 1867552.3390121679, name:'Chilled Water'},{value: 331669.3191360638, name:'Hot Water'},{value: 128224.14898516258, name:'Natural Gas'}]
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
    data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  },
  yAxis: {
	  type: 'value',
	  name: 'total energy usage for a month(kBTU)'
  },
  series: [
    {
      type: 'line',
      data: ['296807.49706063425', '261558.42256879114', '180114.35162647613', '274484.24229321314', '270307.6917046873', '233552.93341341562', '254115.71998181907', '196299.90520050575', '228067.40984075813', '237166.6218816516', '325891.1481250782', '323037.274054023']
    }
  ]
};
graph_3_c2.setOption(option);
