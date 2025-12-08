# python examples

A collection of Python examples, including Data Structures and Algorithms (DSA).

![GitHub repo file count](https://img.shields.io/github/directory-file-count/rubenhortas/python_examples)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rubenhortas/python_examples)
![GitHub repo size](https://img.shields.io/github/repo-size/rubenhortas/python_examples)

![GitHub issues](https://img.shields.io/github/issues-raw/rubenhortas/python_examples?logo=github)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/rubenhortas/python_examples?logo=github)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/rubenhortas/python_examples?&logo=github)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/rubenhortas/python_examples?logo=github)

![GitHub](https://img.shields.io/github/license/rubenhortas/python_examples)

## Python naming conventions

### Public elements

| Type            | Notation                    | Example       | Notes                                                                             |
|-----------------|-----------------------------|---------------|-----------------------------------------------------------------------------------|
| Class           | PascalCase (UpperCamelCase) | MyClass       |                                                                                   |
| Constant        | SCREAMING_SNAKE_CASE        | MY_CONSTANT   | Uppercase single letter, word, or words. Separate words with underscores.         |
| Enum values     | SCREAMING_SNAKE_CASE        | SOME_ENUM     |                                                                                   |
| Exception       | PascalCase (UpperCamelCase) | MyException   |                                                                                   |
| Function/Method | snake_case                  | my_function() | Lowercase word or words. Separate words by underscores.                           |
| Module          | snake_case                  | my_module.py  | Short. Lowercase word or words.  Underscores can be used if improves readability. |
| Package         | lowercase                   | mypackage     | Short. Lowercase word or words. The use of underscores is discouraged.            |
| Variable        | snake_case                  | my_variable   | Lowercase single letter, word, or words. Separate words with underscores.         |

### Private elements

No attribute is really private in Python (without a generally unnecessary amount of work), but there are conventions:

| Convention                  | Meaning                      | Use                                                                                           |
|-----------------------------|------------------------------|-----------------------------------------------------------------------------------------------|
| _single_leading_underscore  | Weak internal use indicator. | The object is meant to be private, and shouldn't be directly accessed from outside the class. |
| __double_leading_underscore | Invokes name mangling.       | A way to make instance variables less likely to collide with variables in subclasses.         |

### Comments

* Should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a
  lower case letter.
* Block comments generally consist of one or more paragraphs built out of complete sentences, with each sentence ending
  in a period.
* Use two spaces after a sentence-ending period in multi-sentence comments except after the final sentence.
    * ### Block Comments
      Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that
      code.
      Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).  
      Paragraphs inside a block comment are separated by a line containing a single #.

      ```python
      # Use this function to check code quality. 
      # Code quality is defined by the following parameters: 
      # - The code follows naming conventions
      # - The code is easy to understand
      # - ...
      def check_code_quality(code):
        ...
      ```

    * ### Inline Comments
      Inline comments should be separated by at least two spaces from the statement. They should start with a # and a
      single space.

      ```python
      if len(commits) > 0:  # Make sure that there is commits
        ...
      ```

### Documentation strings

* Write docstrings for all public modules, functions, classes, and methods.
  A docstring is the first statement in a package, module, class or function.
  Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method
  does.
  * The """ that ends a multiline docstring should be on a line by itself.

    ```python
    def draw_circle():
        """
        Returns a circle
        Draws a circle.
        """
        ...
    ```
* For one-liner docstrings keep the closing """ on the same line:
  ```python
  """Returns a circle."""
  ```

## Python file format

  1. Hashbang
  2. Docstrings
  3. Imports
  4. Code

## Sources

* [PEP 8](https://peps.python.org/pep-0008)
* [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

## Support

If you find these examples useful, please consider starring this repository!
