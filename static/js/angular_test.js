'use strict';

describe('Test Angular in Rosetta Fight', function() {
  var scope, ctrl, $httpBackend;

  beforeEach(inject(function(_$httpBackend_, $rootScope, $controller) {
    // Following http://docs.angularjs.org/tutorial/step_05
    $httpBackend = _$httpBackend_;
    $httpBackend.when('GET', '/data/tasklist.json').respond(
      {tasklist: ['Addition', '0/1-Knapsack', 'Pythagoras', 'Vigenere']}
    );
    scope = $rootScope.$new();
    ctrl = $controller(RosettaController, {$scope: scope});
  }));

  it('should start with tasklist as null', inject(function() {
    expect(scope.tasklist).toEqual(null);
  }));

  it('should retrieve tasklist.json and populate tasklist', inject(function() {
    // We expect just the one AJAX call to tasklist.json
    $httpBackend.flush(1);
    // Ensure it hits the request we expect
    $httpBackend.expectGET('/data/tasklist.json');
    // Ensure the stored value is what we expect
    expect(scope.tasklist).toEqual(['Addition', '0/1-Knapsack', 'Pythagoras', 'Vigenere']);
  }));

  // TODO: Full browser end-to-end test

  it('should request solutions if selecting a task to view', inject(function() {
    // AJAX: tasklist.json
    $httpBackend.flush(1);

    // We expect the GET requests for the task's solutions
    $httpBackend.when('GET', '/data/tasks/01Knapsack.json').respond(
      {solutions: {python: ['print', 'sys.stdout'], go: ['fmt.Println']}}
    );
    $httpBackend.expectGET('/data/tasks/01Knapsack.json');

    scope.taskSelector = '0/1-Knapsack';
    scope.retrieveTask();

    // AJAX: 01Knapsack.json
    $httpBackend.flush(1);
    expect(scope.selectedTask).toEqual('0/1-Knapsack');
    expect(scope.solutions).toEqual({python: ['print', 'sys.stdout'], go: ['fmt.Println']});
  }));
});
