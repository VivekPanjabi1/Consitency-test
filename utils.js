function add(a, b) {
  return a + b;
}

function getData(items = []) {
  const result = [];
  for (let i = 0; i < items.length; i++) {
    if (items[i] === null) {
      continue;
    }
    result.push(items[i]);
  }
  return result;
}

console.log(add(5, 10));
