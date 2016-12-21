
var app = angular.module('dlHsProvinceChartApp', ["nvd3"]);

app.controller("DlHsProvinceChartController", ['$scope','$http',function ($scope,$http) {

 $scope.district;
 $scope.incident;

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
    data: angular.toJson({'table_name': 'Table_9',
     'chart_stacked_data':
    {'DspPubDnLmh': {'hfa_dsp_pub_dl':
    {'key_1': ['facilities_assets', 'total_damages'],
     'key_2': ['facilities_assets', 'total_losses']},
    },
    'DspPubDnMoh': {'hfa_dsp_pub_dl':
    {'key_1': ['facilities_assets', 'total_damages'],
     'key_2': ['facilities_assets', 'total_losses']},
    },
    'DspPubDnOmc': {'hfa_dsp_pub_dl':
    {'key_1': ['facilities_assets', 'total_damages'],
     'key_2': ['facilities_assets', 'total_losses']},
    },
    'DspPvtDn': {'hfa_dsp_pvt_dl':
    {'key_1': ['facilities_assets', 'total_damages'],
     'key_2': ['facilities_assets', 'total_losses']},
    },
    'DspTdlOwship': {'hfa_dsp_ownership_dl':
    {'key_1': ['ownership', 'damages'],
     'key_2': ['ownership', 'losses_y1'],
     'key_3': ['ownership', 'losses_y2']},
    },
    },

     'com_data': {'district': $scope.district,
          'incident': $scope.incident} }),
    }).success(function(data) {


    $scope.dspPubDnLmhDl = setData('chart_1', data.Table_9.DspPubDnLmh.hfa_dsp_pub_dl);


     $scope.dspPubDnMohDl = setData('chart_2', data.Table_9.DspPubDnMoh.hfa_dsp_pub_dl);

     $scope.dspPubDnOmcDl = setData('chart_3', data.Table_9.DspPubDnOmc.hfa_dsp_pub_dl);

     $scope.dspPvtDn = setData('chart_4', data.Table_9.DspPvtDn.hfa_dsp_pvt_dl);

     $scope.dspTdlOwship = setData('chart_5', data.Table_9.DspTdlOwship.hfa_dsp_ownership_dl);

    })

}


 }])


