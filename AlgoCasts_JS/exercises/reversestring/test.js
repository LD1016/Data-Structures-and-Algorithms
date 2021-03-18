const reverse = require('./index');

test('Reverse function exists', () => {
  expect(reverse).toBeDefined();
});

test('Reverse reverse a string', () => {
  expect(reverse('abcd')).toEqual('dcba');
});

test('Reverse reverse a string', () => {
  expect(reverse('abcd   ')).toEqual('   dcba');
});
