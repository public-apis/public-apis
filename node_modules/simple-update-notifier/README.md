# simple-update-notifier [![GitHub stars](https://img.shields.io/github/stars/alexbrazier/simple-update-notifier?label=Star%20Project&style=social)](https://github.com/alexbrazier/simple-update-notifier/stargazers)

[![CI](https://github.com/alexbrazier/simple-update-notifier/workflows/Build%20and%20Deploy/badge.svg)](https://github.com/alexbrazier/simple-update-notifier/actions)
[![Dependencies](https://img.shields.io/librariesio/release/npm/simple-update-notifier)](https://www.npmjs.com/package/simple-update-notifier?activeTab=dependencies)
[![npm](https://img.shields.io/npm/v/simple-update-notifier)](https://www.npmjs.com/package/simple-update-notifier)
[![npm bundle size](https://img.shields.io/bundlephobia/min/simple-update-notifier)](https://bundlephobia.com/result?p=simple-update-notifier)
[![npm downloads](https://img.shields.io/npm/dw/simple-update-notifier)](https://www.npmjs.com/package/simple-update-notifier)
[![License](https://img.shields.io/npm/l/simple-update-notifier)](./LICENSE)

Simple update notifier to check for npm updates for cli applications.

<img src="./.github/demo.png" alt="Demo in terminal showing an update is required">

Checks for updates for an npm module and outputs to the command line if there is one available. The result is cached for the specified time so it doesn't check every time the app runs.

## Install

```bash
npm install simple-update-notifier
OR
yarn add simple-update-notifier
```

## Usage

```js
import updateNotifier from 'simple-update-notifier';
import packageJson from './package.json' assert { type: 'json' };

updateNotifier({ pkg: packageJson });
```

### Options

#### pkg

Type: `object`

##### name

_Required_\
Type: `string`

##### version

_Required_\
Type: `string`

#### updateCheckInterval

Type: `number`\
Default: `1000 * 60 * 60 * 24` _(1 day)_

How often to check for updates.

#### shouldNotifyInNpmScript

Type: `boolean`\
Default: `false`

Allows notification to be shown when running as an npm script.

#### distTag

Type: `string`\
Default: `'latest'`

Which [dist-tag](https://docs.npmjs.com/adding-dist-tags-to-packages) to use to find the latest version.

#### alwaysRun

Type: `boolean`\
Default: `false`

When set, `updateCheckInterval` will not be respected and a check for an update will always be performed.

#### debug

Type: `boolean`\
Default: `false`

When set, logs explaining the decision will be output to `stderr` whenever the module opts to not print an update notification
