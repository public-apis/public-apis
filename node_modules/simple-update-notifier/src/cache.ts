import os from 'os';
import path from 'path';
import fs from 'fs';

const homeDirectory = os.homedir();
const configDir =
  process.env.XDG_CONFIG_HOME ||
  path.join(homeDirectory, '.config', 'simple-update-notifier');

const getConfigFile = (packageName: string) => {
  return path.join(
    configDir,
    `${packageName.replace('@', '').replace('/', '__')}.json`
  );
};

export const createConfigDir = () => {
  if (!fs.existsSync(configDir)) {
    fs.mkdirSync(configDir, { recursive: true });
  }
};

export const getLastUpdate = (packageName: string) => {
  const configFile = getConfigFile(packageName);

  try {
    if (!fs.existsSync(configFile)) {
      return undefined;
    }
    const file = JSON.parse(fs.readFileSync(configFile, 'utf8'));
    return file.lastUpdateCheck as number;
  } catch {
    return undefined;
  }
};

export const saveLastUpdate = (packageName: string) => {
  const configFile = getConfigFile(packageName);

  fs.writeFileSync(
    configFile,
    JSON.stringify({ lastUpdateCheck: new Date().getTime() })
  );
};
