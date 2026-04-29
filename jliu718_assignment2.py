import sys
import re
import string


def cleanFileContents(f):
    with open(f, 'r', encoding='utf-8') as f:
        text = f.read()

    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    clean_text = re.sub(r'\s+', ' ', clean_text)

    return clean_text


def countTokens(text):
    token_counts = {}
    tokens = text.split()

    for token in tokens:
        if token not in token_counts:
            token_counts[token] = 0
        token_counts[token] += 1

    return token_counts


POS_REVIEW = "POSITIVE"
NEG_REVIEW = "NEGATIVE"
NONE = "NONE"
POS = 'good'
NEG = 'bad'


def predictSimplistic(counts):
    pos_count = counts.get(POS, 0)
    neg_count = counts.get(NEG, 0)

    if pos_count > neg_count:
        return POS_REVIEW
    elif neg_count > pos_count:
        return NEG_REVIEW
    else:
        return NONE


def main(argv):
    filename = argv[1]
    clean_text = cleanFileContents(filename)
    tokens_with_counts = countTokens(clean_text)
    prediction = predictSimplistic(tokens_with_counts)
    print("The prediction for file {} is {}".format(filename, prediction))


if __name__ == "__main__":
    main(sys.argv)
