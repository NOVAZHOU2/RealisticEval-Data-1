function shellSort(arr) {
    const n = arr.length;

    // Start with a large gap, then reduce the gap
    for (let gap = Math.floor(n / 2); gap > 0; gap = Math.floor(gap / 2)) {
        // Perform a gapped insertion sort
        for (let i = gap; i < n; i++) {
            const temp = arr[i];

            // Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            let j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }

            // Put temp (the original arr[i]) in its correct location
            arr[j] = temp;
        }
    }
}

// Function to print an array
function printArray(arr) {
    console.log(arr.join(' '));
}