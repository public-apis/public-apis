# pstree.remy

> Cross platform ps-tree (including unix flavours without ps)

## Installation

```shel
npm install pstree.remy
```

## Usage

```js
const psTree = psTree require('pstree.remy');

psTree(PID, (err, pids) => {
  if (err) {
    console.error(err);
  }
  console.log(pids)
});

console.log(psTree.hasPS
  ? "This platform has the ps shell command"
  : "This platform does not have the ps shell command");
```
