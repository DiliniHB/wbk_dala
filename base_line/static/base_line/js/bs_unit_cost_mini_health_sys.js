var app= angular.module('unitCostMiniHealthSysApp', [])

app.controller('unitCostMiniHealthSysController', ['$scope', '$http', function($scope, $http) {
    $scope.district;
    $scope.baselineDate;

    $scope.bsUnitCostMiniHealthSys = {
        'Table_3': {
            'BucMarStructure': [{
                particulars : '1 Floor Structure',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }, {
                particulars : '2-3 Floors Structure',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }, {
                particulars : 'More Than 3 Floors Structure',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }],
            'BucMarSupplies': [{
                particulars : 'Medicines',
                teaching_hospital:null,
                provincial_general_hospital:null,
                district_general_hospital:null,
            }, {
                particulars : 'Medical Supplies',
                teaching_hospital:null,
                provincial_general_hospital:null,
                district_general_hospital:null,
            }, {
                particulars : 'Others',
                teaching_hospital:null,
                provincial_general_hospital:null,
                district_general_hospital:null,
            }],
            'BucMarMequipment' : [{
                particulars : 'CT Scan',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
             }, {
                particulars : 'X-ray Machine',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
             }, {
                particulars : 'MRI Machine',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
             }, {
                particulars : 'Other Equipment (Specify)',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
             }],
            'BucMarOassets' : [{
                particulars : 'Computers',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }, {
                particulars : 'Vehicles',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }, {
                particulars : 'Furniture',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }, {
                particulars : 'Office Equipment',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }, {
                particulars : 'Others',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }],
            //----
            'BucMarcStructures': [{
                particulars : 'Roof',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }, {
                particulars : 'Wall',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }, {
                particulars : 'Flooring',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }],
            'BucMarcMequipment' : [{
                particulars : 'CT Scan',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
            }, {
                particulars : 'X-ray Machine',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
            }, {
                particulars : 'MRI Machine',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
            }, {
                particulars : 'Other Equipment (Specify)',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
             }],
            'BucMarcOassets' : [{
                particulars : 'Computers',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }, {
                particulars : 'Vehicles',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }, {
                particulars : 'Furniture',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }, {
                particulars : 'Office Equipment',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }, {
                particulars : 'Others',
                teaching_hospital :null,
                provincial_general_hospital :null,
                district_general_hospital :null,
                office :null,
                other :null,
            }],
            'BucMarcCrpm': [{
                particulars : 'Average Construction Period',
                teaching_hospital:null,
                provincial_general_hospital:null,
                district_general_hospital:null,
                office :null,
                other :null,
            }, {
                particulars : 'Average Repair Period',
                teaching_hospital:null,
                provincial_general_hospital:null,
                district_general_hospital:null,
                office :null,
                other :null,
            }]
        }
    }

    $scope.saveBucMarStructure = function() {
        console.log($scope.data);
        $http({
            method : 'POST',
            url : '/base_line/bs_save_data',
            contentType: 'application/json; charset=utf-8',
            data: angular.toJson({
                'table_data': $scope.bsUnitCostMiniHealthSys,
                'com_data':{
                    'district': $scope.district,
                    'bs_date': $scope.baselineDate,

                },
                 'is_edit' : false
            }),
            dataType: 'json',
        }).then(function mySucces(response) {

            //if data sent to server side method successfull
	$("#modal-container-239453").modal('show');
            console.log(response);
 
            }, function myError(response) {
                //if data sent to server side method unsuccessfull
                console.log(response);
        });
    }
}])
