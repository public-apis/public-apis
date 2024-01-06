const spawn = require('child_process').spawn;
function run() {
  spawn(
    'sh',
    ['-c', 'node -e "setInterval(() => console.log(`running`), 200)"'],
    {
      stdio: 'pipe',
    }
  );
}

var runCallCount = process.argv[2] || 1;
for (var i = 0; i < runCallCount; i++) run();
