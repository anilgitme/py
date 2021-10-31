var reverseWords = function(s) {
    let words = s.split(' ');
    let rev_words = [];

    for (let i = words.length - 1; i >= 0; i--) {
        if (words[i] !== '') {
            rev_words.push(words[i])
        }
    };

    return rev_words.join(' ');
};


console.log(reverseWords('the sky is blue'))
console.log(reverseWords('      the sky is blue      '))