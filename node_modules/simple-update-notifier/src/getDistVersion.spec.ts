import Stream from 'stream';
import https from 'https';
import getDistVersion from './getDistVersion';

jest.mock('https', () => ({
  get: jest.fn(),
}));

test('Valid response returns version', async () => {
  const st = new Stream();
  (https.get as jest.Mock).mockImplementation((url, cb) => {
    cb(st);

    st.emit('data', '{"latest":"1.0.0"}');
    st.emit('end');
  });

  const version = await getDistVersion('test', 'latest');

  expect(version).toEqual('1.0.0');
});

test('Invalid response throws error', async () => {
  const st = new Stream();
  (https.get as jest.Mock).mockImplementation((url, cb) => {
    cb(st);

    st.emit('data', 'some invalid json');
    st.emit('end');
  });

  expect(getDistVersion('test', 'latest')).rejects.toThrow(
    'Could not parse version response'
  );
});
