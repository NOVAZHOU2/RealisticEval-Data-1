/* function created using chatGPT */
function setEurValue(value) {
    if (value === '' || value === null) return '';
    let number = parseInt(value);
    if (isNaN(number)) return '';
    if (number >= 1000000) {
        return (number / 1000000).toFixed(1) + 'm';
    } else if (number >= 1000) {
        return (number / 1000).toFixed(1) + 'k';
    } else {
        return number.toString();
    }
}
