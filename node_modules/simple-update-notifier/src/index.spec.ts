import simpleUpdateNotifier from '.';
import hasNewVersion from './hasNewVersion';

const consoleSpy = jest.spyOn(console, 'error');

jest.mock('./hasNewVersion', () => jest.fn().mockResolvedValue('2.0.0'));

beforeEach(jest.clearAllMocks);

test('it logs message if update is available', async () => {
  await simpleUpdateNotifier({
    pkg: { name: 'test', version: '1.0.0' },
    alwaysRun: true,
  });

  expect(consoleSpy).toHaveBeenCalledTimes(1);
});

test('it does not log message if update is not available', async () => {
  (hasNewVersion as jest.Mock).mockResolvedValue(false);
  await simpleUpdateNotifier({
    pkg: { name: 'test', version: '2.0.0' },
    alwaysRun: true,
  });

  expect(consoleSpy).toHaveBeenCalledTimes(0);
});
