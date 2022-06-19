function sentenceCounter(str) {
    const problematicFragmentsDict = ['Mr. ', 'Mrs. ', 'Ms. ', 'Dr. ']; // Problematic fragments, change if needed to remove more
    const suffixDict = ['.', '!', '?']; // Suffixes, change if needed to count more
    var sentence = str
    var sentenceCount = 0;

    problematicFragmentsDict.forEach(fragment => {
        sentence = sentence.replace(fragment, '');
    });

    suffixDict.forEach(element => {
        sentenceCount += (sentence.match(new RegExp("\\" + element + "\\s", "g")) || []).length // Use Regex to count the number of occurrences of the suffix
        if (sentence.endsWith(element)) {
            sentenceCount += 1; // Add one for the last sentence
        }
    });

    

  return sentenceCount;
}

console.log(sentenceCounter("Mr. Smith went to get an X-Ray from Dr. Jones and was charged $99.99."))