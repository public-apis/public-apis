type AnymatchFn = (testString: string) => boolean;
type AnymatchPattern = string|RegExp|AnymatchFn;
type AnymatchMatcher = AnymatchPattern|AnymatchPattern[]
type AnymatchTester = {
  (testString: string|any[], returnIndex: true): number;
  (testString: string|any[]): boolean;
}

type PicomatchOptions = {dot: boolean};

declare const anymatch: {
  (matchers: AnymatchMatcher): AnymatchTester;
  (matchers: AnymatchMatcher, testString: null, returnIndex: true | PicomatchOptions): AnymatchTester;
  (matchers: AnymatchMatcher, testString: string|any[], returnIndex: true | PicomatchOptions): number;
  (matchers: AnymatchMatcher, testString: string|any[]): boolean;
}

export {AnymatchMatcher as Matcher}
export {AnymatchTester as Tester}
export default anymatch
