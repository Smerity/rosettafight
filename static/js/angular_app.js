angular.module('RosettaFight', [])
.filter('prettify', function() {
  return function(input) {
    return prettyPrintOne(input);
  };
})
.filter('escapeHTML', function() {
  return function(text) {
    if (text) {
      return text.
          replace(/&/g, '&amp;').
          replace(/</g, '&lt;').
          replace(/>/g, '&gt;').
          replace(/'/g, '&#39;').
          replace(/"/g, '&quot;');
    }
    return '';
  }
});

function RosettaController($scope, $http) {
  //
  $scope.taskSelector = null;
  $scope.selectedTask = null;
  //
  $scope.tasklist = null;
  $scope.solutions = null;

  $scope.taskUri = function(task) {
      return task.replace(/[^A-Za-z0-9]/g, '');
    }


  $scope.retrieveTask = function() {
    $scope.selectedTask = $scope.taskSelector;
    $http.get('/data/tasks/' + $scope.taskUri($scope.selectedTask) + '.json').then(
      function(resp) {
        $scope.solutions = resp.data['solutions'];
      }
    )
  }

  $scope.totalSolutions = function() { return Object.size($scope.solutions); }

  $http.get('/data/tasklist.json').then(
    function(resp) {
      $scope.tasklist = resp.data['tasklist'];
    }
  );
}

// JS, you make it hard for me to like you
// http://stackoverflow.com/questions/5223/length-of-javascript-object-ie-associative-array
Object.size = function(obj) {
  var size = 0, key;
  for (key in obj) {
    if (obj.hasOwnProperty(key)) size++;
  }
  return size;
};
