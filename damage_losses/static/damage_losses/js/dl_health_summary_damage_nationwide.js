var app = angular.module('dlHealthSummaryDamageNationwideApp', []);

app.controller("DlHealthSummaryDamageNationwideController", ['$scope','$http',function ($scope,$http) {

 $scope.district;
 //bind Disasteroption
    $scope.dlhealthsummarydamagenationwide = {
        'Table_10': {
            'DsnPubP1Lmh': [{
                facilities_assets : 'Teaching Hospitals',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Provincial General Hospitals',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'District General Hospitals',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Total',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                }],
                'DsnPubP1Moh': [{
                facilities_assets : 'Offices',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Others',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Total',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                }],
                'DsnPubP1Omc': [{
                facilities_assets : 'Base Hospital',
                total_num_affected :0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Divisional Hospital',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Rural Hospital',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Central Dispensary',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'PMCUs',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'PHCCs',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'MCHCs',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Total',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'TOTAL',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                }],
                'DsnPubPnLmh': [{
                facilities_assets : 'Teaching Hospitals',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Provincial General Hospitals',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'District General Hospitals',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Total',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                }],
                'DsnPubPnMoh': [{
                facilities_assets : 'Offices',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Others',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Total',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                }],
                'DsnPubPnOmc': [{
                facilities_assets : 'Base Hospital',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Divisional Hospital',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Rural Hospital',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Central Dispensary',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'PMCUs',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'PHCCs',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'MCHCs',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Total',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'TOTAL',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'GRAND TOTAL',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                }],
                'DsnPvtP1': [{
                facilities_assets : 'Private Clinics',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Others',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Total',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                }],
                'DsnPvtPn': [{
                facilities_assets : 'Private Clinics',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Others',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'Total',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                },{
                facilities_assets : 'TOTAL',
                total_num_affected : 0,
                male : 0,
                female : 0,
                total_damages: 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total_losses : 0,
                }],
                'DsnTdlOwship': [{
                ownership : 'Public Sector',
                damages : 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total : 0,
                },{
                ownership : 'Private Sector',
                damages : 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total : 0,
                },{
                ownership : 'TOTAL',
                damages : 0,
                losses_y1 : 0,
                losses_y2 : 0,
                total : 0,
                }]



        }
    }


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

                }
            }),
            dataType: 'json',
        }).then(function successCallback(response) {

            console.log(response);

        }, function errorCallback(response) {

            console.log(response);
        });

    }




 }])


