var app = angular.module('dlHealthSummaryDamageNationwideApp', []);

app.controller("DlHealthSummaryDamageNationwideController", ['$scope','$http',function ($scope,$http) {

 $scope.district;
 $scope.incident;
 $scope.dl_data={};
 $scope.is_edit = false;

    var init_data = {
        'Table_10': {
            'DsnPubP1Lmh': [{
                facilities_assets : 'Teaching Hospitals',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Provincial General Hospitals',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'District General Hospitals',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                }],
                'DsnPubP1Moh': [{
                facilities_assets : 'Offices',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Others',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                }],
                'DsnPubP1Omc': [{
                facilities_assets : 'Base Hospital',
                total_num_affected :null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Divisional Hospital',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Rural Hospital',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Central Dispensary',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'PMCUs',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'PHCCs',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'MCHCs',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'TOTAL',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                }],
                'DsnPubPnLmh': [{
                facilities_assets : 'Teaching Hospitals',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Provincial General Hospitals',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'District General Hospitals',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                }],
                'DsnPubPnMoh': [{
                facilities_assets : 'Offices',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Others',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                }],
                'DsnPubPnOmc': [{
                facilities_assets : 'Base Hospital',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Divisional Hospital',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Rural Hospital',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Central Dispensary',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'PMCUs',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'PHCCs',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'MCHCs',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'TOTAL',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'GRAND TOTAL',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                }],
                'DsnPvtP1': [{
                facilities_assets : 'Private Clinics',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Others',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                }],
                'DsnPvtPn': [{
                facilities_assets : 'Private Clinics',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Others',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                },{
                facilities_assets : 'TOTAL',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages: null,
                losses_y1 : null,
                losses_y2 : null,
                total_losses : null,
                }],
                'DsnTdlOwship': [{
                ownership : 'Public Sector',
                damages : null,
                losses_y1 : null,
                losses_y2 : null,
                total : null,
                },{
                ownership : 'Private Sector',
                damages : null,
                losses_y1 : null,
                losses_y2 : null,
                total : null,
                },{
                ownership : 'TOTAL',
                damages : null,
                losses_y1 : null,
                losses_y2 : null,
                total : null,
                }]



        }
    }


  $scope.dlhealthsummarydamagenationwide = init_data;

   $scope.SaveData = function() {
        console.log($scope.data);

        $http({
            method: 'POST',
            url: '/damage_losses/dl_save_data',
            contentType: 'application/json; charset=utf-8',
            data: angular.toJson({
                'table_data': $scope.dlhealthsummarydamagenationwide,
                'com_data': {
                    'district': $scope.district,
                    'incident' : $scope.incident,
                },
                'is_edit':$scope.is_edit
            }),
            dataType: 'json',
        }).then(function successCallback(response) {

            console.log(response);

        }, function errorCallback(response) {

            console.log(response);
        });

    }


    // get relevant damage_losses data for calculations


    $scope.changedValue = function getDlData()
    {


        if($scope.district && $scope.incident){
        console.log($scope.district);
        console.log($scope.incident);
        $http({
        method: 'POST',
        url: '/damage_losses/dl_get_data',
        contentType: 'application/json; charset=utf-8',
        data: angular.toJson({
                'db_tables': ['DspPubD1Lmh','DspPubDnLmh','DspPubDnMoh','DspPubD1Moh','DspPubD1Omc','DspPubDnOmc','DspPvtD1','DspPvtDn'],
                'com_data': {
                    'district': $scope.district,
                    'incident': $scope.incident,
                }
            }),
        dataType: 'json',
        }).then(function successCallback(response) {
            var data = response.data;
            angular.forEach(data, function(value, key) {
              $scope.dl_data[key] = JSON.parse(value);
            });

            console.log($scope.dl_data);

        }, function errorCallback(response) {

            console.log(response);
        });
        }

    }

  // edit relevant damage_losses data


    $scope.dlDataEdit = function()
{

   $scope.is_edit = true;

    $http({
    method: "POST",
    url: '/damage_losses/dl_fetch_edit_data',
    data: angular.toJson({
    'table_name':  'Table_1null',
    'com_data': {
           'district': $scope.district,
            'incident': $scope.incident,
          },
           'is_edit':$scope.is_edit
           }),
    }).success(function(data) {

    console.log(data);


    $scope.dlhealthsummarydamagenationwide = data;
    })


}


    $scope.cancelEdit = function()
{
     $scope.is_edit = false;
     $scope.dlhealthsummarydamagenationwide = init_data;
}



}])



