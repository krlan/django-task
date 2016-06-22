var app;

app = angular.module('App', []);

app.controller('AppController', [
  '$scope', '$http', function($scope, $http) {
    $scope.schools = [];
    return $http.get('/api/school').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.schools.push(item);
      });
    });
  }
]);

app.controller('SchoolController', [
  '$scope', '$http', function($scope, $http) {
    $scope.classrooms = [];
    return $http.get('/api/class').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.classrooms.push(item);
      });
    });
  }
]);

app.controller('ClassController', [
  '$scope', '$http', function($scope, $http) {
    $scope.students = [];
    return $http.get('/api/student').then(function(result) {
      return angular.forEach(result.data, function(item) {
        return $scope.students.push(item);
      });
    });
  }
]);

