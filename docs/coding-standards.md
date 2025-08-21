# Coding Standards
This page should serve to define coding standards that should be relevant for the project.
The definitions are divided into various areas such as general and for the individual languages and technologies.

## General
1. Readability: Code should always be easily readable. This means using meaningful names for variables, functions, modules, etc.
2. Modularity: The code should be divided into smaller modules to simplify maintainability. Use functions and classes to logically group the code.
3. Commenting: Comment the code to explain what it does and why. Use comments to explain and document complicated parts of the code.
4. Testing: Write tests to ensure that the code works as expected. Write automated tests to ensure that no errors are introduced during further development of the code.
5. Code reviews: Code reviews are important to ensure that the code meets the standards and to receive feedback from other developers. Code reviews should also be used to improve collaboration and code quality.
6. Documentation: The documentation should describe how the code should be used and how it works. Automatic documentation generation should be used to ensure that the documentation is always up-to-date.
7. Use descriptive names: Use descriptive variable, function, and class names that accurately describe their purpose. Avoid abbreviations, single-letter variables, and names that are too general.
8. Follow the DRY principle: Don't Repeat Yourself. Avoid writing duplicate code and instead use functions or classes to reuse code where possible.

## Python
1. Code conventions: A unified convention should be used. For this purpose, in Python, there is PEP8: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)
2. Tests: In Python, there is the following testing library we should use to run the tests: [pytest](https://docs.pytest.org/en/7.3.x/) 
3. Use docstrings: Use docstrings to document your code's functions and classes. Docstrings are used to generate documentation and can be helpful for other developers who want to use your code: [docstrings](https://peps.python.org/pep-0257/)

### Further tools which should be considered using are:
- Dependency Manager: [poetry](https://python-poetry.org/)
- Formatter: [black](https://pypi.org/project/black/)
- Linter: [ruff](https://pypi.org/project/ruff/)
- Type Checker: [pyright](https://github.com/microsoft/pyright)
