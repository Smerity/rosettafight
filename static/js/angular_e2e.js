'use strict';

describe('RosettaFight E2E Test', function() {
  beforeEach(function() {
    browser().navigateTo('/');
  });

  it('should have RosettaFight in the name', function() {
    expect(element('h2').text()).toEqual('Rosetta Fight');
  });

  it('should correctly show task description', function() {
    select('taskSelector').option('100 doors');
    element('#taskSelectorArea button').click();
    expect(element('#taskDescription').text()).toContain('100 doors');
    expect(element('#taskDescription').text()).toContain('156 languages');
  });

  it('should load a different language', function() {
    select('taskSelector').option('Hello world/Text');
    element('#taskSelectorArea button').click();
    // This test will fail due to a bug I've found in Angular Scenario's DSL for select-option
    // Sending pull request to resolve this issue -- but my test is correct!
    select('lang').option('c');
    // Ensure escaping works properly -- should have escaped #include <stdlib.h>
    expect(element('pre.prettyprint:first').html()).toContain('&lt;stdlib.h&gt;');
  });

  it('should allow selecting a different solution', function() {
    select('taskSelector').option('100 doors');
    element('#taskSelectorArea button').click();
    expect(element('#code-0 li.active').count()).toBe(1);
    // TODO: Ensure that eq(0).hasClass(active), change to element #1, repeat test
  });
});
