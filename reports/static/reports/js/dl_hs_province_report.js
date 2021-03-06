var app = angular.module('dlHsProvinceApp', []);

app.controller("DlHsProvinceController", ['$scope','$http',function ($scope,$http) {

 $scope.district;
 $scope.incident;
 $scope.province;
 $scope.dl_data={};
 $scope.submitted = false;

    $scope.dlHsProvince = {
        'Table_9': {
            'DspPubD1Lmh': [{
                facilities_assets : 'Teaching Hospitals',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'Provincial General Hospitals',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'District General Hospitals',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                }],
                'DspPubD1Moh': [{
                facilities_assets : 'Offices',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'Others',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                }],
                'DspPubD1Omc': [{
                facilities_assets : 'Base Hospital',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'Divisional Hospital',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'Rural Hospital',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'Central Dispensary',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'PMCUs',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'PHCCs',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'MCHCs',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'TOTAL',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                }],
                'DspPubDnLmh': [{
                facilities_assets : 'Private Clinics',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'Others',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'District General Hospitals',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null,
                }],
                'DspPubDnMoh': [{
                facilities_assets : 'District General Hospitals',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null
                },{
                facilities_assets : 'District General Hospitals',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null
                },{
                facilities_assets : 'Total',
                total_num_affected : null,
                male : null,
                female : null,
                total_damages : null,
                losses_y1 : null,
                losses_y2  : null,
                total_losses : null
                }
                ],
                'DspPubDnOmc': [
                {
                 facilities_assets: null,
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },
                 {
                 facilities_assets: null,
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },
                {
                 facilities_assets: null,
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },{
                 facilities_assets: null,
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },{
                 facilities_assets: null,
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },{
                 facilities_assets: null,
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },{
                 facilities_assets: null,
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },{
                 facilities_assets: 'Total',
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },{
                 facilities_assets: 'TOTAL',
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },{
                 facilities_assets: 'GRAND TOTAL',
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                }
                ],
                'DspPvtD1': [
                {
                 facilities_assets: null,
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },{
                 facilities_assets: null,
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },{
                 facilities_assets: null,
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                }
                ],
                'DspPvtDn': [
                {
                 facilities_assets: null,
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },{
                 facilities_assets: null,
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },{
                 facilities_assets: 'Total',
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                },{
                 facilities_assets: 'TOTAL',
                 total_num_affected: null,
                 male: null,
                 female: null,
                 total_damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total_losses: null,
                }
                ],
                'DspTdlOwship': [
                {
                 ownership: null,
                 damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total: null,
                },{
                 ownership: null,
                 damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total: null,
                },{
                 ownership: 'TOTAL',
                 damages: null,
                 losses_y1: null,
                 losses_y2: null,
                 total: null,
                }
                ]
        }
    }

$scope.filterData = function filterData(form)
{
$scope.submitted = true;
if(form.$valid){
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

$scope.provinces = [];
$scope.fetchProvinces = function fetchProvinces(incident_id)
{
    $http({
    method: "POST",
    url: "/damage_losses/fetch_incident_provinces",
    data: angular.toJson({'incident': $scope.incident }),
    }).success(function(data) {
        $scope.provinces = data;
        $scope.province = "";
        console.log(data);

    })

}

 }])


