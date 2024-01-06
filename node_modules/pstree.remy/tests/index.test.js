const tap = require('tap');
const test = tap.test;
const readFile = require('fs').readFileSync;
const spawn = require('child_process').spawn;
const pstree = require('../');
const { tree, pidsForTree, getStat } = require('../lib/utils');

if (process.platform !== 'darwin') {
  test('reads from /proc', async (t) => {
    const ps = await getStat();
    t.ok(ps.split('\n').length > 1);
  });
}

test('tree for live env', async (t) => {
  const pid = 4079;
  const fixture = readFile(__dirname + '/fixtures/out2', 'utf8');
  const ps = await tree(fixture);
  t.deepEqual(
    pidsForTree(ps, pid).map((_) => _.PID),
    ['4080']
  );
});

function testTree(t, runCallCount) {
  const sub = spawn('node', [`${__dirname}/fixtures/index.js`, runCallCount], {
    stdio: 'pipe',
  });
  setTimeout(() => {
    const pid = sub.pid;

    pstree(pid, (error, pids) => {
      pids.concat([pid]).forEach((p) => {
        spawn('kill', ['-s', 'SIGTERM', p]);
      });

      // the fixture launches `sh` which launches node which is why we
      // are looking for two processes.
      // Important: IDKW but MacOS seems to skip the `sh` process. no idea.
      t.equal(pids.length, runCallCount * 2);
      t.end();
    });
  }, 1000);
}

test('can read full process tree', (t) => {
  testTree(t, 1);
});
test('can read full process tree with multiple processes', (t) => {
  testTree(t, 2);
});
