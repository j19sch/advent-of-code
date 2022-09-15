import * as fs from 'fs';

export function readFileOfNumbers(fileLocation: string): Array<number> {
    const inputFile: Buffer = fs.readFileSync(fileLocation);
    const inp_array: Array<number> = inputFile.toString().split("\n").map(Number);
    return inp_array;
}
