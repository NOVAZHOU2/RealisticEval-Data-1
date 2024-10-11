function printMemoryBits(memorySection) {
    for (let byte of memorySection) {
        let bits = '';
        for (let i = 7; i >= 0; i--) {
            bits += (byte >> i) & 1;
        }
        console.log(bits);
    }
}