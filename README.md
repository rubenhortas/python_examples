# python examples
Small examples of Python3 code, data structures and algorithms.

## Python naming conventions
### Public elements

| Public element  | Notation                    | Example      | Notes                                                                     |
|-----------------|-----------------------------|--------------|---------------------------------------------------------------------------|
| Class           | PascalCase (UpperCamelCase) | MyClass      |                                                                           |
| Constant        | SCREAMING_SNAKE_CASE        | MY_CONSTANT  | Uppercase single letter, word, or words. Separate words with underscores. |
| Function/Method | snake_case                  | my_function  | Lowercase word or words. Separate words by underscores.                   |
| Module          | snake_case                  | my_module.py | Short. Lowercase word or words. Separate words with underscores.          |
| Package         | lowercase                   | mypackage.py | Short. Lowercase word or words. Do not separate words with underscores.   |
| Variable        | snake_case                  | my_variable  | Lowercase single letter, word, or words. Separate words with underscores. |

### Private elements

| Private element | Notation   | Example                     | Notes                        |
|-----------------|------------|-----------------------------|------------------------------|
| Class Method    | snake_case | \_\_my_private_class_method | Starts with two underscores. |
| Function/Method | snake_case | \_my_private_function       | Starts with one underscore.  |

### Comments

* Should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a lower case letter.
* Block comments generally consist of one or more paragraphs built out of complete sentences, with each sentence ending in a period.
* Use two spaces after a sentence-ending period in multi-sentence comments except after the final sentence.
  * ### Block Comments
    Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).  
    Paragraphs inside a block comment are separated by a line containing a single #. 
    
    ```python
    # Use this function to check code quality. 
    # Code quality is defined by the following parameters: 
    # - The code follows naming conventions
    # - The code is easy to understand
    # - ...
    def check_code_quality(code):
    ```
    
  * ### Inline Comments
    Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.
    
    ```python
    if len(commits) > 0:  # Make sure that there is commits
    ```

### Documentation strings

* Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the def line.
* The """ that ends a multiline docstring should be on a line by itself.
  
  ```python
  def draw_circle():
  """
  Returns a circle
  Draws a circle.
  """
  ```
* For one liner docstrings keep the closing """ on the same line:  
  ```python
  """Returns a circle."""
  ```

## Sources

* [PEP 8](https://peps.python.org/pep-0008/)

## Support
If you find these examples useful you can star this repo.
