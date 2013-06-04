'use strict';

describe('Test Object extensions', function() {
  var pokemon = {charmander:'fire', squirtle:'water', bulbasaur:'grass'};

  it('should have the correct set of keys for associative arrays', function() {
    var emptyAssoc = {};
    var complexAssoc = {tree:{branch:'left'}}
    expect(Object.keys(emptyAssoc).sort()).toEqual([]);
    expect(Object.keys(complexAssoc).sort()).toEqual(['tree']);
    expect(Object.keys(pokemon).sort()).toEqual(['bulbasaur', 'charmander', 'squirtle']);
  });

  it('should have the correct size of an array', function() {
    var noAnimals = [];
    var animals = ['cat', 'dog', 'horse', 'dolphin'];
    expect(Object.size(noAnimals)).toEqual(0);
    expect(Object.size(animals)).toEqual(4);
    expect(Object.size(pokemon)).toEqual(3);
  });
});

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

  it('should request solutions if selecting a task to view', inject(function() {
    // AJAX: tasklist.json
    $httpBackend.flush(1);

    // We expect the GET requests for the task's solutions
    // By using expect instead of when, it responds to a single request and the order matters
    $httpBackend.expect('GET', '/data/tasks/01Knapsack.json').respond(
      {solutions: {python: ['print', 'sys.stdout'], go: ['fmt.Println']}}
    );

    scope.taskSelector = '0/1-Knapsack';
    scope.retrieveTask();

    // AJAX: 01Knapsack.json
    $httpBackend.flush(1);
    expect(scope.selectedTask).toEqual('0/1-Knapsack');
    expect(scope.solutions).toEqual({python: ['print', 'sys.stdout'], go: ['fmt.Println']});
  }));
});
