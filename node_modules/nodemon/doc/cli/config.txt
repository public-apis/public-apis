
  Typically the options to control nodemon are passed in via the CLI and are
  listed under: nodemon --help options

  nodemon can also be configured via a local and global config file:

  * $HOME/nodemon.json
  * $PWD/nodemon.json OR --config <file>
  * nodemonConfig in package.json

  All config options in the .json file map 1-to-1 with the CLI options, so a
  config could read as:

    {
      "ext": "*.pde",
      "verbose": true,
      "exec": "processing --sketch=game --run"
    }

  There are a limited number of variables available in the config (since you
  could use backticks on the CLI to use a variable, backticks won't work in
  the .json config).

  * {{pwd}} - the current directory
  * {{filename}} - the filename you pass to nodemon

  For example:

    {
      "ext": "*.pde",
      "verbose": true,
      "exec": "processing --sketch={{pwd}} --run"
    }

  The global config file is useful for setting up default executables
  instead of repeating the same option in each of your local configs:

    {
      "verbose": true,
      "execMap": {
        "rb": "ruby",
        "pde": "processing --sketch={{pwd}} --run"
      }
    }
