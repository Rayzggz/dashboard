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
      data: [18097320.480381913, 99642373.24738498, 63564051.464043714, 58772584.60255662]
    }
  ]
};
graph_3_c1.setOption(option);

	
document.getElementById('graph_3_d2').innerHTML = '<h1 class="mdui-center"><span class="unit-opacity">$</span>7,294,958.04</h1>';

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
        stillShowZeroSum: false,
        label:{
            fontSize:9,
            position: 'inner'
        },
      data: [{value: 29685840.262311168, name:'Steam'},{value: 11225655.988068227, name:'Electricity'},{value: 21240053.588434976, name:'Chilled Water'},{value: 6.611516222999999, name:'Natural Gas'}]
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
        stillShowZeroSum: false,
        label:{
            fontSize:9,
            position: 'inner'
        },
      data: [{value: 546279.1308572036, name:'Steam'},{value: 342494.36938977207, name:'Electricity'},{value: 5858349.224258548, name:'Chilled Water'},{value:0, name:'Hot Water'},{value: 547835.3150864487, name:'Natural Gas'}]
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
      data: ['582366.3104413521', '348274.4227010335', '330223.3214013977', '358620.45878371457', '421826.1811290571', '434283.46385826415', '616995.9460398003', '1057937.2912968379', '1174178.6373765885', '1281723.4742348122', '1168929.2561154957', '876305.2977281347']
    }
  ]
};
graph_3_c2.setOption(option);
