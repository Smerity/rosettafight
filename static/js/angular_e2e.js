'use strict';

describe('RosettaFight E2E Test', function() {
  beforeEach(function() {
    browser().navigateTo('/');
  });

  it('should have RosettaFight in the name', function() {
    expect(element('h2').text()).toEqual('Rosetta Fight');
  });

  it('should correct show task description', function() {
    select('taskSelector').option('100 doors');
    element('#taskSelectorArea button').click();
    expect(element('#taskDescription').text()).toContain('100 doors');
    expect(element('#taskDescription').text()).toContain('156 languages');
  });
});
