# Public elements

| Public element  | Notation                    | Example      | Notes                                                                     |
|-----------------|-----------------------------|--------------|---------------------------------------------------------------------------|
| Class           | PascalCase (UpperCamelCase) | MyClass      |                                                                           |
| Constant        | SCREAMING_SNAKE_CASE        | MY_CONSTANT  | Uppercase single letter, word, or words. Separate words with underscores. |
| Function/Method | snake_case                  | my_function  | Lowercase word or words. Separate words by underscores.                   |
| Module          | snake_case                  | my_module.py | Short. Lowercase word or words. Separate words with underscores.          |
| Package         | lowercase                   | mypackage.py | Short. Lowercase word or words. Do not separate words with underscores.   |
| Variable        | snake_case                  | my_variable  | Lowercase single letter, word, or words. Separate words with underscores. |

# Private elements

| Private element | Notation   | Example                   | Notes                       |
|-----------------|------------|---------------------------|-----------------------------|
| Class Method    | snake_case | __my_private_class_method | Starts with two underscore. |
| Function/Method | snake_case | _my_private_function      | Starts with one underscore. |

# Sources

- [PEP 8](https://peps.python.org/pep-0008/)