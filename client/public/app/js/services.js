app.factory('AuthService', function ($rootScope, $http, $cookies, $location) {
    return {
        login: function (username, password, code){
            $http.post(BASE_URL+'/login', {username: username, password:password, code:code})
                .success(function(data){
                    $cookies.access_token = data['access_token'];
                    $rootScope.access_token = data['access_token'];
                    $location.path('/chat');
                })
                .error(function(data){

                })
        }
    };
});
