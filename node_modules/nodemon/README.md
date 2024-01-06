<p align="center">
  <a href="https://nodemon.io/"><img src="https://user-images.githubusercontent.com/13700/35731649-652807e8-080e-11e8-88fd-1b2f6d553b2d.png" alt="Nodemon Logo"></a>
</p>

# nodemon

nodemon is a tool that helps develop Node.js based applications by automatically restarting the node application when file changes in the directory are detected.

nodemon does **not** require *any* additional changes to your code or method of development. nodemon is a replacement wrapper for `node`. To use `nodemon`, replace the word `node` on the command line when executing your script.

[![NPM version](https://badge.fury.io/js/nodemon.svg)](https://npmjs.org/package/nodemon)
[![Backers on Open Collective](https://opencollective.com/nodemon/backers/badge.svg)](#backers) [![Sponsors on Open Collective](https://opencollective.com/nodemon/sponsors/badge.svg)](#sponsors)

# Installation

Either through cloning with git or by using [npm](http://npmjs.org) (the recommended way):

```bash
npm install -g nodemon # or using yarn: yarn global add nodemon
```

And nodemon will be installed globally to your system path.

You can also install nodemon as a development dependency:

```bash
npm install --save-dev nodemon # or using yarn: yarn add nodemon -D
```

With a local installation, nodemon will not be available in your system path or you can't use it directly from the command line. Instead, the local installation of nodemon can be run by calling it from within an npm script (such as `npm start`) or using `npx nodemon`.

# Usage

nodemon wraps your application, so you can pass all the arguments you would normally pass to your app:

```bash
nodemon [your node app]
```

For CLI options, use the `-h` (or `--help`) argument:

```bash
nodemon -h
```

Using nodemon is simple, if my application accepted a host and port as the arguments, I would start it as so:

```bash
nodemon ./server.js localhost 8080
```

Any output from this script is prefixed with `[nodemon]`, otherwise all output from your application, errors included, will be echoed out as expected.

You can also pass the `inspect` flag to node through the command line as you would normally:

```bash
nodemon --inspect ./server.js 80
```

If you have a `package.json` file for your app, you can omit the main script entirely and nodemon will read the `package.json` for the `main` property and use that value as the app ([ref](https://github.com/remy/nodemon/issues/14)).

nodemon will also search for the `scripts.start` property in `package.json` (as of nodemon 1.1.x).

Also check out the [FAQ](https://github.com/remy/nodemon/blob/master/faq.md) or [issues](https://github.com/remy/nodemon/issues) for nodemon.

## Automatic re-running

nodemon was originally written to restart hanging processes such as web servers, but now supports apps that cleanly exit. If your script exits cleanly, nodemon will continue to monitor the directory (or directories) and restart the script if there are any changes.

## Manual restarting

Whilst nodemon is running, if you need to manually restart your application, instead of stopping and restart nodemon, you can type `rs` with a carriage return, and nodemon will restart your process.

## Config files

nodemon supports local and global configuration files. These are usually named `nodemon.json` and can be located in the current working directory or in your home directory. An alternative local configuration file can be specified with the `--config <file>` option.

The specificity is as follows, so that a command line argument will always override the config file settings:

- command line arguments
- local config
- global config

A config file can take any of the command line arguments as JSON key values, for example:

```json
{
  "verbose": true,
  "ignore": ["*.test.js", "**/fixtures/**"],
  "execMap": {
    "rb": "ruby",
    "pde": "processing --sketch={{pwd}} --run"
  }
}
```

The above `nodemon.json` file might be my global config so that I have support for ruby files and processing files, and I can run `nodemon demo.pde` and nodemon will automatically know how to run the script even though out of the box support for processing scripts.

A further example of options can be seen in [sample-nodemon.md](https://github.com/remy/nodemon/blob/master/doc/sample-nodemon.md)

### package.json

If you want to keep all your package configurations in one place, nodemon supports using `package.json` for configuration.
Specify the config in the same format as you would for a config file but under `nodemonConfig` in the `package.json` file, for example, take the following `package.json`:

```json
{
  "name": "nodemon",
  "homepage": "http://nodemon.io",
  "...": "... other standard package.json values",
  "nodemonConfig": {
    "ignore": ["**/test/**", "**/docs/**"],
    "delay": 2500
  }
}
```

Note that if you specify a `--config` file or provide a local `nodemon.json` any `package.json` config is ignored.

*This section needs better documentation, but for now you can also see `nodemon --help config` ([also here](https://github.com/remy/nodemon/blob/master/doc/cli/config.txt))*.

## Using nodemon as a module

Please see [doc/requireable.md](doc/requireable.md)

## Using nodemon as child process

Please see [doc/events.md](doc/events.md#Using_nodemon_as_child_process)

## Running non-node scripts

nodemon can also be used to execute and monitor other programs. nodemon will read the file extension of the script being run and monitor that extension instead of `.js` if there's no `nodemon.json`:

```bash
nodemon --exec "python -v" ./app.py
```

Now nodemon will run `app.py` with python in verbose mode (note that if you're not passing args to the exec program, you don't need the quotes), and look for new or modified files with the `.py` extension.

### Default executables

Using the `nodemon.json` config file, you can define your own default executables using the `execMap` property. This is particularly useful if you're working with a language that isn't supported by default by nodemon.

To add support for nodemon to know about the `.pl` extension (for Perl), the `nodemon.json` file would add:

```json
{
  "execMap": {
    "pl": "perl"
  }
}
```

Now running the following, nodemon will know to use `perl` as the executable:

```bash
nodemon script.pl
```

It's generally recommended to use the global `nodemon.json` to add your own `execMap` options. However, if there's a common default that's missing, this can be merged in to the project so that nodemon supports it by default, by changing [default.js](https://github.com/remy/nodemon/blob/master/lib/config/defaults.js) and sending a pull request.

## Monitoring multiple directories

By default nodemon monitors the current working directory. If you want to take control of that option, use the `--watch` option to add specific paths:

```bash
nodemon --watch app --watch libs app/server.js
```

Now nodemon will only restart if there are changes in the `./app` or `./libs` directory. By default nodemon will traverse sub-directories, so there's no need in explicitly including sub-directories.

Nodemon also supports unix globbing, e.g `--watch './lib/*'`. The globbing pattern must be quoted. For advanced globbing, [see `picomatch` documentation](https://github.com/micromatch/picomatch#advanced-globbing), the library that nodemon uses through `chokidar` (which in turn uses it through `anymatch`).

## Specifying extension watch list

By default, nodemon looks for files with the `.js`, `.mjs`, `.coffee`, `.litcoffee`, and `.json` extensions. If you use the `--exec` option and monitor `app.py` nodemon will monitor files with the extension of `.py`. However, you can specify your own list with the `-e` (or `--ext`) switch like so:

```bash
nodemon -e js,pug
```

Now nodemon will restart on any changes to files in the directory (or subdirectories) with the extensions `.js`, `.pug`.

## Ignoring files

By default, nodemon will only restart when a `.js` JavaScript file changes. In some cases you will want to ignore some specific files, directories or file patterns, to prevent nodemon from prematurely restarting your application.

This can be done via the command line:

```bash
nodemon --ignore lib/ --ignore tests/
```

Or specific files can be ignored:

```bash
nodemon --ignore lib/app.js
```

Patterns can also be ignored (but be sure to quote the arguments):

```bash
nodemon --ignore 'lib/*.js'
```

**Important** the ignore rules are patterns matched to the full absolute path, and this determines how many files are monitored. If using a wild card glob pattern, it needs to be used as `**` or omitted entirely. For example, `nodemon --ignore '**/test/**'` will work, whereas `--ignore '*/test/*'` will not.

Note that by default, nodemon will ignore the `.git`, `node_modules`, `bower_components`, `.nyc_output`, `coverage` and `.sass-cache` directories and *add* your ignored patterns to the list. If you want to indeed watch a directory like `node_modules`, you need to [override the underlying default ignore rules](https://github.com/remy/nodemon/blob/master/faq.md#overriding-the-underlying-default-ignore-rules).

## Application isn't restarting

In some networked environments (such as a container running nodemon reading across a mounted drive), you will need to use the `legacyWatch: true` which enables Chokidar's polling.

Via the CLI, use either `--legacy-watch` or `-L` for short:

```bash
nodemon -L
```

Though this should be a last resort as it will poll every file it can find.

## Delaying restarting

In some situations, you may want to wait until a number of files have changed. The timeout before checking for new file changes is 1 second. If you're uploading a number of files and it's taking some number of seconds, this could cause your app to restart multiple times unnecessarily.

To add an extra throttle, or delay restarting, use the `--delay` command:

```bash
nodemon --delay 10 server.js
```

For more precision, milliseconds can be specified.  Either as a float:

```bash
nodemon --delay 2.5 server.js
```

Or using the time specifier (ms):

```bash
nodemon --delay 2500ms server.js
```

The delay figure is number of seconds (or milliseconds, if specified) to delay before restarting. So nodemon will only restart your app the given number of seconds after the *last* file change.

If you are setting this value in `nodemon.json`, the value will always be interpreted in milliseconds. E.g., the following are equivalent:

```bash
nodemon --delay 2.5

{
  "delay": 2500
}
```

## Gracefully reloading down your script

It is possible to have nodemon send any signal that you specify to your application.

```bash
nodemon --signal SIGHUP server.js
```

Your application can handle the signal as follows.

```js
process.once("SIGHUP", function () {
  reloadSomeConfiguration();
})
```

Please note that nodemon will send this signal to every process in the process tree.

If you are using `cluster`, then each workers (as well as the master) will receive the signal. If you wish to terminate all workers on receiving a `SIGHUP`, a common pattern is to catch the `SIGHUP` in the master, and forward `SIGTERM` to all workers, while ensuring that all workers ignore `SIGHUP`.

```js
if (cluster.isMaster) {
  process.on("SIGHUP", function () {
    for (const worker of Object.values(cluster.workers)) {
      worker.process.kill("SIGTERM");
    }
  });
} else {
  process.on("SIGHUP", function() {})
}
```

## Controlling shutdown of your script

nodemon sends a kill signal to your application when it sees a file update. If you need to clean up on shutdown inside your script you can capture the kill signal and handle it yourself.

The following example will listen once for the `SIGUSR2` signal (used by nodemon to restart), run the clean up process and then kill itself for nodemon to continue control:

```js
process.once('SIGUSR2', function () {
  gracefulShutdown(function () {
    process.kill(process.pid, 'SIGUSR2');
  });
});
```

Note that the `process.kill` is *only* called once your shutdown jobs are complete. Hat tip to [Benjie Gillam](http://www.benjiegillam.com/2011/08/node-js-clean-restart-and-faster-development-with-nodemon/) for writing this technique up.

## Triggering events when nodemon state changes

If you want growl like notifications when nodemon restarts or to trigger an action when an event happens, then you can either `require` nodemon or add event actions to your `nodemon.json` file.

For example, to trigger a notification on a Mac when nodemon restarts, `nodemon.json` looks like this:

```json
{
  "events": {
    "restart": "osascript -e 'display notification \"app restarted\" with title \"nodemon\"'"
  }
}
```

A full list of available events is listed on the [event states wiki](https://github.com/remy/nodemon/wiki/Events#states). Note that you can bind to both states and messages.

## Pipe output to somewhere else

```js
nodemon({
  script: ...,
  stdout: false // important: this tells nodemon not to output to console
}).on('readable', function() { // the `readable` event indicates that data is ready to pick up
  this.stdout.pipe(fs.createWriteStream('output.txt'));
  this.stderr.pipe(fs.createWriteStream('err.txt'));
});
```

## Using nodemon in your gulp workflow

Check out the [gulp-nodemon](https://github.com/JacksonGariety/gulp-nodemon) plugin to integrate nodemon with the rest of your project's gulp workflow.

## Using nodemon in your Grunt workflow

Check out the [grunt-nodemon](https://github.com/ChrisWren/grunt-nodemon) plugin to integrate nodemon with the rest of your project's grunt workflow.

## Pronunciation

> nodemon, is it pronounced: node-mon, no-demon or node-e-mon (like pokémon)?

Well...I've been asked this many times before. I like that I've been asked this before. There's been bets as to which one it actually is.

The answer is simple, but possibly frustrating. I'm not saying (how I pronounce it). It's up to you to call it as you like. All answers are correct :)

## Design principles

- Fewer flags is better
- Works across all platforms
- Fewer features
- Let individuals build on top of nodemon
- Offer all CLI functionality as an API
- Contributions must have and pass tests

Nodemon is not perfect, and CLI arguments has sprawled beyond where I'm completely happy, but perhaps it can be reduced a little one day.

## FAQ

See the [FAQ](https://github.com/remy/nodemon/blob/master/faq.md) and please add your own questions if you think they would help others.

## Backers

Thank you to all [our backers](https://opencollective.com/nodemon#backer)! 🙏

[![nodemon backers](https://opencollective.com/nodemon/backers.svg?width=890)](https://opencollective.com/nodemon#backers)

## Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [Sponsor this project today ❤️](https://opencollective.com/nodemon#sponsor)

<div style="overflow: hidden; margin-bottom: 80px;"><!--oc--><a title='Netpositive' data-id='162674' href='https://najlepsibukmacherzy.pl/ranking-legalnych-bukmacherow/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/52acecf0-608a-11eb-b17f-5bca7c67fe7b.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='KasynoHEX' data-id='177376' href='https://polskiekasynohex.org/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/2bb0d6e0-99c8-11ea-9349-199aa0d5d24a.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Casinoonlineaams.com' data-id='198634' href='https://www.casinoonlineaams.com'><img alt='Casinoonlineaams.com' src='https://opencollective-production.s3.us-west-1.amazonaws.com/61bcf1d0-43ce-11ed-b562-6bf567fce1fd.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Aussielowdepositcasino' data-id='215800' href='https://aussielowdepositcasino.com/'><img alt='Best Aussie casinos at aussielowdepositcasino.com' src='https://user-images.githubusercontent.com/13700/151881982-04677f3d-e2e1-44ee-a168-258b242b1ef4.svg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Casino Wise' data-id='243140' href='https://casino-wise.com/'><img alt='Best online casinos not on GamStop in the UK' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/f889d209-a931-4c06-a529-fe1f86c411bf/casino-wise-logo.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='freebets.ltd.uk' data-id='269861' href='https://freebets.ltd.uk/'><img alt='freebets.ltd.uk' src='https://logo.clearbit.com/freebets.ltd.uk' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='TheCasinoDB' data-id='270835' href='https://www.thecasinodb.com'><img alt='null' src='https://logo.clearbit.com/thecasinodb.com' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Casino Utan Svenska Licensen' data-id='285700' href='https://www.casinoutansvenskalicensen.se/'><img alt='Marketing' src='https://opencollective-production.s3.us-west-1.amazonaws.com/ed105cb0-b01f-11ec-935f-77c14be20a90.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Online Casinos Australia' data-id='297999' href='https://online-casinosaustralia.com/'><img alt='Best Online Casino Guide in Australia' src='https://opencollective-production.s3.us-west-1.amazonaws.com/88bb6d20-900a-11ec-8a5a-a92310c15e5b.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Betting sites Australia' data-id='303335' href='https://hellsbet.com/en-au/'><img alt='Rating of best betting sites in Australia' src='https://opencollective-production.s3.us-west-1.amazonaws.com/aeb99e10-d1ec-11ec-88be-f9a15ca9f6f8.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='inkedin' data-id='305884' href='https://inkedin.com'><img alt='null' src='https://logo.clearbit.com/inkedin.com' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='AU Internet Pokies' data-id='318650' href='http://www.australiainternetpokies.com/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/44dc83f0-4315-11ed-9bf2-cf65326f4741.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='CasinoAus' data-id='318653' href='https://www.casinoaus.net/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/1e556300-4315-11ed-b96e-8dce3aa4cf2e.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='AU Online Casinos' data-id='318656' href='https://www.australiaonlinecasinosites.com/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/f3aa3b60-2219-11ed-b2b0-83767ea0d654.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Top Australian Gambling' data-id='318659' href='https://www.topaustraliangambling.com/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/d7687f70-2219-11ed-a0b5-97427086b4aa.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Casinostranieri.net' data-id='319480' href='https://www.casinostranieri.net/'><img alt='' src='https://opencollective-production.s3.us-west-1.amazonaws.com/7aae8900-0c02-11ed-9aa8-2bd811fd6f10.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Goread.io' data-id='320564' href='https://goread.io/buy-instagram-followers'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/7d1302a0-0f33-11ed-a094-3dca78aec7cd.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='SureBet' data-id='321121' href='https://www.sure.bet/casinos-not-on-gamstop/'><img alt='We are the most advanced casino guide!' src='https://logo.clearbit.com/sure.bet' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Correct Casinos Australia' data-id='322445' href='https://www.correctcasinos.com/australian-online-casinos/'><img alt='Best Australian online casinos. Reviewed by Correct Casinos.' src='https://opencollective-production.s3.us-west-1.amazonaws.com/fef95200-1551-11ed-ba3f-410c614877c8.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Casino utan svensk licens' data-id='326858' href='https://casinoburst.com/casino-utan-licens/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/ac61d790-1d3c-11ed-b8db-7b79b65b0dbb.PNG' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='uudetkasinot.com' data-id='326865' href='https://www.uudetkasinot.com'><img alt='' src='https://opencollective-production.s3.us-west-1.amazonaws.com/b6055950-df00-11eb-9caa-b58f40adecd5.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Gem M' data-id='327241' href='https://www.noneedtostudy.com/take-my-online-class/'><img alt='null' src='https://user-images.githubusercontent.com/13700/187039696-e2d8cd59-8b4e-438f-a052-69095212427d.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Slotmachineweb.com' data-id='329195' href='https://www.slotmachineweb.com/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/172f9eb0-22c2-11ed-a0b5-97427086b4aa.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Ghotala.com' data-id='342390' href='https://www.ghotala.com/'><img alt='Website dedicated to finding the best and safest licensed online casinos in India' src='https://opencollective-production.s3.us-west-1.amazonaws.com/75afa9e0-4ac6-11ed-8d6a-fdcc8c0d0736.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='CasinoWizard' data-id='344102' href='https://thecasinowizard.com/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/28b8d230-b9ab-11ec-8254-6d6dbd89fb51.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Scommesseseriea.eu' data-id='353466' href='https://www.scommesseseriea.eu/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/31600a10-4df4-11ed-a07e-95365d1687ba.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Gambe Online AU' data-id='356565' href='https://www.gambleonlineaustralia.com/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/a70354f0-337f-11ed-a5da-ebb8fe99a73a.JPG' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Gamble Online' data-id='356566' href='https://www.gambleonline.co'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/af336e80-337f-11ed-a5da-ebb8fe99a73a.JPG' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Italianonlinecasino.net' data-id='362210' href='https://www2.italianonlinecasino.net/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/2e8dbbb0-22bc-11ed-b874-23b20736a51e.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='nongamstopcasinos.net' data-id='367236' href='https://nongamstopcasinos.net/gb/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/fb8b5ba0-3904-11ed-8516-edd7b7687a36.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Scommesse777' data-id='370216' href='https://www.scommesse777.com/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/c0346cb0-7ad4-11ed-a9cf-49dc3536976e.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Twicsy' data-id='371088' href='https://twicsy.com/buy-instagram-likes'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/19bb95b0-7be3-11ed-8734-4d07568f9c95.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Casino Australia Online' data-id='380510' href='https://www.casinoaustraliaonline.com/under-1-hour-withdrawal-casinos/'><img alt='At Casinoaustraliaonline.com, we review, compare and list all the best gambling sites for Aussies.
' src='https://opencollective-production.s3.us-west-1.amazonaws.com/7c3d81f0-8cad-11ed-b048-95ec46716b47.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Casino Utan Svensk Licens' data-id='404959' href='https://coolspins.net/'><img alt='Casinon utan svensk licens erbjuder generösa bonusar och kampanjer. Besök coolspins.net för att utforska säkra och pålitliga alternativ.' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/3a988fb2-66a3-43f9-a0d1-65950128c68d/casino-utan-svensk-licens-open-collective.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='BestUSCasinos' data-id='409421' href='https://bestuscasinos.org'><img alt='null' src='https://logo.clearbit.com/bestuscasinos.org' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='TightPoker' data-id='410184' href='https://www.tightpoker.com/'><img alt='null' src='https://logo.clearbit.com/tightpoker.com' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Poprey.com' data-id='411448' href='https://poprey.com/'><img alt='Buy Instagram Likes' src='https://opencollective-production.s3.us-west-1.amazonaws.com/fe650970-c21c-11ec-a499-b55e54a794b4.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Casinot.biz' data-id='417601' href='https://www.casinot.biz/'><img alt='Find the best casinos online. Casinot.biz lists and reviews online casinos. ' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/366e3423-81af-484a-b9f8-eebe04224407/casinot-biz-icon.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='btcgaming' data-id='419934' href='https://bitcoinist.com/best-real-money-online-slots-play-slots-for-real-money/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/3ecded2c-a7c2-4291-b9ef-7db1f0128207/btcgaming.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Nettcasino' data-id='422431' href='https://www.nettcasino.com/'><img alt='Norway's biggest and most reliable online casino portal' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/5d739e1a-7813-489e-ab82-697daff8bf12/nettcasino.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Doctor Sports&Casinos - dr.sc' data-id='423396' href='https://dr.sc/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/dc0083f5-802f-4dd4-ace1-3c595d1f1659/open%20dr.sc.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='OnlineCasinosSpelen.com' data-id='423738' href='https://onlinecasinosspelen.com'><img alt='Online Casinos Spelen' src='https://logo.clearbit.com/onlinecasinosspelen.com' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Nieuwe-Casinos.net' data-id='424449' href='https://Nieuwe-Casinos.net'><img alt='Beoordelen van nieuwe online casino's 2023' src='https://logo.clearbit.com/Nieuwe-Casinos.net' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='CasinoZonderRegistratie.net' data-id='424450' href='https://casinoZonderregistratie.net/'><img alt='CasinoZonderRegistratie.net - Nederlandse Top Casino's' src='https://opencollective-production.s3.us-west-1.amazonaws.com/aeb624c0-7ae7-11ed-8d0e-bda59436695a.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='OnlineCasinoProfy' data-id='426813' href='https://onlinecasinoprofy.com/en/crypto/'><img alt='Onlinecasinoprofy is your guide to the world of gambling.' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/f8b0f6de-6ab5-4860-9688-709fe03873d3/2%201%20%282%29.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='OSLabs' data-id='427226' href='https://opensourcelabs.io'><img alt='OSLabs is a nonprofit tech accelerator devoted to furthering high-impact open source software within a collaborative community of dedicated engineers and mentors' src='https://opencollective-production.s3.us-west-1.amazonaws.com/dc95aaa0-823f-11ed-a97d-09a08de033e1.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Ilmaiset Pitkävetovihjeet' data-id='430701' href='https://www.vedonlyontibonukset.com/pitkavetovihjeet'><img alt='Ilmaiset Pitkävetovihjeet ' src='https://logo.clearbit.com/vedonlyontibonukset.com' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='NyeCasino' data-id='432409' href='https://www.nyecasino.me/'><img alt='NyeCasino.me is a website that lists the newest and best online casinos in Norway' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/20b616d7-bb05-4605-9904-6610a5d1e248/nyecasino200.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Famoid' data-id='434604' href='https://famoid.com/'><img alt='Famoid is a digital marketing agency that specializes in social media services and tools.' src='https://logo.clearbit.com/famoid.com' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='LookSlots' data-id='441291' href='https://www.outlookindia.com/outlook-spotlight/slots-not-on-gamstop-new-non-gamstop-casinos-uk-news-284058'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/d4c16601-f183-4239-9df6-eb2ade7a36f3/slots%20not%20on%20gamstop%20-%20non%20gamstop%20casinos.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Игровые автоматы' data-id='443264' href='https://slotoking.ua/games/'><img alt='Gives a fun for our users' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/94601d07-3205-4c60-9c2d-9b8194dbefb7/skg-blue.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='BairesDev' data-id='452424' href='https://www.bairesdev.com/sponsoring-open-source-projects/'><img alt='We are the leading Nearshore Technology Solutions company. We architect and engineer scalable and high-performing software solutions.' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/dc38bc3b-7430-4cf7-9b77-36467eb92915/logo8.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Buy Instagram Followers Twicsy' data-id='453050' href='https://twicsy.com/buy-instagram-followers'><img alt='Buy real Instagram followers from Twicsy starting at only $2.97. Twicsy has been voted the best site to buy followers from the likes of US Magazine.' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/eb3228cb-9810-42b0-9758-2a7aad5633ef/Screen%20Shot%202023-07-06%20at%209.08.54%20PM.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Buy Instagram Followers from SocialWick' data-id='462750' href='https://www.socialwick.com/instagram/followers'><img alt='SocialWick offers the best Instagram Followers in the market. If you are looking to boost your organic growth, buy Instagram followers from SocialWick' src='https://logo.clearbit.com/socialwick.com' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Online United States Casinos' data-id='466446' href='https://www.onlineunitedstatescasinos.com/'><img alt='null' src='https://logo.clearbit.com/onlineunitedstatescasinos.com' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Incognito' data-id='468969' href='https://bestnongamstopcasinos.net/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/1aec3bc6-2527-4a36-9c40-c2283454be76/cropped-logo1%20%281%29.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Aviators.com.br' data-id='471843' href='https://aviators.com.br'><img alt='O melhor jogo de aviação' src='https://github-production-user-asset-6210df.s3.amazonaws.com/13700/277616726-33b554c8-24e0-4570-b8ed-293fb2ab2448.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='CasinoHEX Phillipines' data-id='473786' href='https://onlinecasinohex.ph/'><img alt='Online iGaming platform with reliable and trusted reviews.' src='https://opencollective-production.s3.us-west-1.amazonaws.com/b19cbf10-3a5e-11ed-9713-c7c7fc5beda8.svg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='SlotCasinoCanada' data-id='480605' href='https://slotcasinocanada.ca/casinos/casino-1-dollar/'><img alt='$1 deposit casino' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/3df9dabb-86ff-4f2e-8edd-f195b55a8555/scc%20logo_600x600.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='null' data-id='Online Casinos Australia' href='https://online-casinosaustralia.com/'><img alt='Online Casinos Australia' src='https://github-production-user-asset-6210df.s3.amazonaws.com/13700/268531585-c2b4e482-0409-4664-9aa2-95a62b0d606d.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Views4You' data-id='493616' href='https://views4you.com/buy-youtube-subscribers/'><img alt='Looking to boost your YouTube channel? Buy YouTube subscribers with Views4You and watch your audience grow!' src='https://logo.clearbit.com/views4you.com' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='casinosonlineaus' data-id='495874' href='https://casinosonlineaus.com/'><img alt='null' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/7fb69094-c265-4275-b295-faf6cc0c5372/imgonline-com-ua-Resize-YkHndKrIwMdOKZAz.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='LeafletCasino' data-id='499738' href='https://leafletcasino.com/online-casino/best-payout/'><img alt='Check out highest payout online casinos in Canada at leafletcasino.com' src='https://opencollective-production.s3.us-west-1.amazonaws.com/4f4c1b90-6183-11eb-8d33-bbbffb3655c5.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Thebestsolution' data-id='501897' href='https://buycheapestfollowers.com/buy-telegram-channel-members'><img alt='Services to make the world a better place' src='https://github-production-user-asset-6210df.s3.amazonaws.com/13700/286696172-747dca05-a1e8-4d93-a9e9-95054d1566df.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Kasinoceske.com' data-id='504161' href='https://kasinoceske.com'><img alt='Najděte nejlepší online casino v České republice' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/e6056d09-1db2-4fde-ae54-4cee5d99f32e/CZ.png' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='CasinoLandia.com' data-id='504258' href='https://casinolandia.com'><img alt='We review the entire iGaming industry from A to Z' src='https://opencollective-production.s3.us-west-1.amazonaws.com/account-avatar/5f858add-77f1-47a2-b577-39eecb299c8c/Logo264.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='Casino Utan Svensk Licens' data-id='506063' href='https://casino-utan-svensk-licens.com/'><img alt='Helping Swedes finding safe unlicensed casinos' src='https://logo.clearbit.com/casino-utan-svensk-licens.com' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a>
<a title='null' data-id='slotozilla' href='https://www.slotozilla.com/au/free-spins'><img alt='free spins no deposit' src='https://github-production-user-asset-6210df.s3.amazonaws.com/13700/286693953-c68112b6-ebe6-49fd-af6a-5c810a54908d.jpg' style='object-fit: contain; float: left; margin:12px' height='120' width='120'></a><!--oc-->
</div>

Please note that links to the sponsors above are not direct endorsements nor affiliated with any of contributors of the nodemon project.

# License

MIT [http://rem.mit-license.org](http://rem.mit-license.org)
