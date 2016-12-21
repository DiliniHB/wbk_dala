var app = angular.module('dlHsNationalApp', []);

app.controller("DlHsNationalController", ['$scope','$http',function ($scope,$http) {

 $scope.district;
 $scope.incident;
 $scope.dl_data={};

    $scope.dlhealthsectordistrict = {
        'Table_8': {
            'DshPubLmh': [{
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
                'DshPubMoh': [{
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
                'DshPubOmf': [{
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
                'DshPvtFa': [{
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
                facilities_assets : 'TOTAL',
                total_num_affected :0,
                male :0,
                female :0,
                total_damages :0,
                losses_y1 :0,
                losses_y2  :0,
                total_losses :0,
                }],
                'DshTdlOwship': [{
                ownership : 'Public Sector',
                damages :0,
                losses_y1 :0,
                losses_y2 :0,
                total :0,
                },{
                ownership : 'Private Sector',
                damages :0,
                losses_y1 :0,
                losses_y2 :0,
                total :0,
                },{
                ownership : 'TOTAL',
                damages :0,
                losses_y1 :0,
                losses_y2 :0,
                total :0,
                }

                ]



        }
    }

 }])


