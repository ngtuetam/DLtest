// Problem:
// https://www.hackerrank.com/challenges/js10-try-catch-and-finally/problem?isFullScreen=true

function reverseString(s) {
    try {
        let reversed= s.split("").reverse().join("");
        console.log(reversed);
}
catch(err) {
    console.log(err.message);
    console.log(s);
  
}
finally {
  
}
}


function main() {
    const s = eval(readLine());
    
    reverseString(s);
}