
var app = angular.module('dlHsDistrictChartApp', ["nvd3"]);

app.controller("DlHsDistrictChartController", ['$scope','$http',function ($scope,$http) {

 $scope.district;
 $scope.incident;

/*$scope.options = {
    chart: {
        type: "discreteBarChart",
        height: 250,
        //x: function(d){return (d.facilities_assets);},
        //y: function(d){return parseInt(d.female);},
        x: function(d){return d[0];},
         y: function(d){return d[1];},
        showValues: true,
        transitionDuration: 200,
        xAxis: {
            axisLabel: "Date",
            rotateLabels: -20
        },
        yAxis: {
            axisLabel: "No. of Incidents",
            axisLabelDistance: 30
        }
    }
}*/

 $scope.options = {
            chart: {
                type: 'multiBarChart',
                height: 450,
                x: function(d){return d[0];},
                y: function(d){return d[1];},
                stacked: true,
                barColor: function(d, i){
                  var colors = d3.scale.category20().range();
                  var rnd = Math.floor(Math.random() * colors.length)
                  return colors[rnd];
                }
            }
        };

$scope.optionsOwnership = {
    chart: {
        type: "discreteBarChart",
        height: 250,
        x: function(d){return (d.ownership);},
        y: function(d){return parseInt(d.total);},
        showValues: true,
        transitionDuration: 200,
        xAxis: {
            axisLabel: "Date",
            rotateLabels: -20
        },
        yAxis: {
            axisLabel: "No. of Incidents",
            axisLabelDistance: 30
        }
    }
}



function setChartData()
{

//$scope.api.updateWithData($scope.data);
//$scope.api.refresh();

}


function setData(chartName, data)
{
var chartData;

chartData = [
                /*{
                    key: 'ghnj',
                    values: data,
                    //color: "#ff7f0e",
                    strokeWidth: 2,
                },
                {
                    "key": "Total Sueños",
                    "values": [['gnh',300000], ['h', 1000000]]
                }
                */
                {
                    "key": "Total Damages",
                    "values": data.key_1
                }
                , {
                    "key": "Total Losses",
                    "values": data.key_2
                }
            ];


 return chartData;
}

$scope.generateCharts = function generateChart()
{
    $http({
    method: "POST",
    url: "/charts/dl_fetch_chart_data",
    data: angular.toJson({'table_name': 'Table_8',
     'chart_stacked_data':
    {'DshPubLmh': {'hfa_pub_dl':
    {'key_1': ['facilities_assets', 'total_damages'],
     'key_2': ['facilities_assets', 'total_losses']},
    },
    'DshPubMoh': {'hfa_pub_dl':
    {'key_1': ['facilities_assets', 'total_damages'],
     'key_2': ['facilities_assets', 'total_losses']},
    },
    'DshPubOmf': {'hfa_pub_dl':
    {'key_1': ['facilities_assets', 'total_damages'],
     'key_2': ['facilities_assets', 'total_losses']},
    },
    'DshPvtFa': {'hfa_pvt_dl':
    {'key_1': ['facilities_assets', 'total_damages'],
     'key_2': ['facilities_assets', 'total_losses']},
    },
    'DshTdlOwship': {'hfa_ownership_dl':
    {'key_1': ['ownership', 'damages'],
     'key_2': ['ownership', 'losses_y1'],
     'key_3': ['ownership', 'losses_y2']},
    },
    },

     'com_data': {'district': $scope.district,
          'incident': $scope.incident} }),
    }).success(function(data) {

    console.log(data.Table_8.DshPubLmh);

    $scope.dshPubLmhDl = setData('chart_1', data.Table_8.DshPubLmh.hfa_pub_dl);


     $scope.dshPubMohDl = setData('chart_2', data.Table_8.DshPubMoh.hfa_pub_dl);

     $scope.dshPubOmfDl = setData('chart_3', data.Table_8.DshPubOmf.hfa_pub_dl);

     $scope.dshPvtFa = setData('chart_4', data.Table_8.DshPvtFa.hfa_pvt_dl);
     $scope.dshTdlOwshipDl = setData('chart_5', data.Table_8.DshTdlOwship.hfa_ownership_dl);

    })

}


 }])


