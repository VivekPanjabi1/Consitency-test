function Add(a, b) {
  return a + b;
}

function getData(items = []) {
  let result = [];
  for (let i = 0; i < items.length; i++) {
    if (items[i] === null) {
      continue;
    }
    result.push(items[i]);
  }
  return result;
}

console.log(Add(5, 10));
