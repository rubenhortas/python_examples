from pathlib import Path

from textblob import TextBlob
from textblob.exceptions import TranslatorError

ENCODING = "UTF-8"
DECIMAL_NUMBERS = 2

if __name__ == "__main__":
    input_path = Path("input.txt")
    results_path = Path("results.txt")

    try:
        with (
            input_path.open(encoding=ENCODING) as input_file,
            results_path.open("w+", encoding=ENCODING) as results_file,
        ):
            results_file.write("line,polarity,subjectivity\n")

            for line in input_file:
                clean_line = line.rstrip("\n")

                if not clean_line:
                    continue

                analysis = TextBlob(clean_line)
                line_polarity = round(analysis.polarity, DECIMAL_NUMBERS)
                line_subjectivity = round(analysis.subjectivity, DECIMAL_NUMBERS)

                results_file.write(f"{clean_line},{line_polarity},{line_subjectivity}\n")
    except TranslatorError:
        pass
    except Exception as e:
        print(f"Unexpected error: {e}")
