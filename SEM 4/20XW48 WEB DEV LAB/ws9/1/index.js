function combSort (inputArray){
    if(inputArray.length < 2) return inputArray
    // let swapped
    let gap = inputArray.length
    do{
        gap = gap > 1 ? Math.floor(gap / 1.5) : 1
        // swapped = false
        for(let i =0; i+gap<inputArray.length; i++){
            if(inputArray[i] > inputArray[i+gap]){
                let temp = inputArray[i]
                inputArray[i] = inputArray[i+gap]
                inputArray[i+gap] = temp
                // swapped = true
            }
        }
    } while ( gap > 1)
    return inputArray
}
const unsortedArray=[3,2,1]
console.log(combSort(unsortedArray));