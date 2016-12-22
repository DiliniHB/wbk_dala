var app = angular.module('dlHealthDamagelostPrivateApp', [])

app.controller('dlHealthDamagelostPrivateAppController', ['$scope', '$http', function($scope, $http) {
    $scope.district;
    $scope.dlDate;
    $scope.incident;
    $scope.submitted = false;
    $scope.Districts=[];

    $scope.is_edit = false;

    var init_data = {
        'Table_7': {
            //tab 1
            'DapNapTmf' : [{
                type_med_fac : 'Private Clinics',
                num_affected_fac : 0,
                male : 0,
                female : 0,
            }, {
                type_med_fac : 'Others',
                num_affected_fac : 0,
                male : 0,
                female : 0,
            }, {
                type_med_fac : 'TOTAL',
                num_affected_fac : 0,
                male : 0,
                female : 0,
            }],
            //tab 2
            'DapBefPc1': [{
                pvt_clinics : 'Structure',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }, {
                pvt_clinics : 'Supplies and Materials',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }, {
                pvt_clinics : 'Equipment',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }, {
                pvt_clinics : 'Total',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }],
            'DapBefPcn': [{
                pvt_clinics : 'Structure',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }, {
                pvt_clinics : 'Supplies and Materials',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }, {
                pvt_clinics : 'Equipment',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }, {
                pvt_clinics : 'Total',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }],
            'DapBefOther': [{
                pvt_clinics : 'Structure',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }, {
                pvt_clinics : 'Supplies and Materials',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }, {
                pvt_clinics : 'Equipment',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }, {
                pvt_clinics : 'Total',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }, {
                pvt_clinics : 'TOTAL',
                est_replacement_cost : 0,
                est_repair_cost : 0,
                total_damages : 0,
                est_losses_y1 : 0,
                est_losses_y2 : 0,
                total_losses : 0,
            }]
        }
    }

    $scope.dlHealthDamagelostPrivateSys = init_data;

    $scope.saveDlHealthDamagelostPrivate = function(form) {
        console.log($scope.data);
        $scope.submitted = true;
       if(form.$valid){
        $http({
            method : 'POST',
            url : '/damage_losses/dl_save_data',
            contentType: 'application/json; charset=utf-8',
            data: angular.toJson({
                'table_data': $scope.dlHealthDamagelostPrivateSys,
                'com_data':{
                    'district': $scope.district.Id,
                    'incident': $scope.incident,

                },
                'is_edit': $scope.is_edit
            }),
            dataType: 'json',
        }).then(function mySucces(response) {
$("#modal-container-239453").modal('show');
            //if data sent to server side method successfull
            console.log(response);
            }, function myError(response) {
                //if data sent to server side method unsuccessfull
                console.log(response);
        });
        }
    }

    $scope.dlDataEdit = function(form){
        $scope.is_edit = true;
        $scope.submitted = true;

    if(form.$valid){

        $http({
        method: "POST",
        url: '/damage_losses/dl_fetch_edit_data',
        data: angular.toJson({
        'table_name':  'Table_7',
        'com_data': {
               'district': $scope.district.Id,
                'incident': $scope.incident,
              },
//               'is_edit':$scope.is_edit
               }),
        }).success(function(data) {

        console.log(data);

        $scope.dlHealthDamagelostPrivateSys = data;
        })
        }
    }

    $scope.cancelEdit = function() {
         $scope.is_edit = false;
         $scope.dlHealthDamagelostPrivateSys = init_data;
    }

    $scope.changeIncident = function getDistrictData()
    {


    $scope.Districts  = [

            {  Id: 1,
                Name: 'Colombo'
            }, {
                Id: 2,
                Name: 'Gampaha'
            }, {
                Id: 3,
                Name: 'Kaluthara'
            }
              ]

  }
   // Sachie
   // get relevant base-line data for calculations
    $scope.changedValue=function getBsData() {


        if($scope.incident){

       $http({
    method: "POST",
    url: "/damage_losses/fetch_incident_districts",
    data: angular.toJson({'incident': $scope.incident }),
    }).success(function(data) {
        $scope.districts = data;
        $scope.district = "";
        console.log(data);

    })
        }


    }
}])
