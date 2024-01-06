
Configuration
  --config <file> .......... alternate nodemon.json config file to use
  --exitcrash .............. exit on crash, allows nodemon to work with other watchers
  -i, --ignore ............. ignore specific files or directories
  --no-colors .............. disable color output
  --signal <signal> ........ use specified kill signal instead of default (ex. SIGTERM)
  -w, --watch path ......... watch directory "dir" or files. use once for each
                             directory or file to watch
  --no-update-notifier ..... opt-out of update version check

Execution
  -C, --on-change-only ..... execute script on change only, not startup
  --cwd <dir> .............. change into <dir> before running the script
  -e, --ext ................ extensions to look for, ie. "js,pug,hbs"
  -I, --no-stdin ........... nodemon passes stdin directly to child process
  --spawn .................. force nodemon to use spawn (over fork) [node only]
  -x, --exec app ........... execute script with "app", ie. -x "python -v"
  -- <your args> ........... to tell nodemon stop slurping arguments

Watching
  -d, --delay n ............ debounce restart for "n" seconds
  -L, --legacy-watch ....... use polling to watch for changes (typically needed
                             when watching over a network/Docker)
  -P, --polling-interval ... combined with -L, milliseconds to poll for (default 100)

Information
  --dump ................... print full debug configuration
  -h, --help ............... default help
  --help <topic> ........... help on a specific feature. Try "--help topics"
  -q, --quiet .............. minimise nodemon messages to start/stop only
  -v, --version ............ current nodemon version
  -V, --verbose ............ show detail on what is causing restarts


> Note that any unrecognised arguments are passed to the executing command.
