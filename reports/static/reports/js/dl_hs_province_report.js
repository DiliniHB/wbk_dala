var app = angular.module('dlHsProvinceApp', []);

app.controller("DlHsProvinceController", ['$scope','$http',function ($scope,$http) {

 $scope.district;
 $scope.incident;
 $scope.province;
 $scope.dl_data={};

    $scope.dlHsProvince = {
        'Table_9': {
            'DspPubD1Lmh': [{
                facilities_assets : 'Teaching Hospitals',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'Provincial General Hospitals',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'District General Hospitals',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'Total',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                }],
                'DspPubD1Moh': [{
                facilities_assets : 'Offices',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'Others',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'Total',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                }],
                'DspPubD1Omc': [{
                facilities_assets : 'Base Hospital',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'Divisional Hospital',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'Rural Hospital',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'Central Dispensary',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'PMCUs',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'PHCCs',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'MCHCs',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'Total',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'TOTAL',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                }],
                'DspPubDnLmh': [{
                facilities_assets : 'Private Clinics',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'Others',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'District General Hospitals',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                },{
                facilities_assets : 'Total',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                }],
                'DspPubDnMoh': [{
                facilities_assets : 'District General Hospitals',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0
                },{
                facilities_assets : 'District General Hospitals',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0
                },{
                facilities_assets : 'Total',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0
                }
                ],
                'DspPubDnOmc': [
                {
                 facilities_assets: 0,
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },
                 {
                 facilities_assets: 0,
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },
                {
                 facilities_assets: 0,
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },{
                 facilities_assets: 0,
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },{
                 facilities_assets: 0,
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },{
                 facilities_assets: 0,
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },{
                 facilities_assets: 0,
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },{
                 facilities_assets: 'Total',
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },{
                 facilities_assets: 'TOTAL',
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },{
                 facilities_assets: 'GRAND TOTAL',
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                }
                ],
                'DspPvtD1': [
                {
                 facilities_assets: 0,
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },{
                 facilities_assets: 0,
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },{
                 facilities_assets: 0,
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                }
                ],
                'DspPvtDn': [
                {
                 facilities_assets: 0,
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },{
                 facilities_assets: 0,
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },{
                 facilities_assets: 'Total',
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                },{
                 facilities_assets: 'TOTAL',
                 total_num_affected: 0,
                 male: 0,
                 female: 0,
                 total_damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total_losses: 0,
                }
                ],
                'DspTdlOwship': [
                {
                 ownership: 0,
                 damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total: 0,
                },{
                 ownership: 0,
                 damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total: 0,
                },{
                 ownership: 'TOTAL',
                 damages: 0,
                 losses_y1: 0,
                 losses_y2: 0,
                 total: 0,
                }
                ]
        }
    }

$scope.filterData = function filterData()
{

    $http({
    method: "POST",
    url: "/reports/dl_fetch_report_data",
    data: angular.toJson({'table_name': 'Table_9', 'com_data': {'province': $scope.province,
          'incident': $scope.incident} }),
    }).success(function(data) {

    console.log(data);
    $scope.dlHsProvince = data;
    })

}


$scope.submit = function submit()
{
 $http({
    method: "POST",
    url: "/damage_losses/dl_save_data",
    /*data: angular.toJson({'table_name': 'Table_8', 'com_data': {'district': $scope.district,
          'incident': $scope.incident, 'province': $scope.province} }),
    })*/
    data: angular.toJson({'table_data': $scope.dlHsProvince, 'com_data': {'province': $scope.province,
     'incident': $scope.incident},
    'is_edit': false})
    })
    .success(function(data) {

    console.log(data);
    $scope.dlHsProvince = data;
    })

}

 }])


