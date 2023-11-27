# Dropdown Parser

Have you ever found yourself in the midst of trying to programmatically extract dropdown values from a Word Document for stakeholders?

If not, consider yourself a lucky person! If so, you've likely scoured StackOverflow and `python-docx` documentation to no avail.

Well, fear no more! Introducing **`dropdown_parser`**, a Python CLI package that is designed to extract and export dropdown values from Word Docs!


<br>

## Installation

```sh
pip3 install git+https://github.com/StephenODea54/dropdown-parser.git
```

If everything went well, you should see the following:

```sh
These apps are now globally available
    - dropdown_parser

done! ✨🌟✨
```


<br>

## Usage Examples

### Documentation

```sh
dropdown_parser --help
```

### Output to CSV

```sh
dropdown_parser my_file.docx

# Outputs to my_file.csv
```

or

```sh
dropdown_parser my_file.docx -o csv

# Outputs to my_file.csv
```

### Output to JSON

```sh
dropdown_parser my_file.docx -o json

# Outputs to my_file.json
```

### Output to TXT

```sh
dropdown_parser my_file.docx -o txt

# Outputs to my_file.txt
```

### Output to XLSX

```sh
dropdown_parser /path/to/word/doc -o xlsx


# Outputs to my_file.xlsx
```


<br>

## Development Setup

### Prerequisites

The following needs to be installed on your local environment:

- poetry
- pytest
- pre-commit
- black

TODO: Add Docker for local dev environment

### Installation

1. Clone the repository:

```sh
git clone https://github.com/StephenODea54/dropdown-parser.git
```

2. Install dependencies:

```sh
poetry install
```

3. Enable pre-commit hooks:

```sh
pre-commit install
```


<br>

### Licensing

Stephen O'Dea - odeastephen1@gmail.com

Distributed under the MIT license. See `LICENSE` for more information.


<br>

### Contributing

1. Fork repo (<https://github.com/StephenODea54/dropdown-parser/fork>)
2. Create a feature branch (`git checkout -b feature/my-cool-feature`)
3. Commit changes (`git commit -m "Added my-cool-feature"`)
4. Push to branch (`git push origin feature/my-cool-feature`)
5. Create a new pull request
