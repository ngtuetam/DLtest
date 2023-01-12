/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    let first =  -1;
    let second = -1;
    let n = nums.length
    if (n<2) {
        return;
    }

    for (let i=0;i<n;i++){
        if (nums[i] > first){
            second = first;
            first = nums[i];
        }

        else if (nums[i] > second && nums[i] != first){
            second = nums[i];
        }
    }
    if (second == -1){
        reuturn;
    }
    else {
        return second;
    }
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}