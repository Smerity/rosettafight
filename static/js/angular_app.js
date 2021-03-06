var RosettaApp = angular.module('RosettaFight', [])
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

// The general controller for interacting with tasks for Rosetta Fight
function RosettaController($scope, $http) {
  //
  $scope.taskSelector = null;
  $scope.selectedTask = null;
  //
  $scope.tasklist = null;
  $scope.solutions = null;
  $scope.availableLanguages = function() { return Object.keys($scope.solutions).sort(); }
  $scope.totalSolutions = function() { return Object.size($scope.solutions); }
  $scope.startLangs = ['python', 'go'];

  // Encode the task to a simpler URL friendly, but still readable, format
  $scope.taskUri = function(task) {
      return task.replace(/[^A-Za-z0-9]/g, '');
  }

  // Retrieve and populate the solutions for a specific task
  $scope.retrieveTask = function() {
    $scope.selectedTask = $scope.taskSelector;
    // Empty task -- just ignore the request
    if ($scope.selectedTask === null) return;
    $http.get('/data/tasks/' + $scope.taskUri($scope.selectedTask) + '.json', {cache:true}).then(
      function(resp) {
        $scope.solutions = resp.data['solutions'];
      }
    )
  }

  // Load the initial tasklist on start-up
  $http.get('/data/tasklist.json', {cache:true}).then(
    function(resp) {
      $scope.tasklist = resp.data['tasklist'];
    }
  );
}

// The 'mini' controller that specifies the language solutions to show for the CodeView
function CodeViewController($scope) {
  $scope.lang = $scope.startLang;
  // Current solution being viewed
  $scope.solutionId = 0;
  $scope.activateSolution = function(solutionId) {
    $scope.solutionId = solutionId;
  }
  // Reset to the first solution if the task or language changes
  $scope.$watch('selectedTask', function() {$scope.solutionId = 0;});
  // Note: select needs to have ng-model set to "$parent.lang", not "lang", as child scope is created
  // See: https://github.com/angular-ui/ui-select2/issues/14
  $scope.$watch('lang', function() {$scope.solutionId = 0;});
}

// JS, you make it hard for me to like you
// http://stackoverflow.com/questions/5223/length-of-javascript-object-ie-associative-array
Object.keys = function(obj) {
  var keys = [];
  for (key in obj) {
    keys.push(key);
  }
  return keys;
};
Object.size = function(obj) {
  return Object.keys(obj).length;
};
