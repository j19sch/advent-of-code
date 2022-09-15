import {readFileOfNumbers} from './read-file';

console.log("day 01, puzzle 01!");

// ex_arr.forEach(function (entry) {
//     console.log(entry);
//   });

function findMatch (input_arr: Array<number>): Array<number|undefined> {
    let numb1: number | undefined = undefined
    let numb2: number | undefined = undefined

    const sum: number = 2020  // const and implicitly typed, so no need to do explicitly?

    for (let item of input_arr) {
        let needed: number = sum - item;
        
        if (input_arr.includes(needed)) {
            // console.log('found: ', needed, item)
            numb1 = item;
            numb2 = needed;
            break;
        }
    }
    if (numb1 === numb2) {console.log(`how many ${sum / 2}s?`)};
    return [numb1, numb2]
}

const ex_arr: Array<number> = [1721, 979, 366, 299, 675, 1456] //514579
let [n1, n2]: Array<number|undefined> = findMatch(ex_arr)

if (n1 != undefined && n2 != undefined) {
    console.log(n1 * n2);
}

const inp_array: Array<number> = readFileOfNumbers('./2020/day01-input.txt'); // 793524

[n1, n2] = findMatch(inp_array)

if (n1 != undefined && n2 != undefined) {
    console.log(n1 * n2);
}
