from textblob import TextBlob
from textblob.exceptions import TranslatorError

ENCODING = 'UTF-8'
DECIMAL_NUMBERS = 2

if __name__ == '__main__':
    input_ = open('input.txt', 'r', encoding=ENCODING)
    results = open('results.txt', 'w+', encoding=ENCODING)
    results.write('line,polarity,subjectivity\n')

    for line in input_.read().split('\n'):
        try:
            analysis = TextBlob(line)

            line_polarity = round(analysis.polarity, DECIMAL_NUMBERS)
            line_subjectivity = round(analysis.subjectivity, DECIMAL_NUMBERS)

            results.write(f"{line},{line_polarity},{line_subjectivity}\n")
        except TranslatorError as translator_exception:
            pass
        except Exception as e:
            print(e)
