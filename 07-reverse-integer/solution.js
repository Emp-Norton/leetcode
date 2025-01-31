
var reverse = function(x) {
    const MAX=2147483648;

    const stringified = x.toString();

    let signed = stringified[0] == '-'; // stringified.length == parseInt(x).length
    let val = '';
    for (let i = stringified.length - 1; i >= 0; i--) {
        val += stringified[i];
    }


    val = parseInt(val);
    if (val > MAX) return 0

    return signed ? val * -1 : val
};
