document.getElementById('graph_2_d1').innerHTML = '<h1 class="mdui-center">5,263,240.82<span class="unit-opacity">kBTU</span></h1>';

document.getElementById('graph_2_d2').innerHTML = '<h1 class="mdui-center"><span class="unit-opacity">$</span>876,305.3</h1>';

document.getElementById('graph_2_d3').innerHTML = '<h1 class="mdui-center"><span class="unit-opacity">$</span>832.99</h1>';


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
        stillShowZeroSum: false,
        label:{
            fontSize:9,
            position: 'inner'
        },
      data: [{value: 2137279.105732002, name:'Steam'},{value: 924294.2516145994, name:'Electricity'},{value: 2201667.4661004, name:'Chilled Water'},{value: 0.0, name:'Natural Gas'}]
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
      data: [8087.549403625, 8036.76356975, 8300.796682458333, 8198.545968541666, 8459.909161583333, 7762.795561541667, 7204.837666791666, 7993.6170375, 8218.370010083334, 8580.0697665, 8606.104565166666, 8324.922838958333, 8557.460467916666, 8302.336753375, 8934.23155725, 6741.7952165, 6053.361288083333, 6814.983991375, 7704.794239916667, 6458.823000375, 5872.297717083333, 5888.092140458333, 6011.199530041667, 6173.0538435416665, 6236.547626583333, 6260.9414506250005, 6321.605924958333, 6196.438880458333, 6563.980260875, 6435.4748545]
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
        stillShowZeroSum: false,
        label:{
            fontSize:9,
            position: 'inner'
        },
      data: [{value: 48364.80034639373, name:'Steam'},{value: 29229.586679136948, name:'Electricity'},{value: 740917.5741598697, name:'Chilled Water'},{value:0, name:'Hot Water'},{value: 57793.33654273429, name:'Natural Gas'}]
    }
  ]
};
graph_2_b2.setOption(option);


