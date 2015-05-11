var app = angular.module('app', ['ui.router', 'ngCookies']);

app.factory('authHttpResponseInterceptor', function($q, $location, $rootScope){
    return {
        request: function(config) {
          config.headers['Authorization'] = 'Bearer '+$rootScope.access_token;
          return config;
        },
        response: function(response){
            if (response.status === 401) {
                console.log("Response 401");
            }
            return response || $q.when(response);
        },
        responseError: function(rejection) {
            if (rejection.status === 401) {
                console.log("Response Error 401",rejection);
                $location.path('/login');
            }
            return $q.reject(rejection);
        }
    }
});

app.config(function($stateProvider, $httpProvider){
  $stateProvider.state('login', {
    url: '/login',
    views: {
      'main': {templateUrl: 'app/tpls/login.html'}
    }
  })
  .state('chat', {
    url: '/chat',
    views: {
      'navbar': {templateUrl: 'app/tpls/menu.html'},
      'main': {templateUrl: 'app/tpls/chat.html', controller:'ChatController'}
    }
  })
  .state('queue', {
    url: '/queue',
    views: {
      'navbar': {templateUrl: 'app/tpls/menu.html'},
      'main': {templateUrl: 'app/tpls/queue.html', controller:'MessageQueueController'}
    }
  })
  .state('contacts', {
    url: '/contacts',
    views: {
      'navbar': {templateUrl: 'app/tpls/menu.html'},
      'main': {templateUrl: 'app/tpls/contacts.html', controller:'ContactController'}
    }
  });
  $httpProvider.interceptors.push('authHttpResponseInterceptor');
});

app.run(function($rootScope, $cookies){
  $rootScope.access_token = $cookies.access_token;
});
