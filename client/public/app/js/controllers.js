
app.controller('LoginController',function ($scope, AuthService){
    $scope.process = function(){
        AuthService.login($scope.username, $scope.password, $scope.code);
    }
});
