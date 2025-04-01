# Quick Sort Python Script

This Python script implements a flexible and efficient sorting algorithm using a customized version of list sorting techniques. It allows sorting a list of items in different ways: numerically, alphabetically, or by specific dictionary keys when working with lists of dictionaries.

## Features

- Sorts a regular list of strings or numbers:
  - Numerically or alphabetically.
  - Handles mixed types in the list (e.g., strings and numbers).

- Sorts a list of dictionaries by a specific key:
  - Default sorting (first dictionary key).
  - Custom sorting based on any dictionary key.

## Usage

### Parameters:
- `data`: The list to be sorted. It can either be a list of dictionaries or a list of strings/numbers.
- `key`: The key used for sorting:
  - For a list of dictionaries, it specifies the dictionary key to sort by (default: the first key in the first dictionary).
  - For a regular list, it can be `'alphabet'`, `'numeric'`, or `'a'`, `'n'`, or `None` to indicate the type of sorting (alphabetical or numerical).

### Example Usage

1. **Sorting a List of Strings and Numbers:**

```python
list_only = [3, 1, 2, "a", "c", "b"]

quick_sort(list_only, "n")
# Output: [1, 2, 3, 'a', 'b', 'c']

quick_sort(list_only, "a")
# Output: ['a', 'b', 'c', 1, 2, 3]
```

2. **Sorting a List of Dictionaries:**

```python
dicts_in_list = [
    {'ArticleNumber': 3, 'Name': 'Product B'},
    {'ArticleNumber': 1, 'Name': 'Product A'},
    {'ArticleNumber': 2, 'Name': 'Product C'}
]

quick_sort(dicts_in_list)
# Output: [{'ArticleNumber': 1, 'Name': 'Product A'}, {'ArticleNumber': 2, 'Name': 'Product C'}, {'ArticleNumber': 3, 'Name': 'Product B'}]

quick_sort(dicts_in_list, 'Name')
# Output: [{'ArticleNumber': 1, 'Name': 'Product A'}, {'ArticleNumber': 3, 'Name': 'Product B'}, {'ArticleNumber': 2, 'Name': 'Product C'}]
```

## Installation

This script does not require any external libraries, so no installation is necessary. Simply download or clone the repository and you can run the script directly.

```bash
git clone https://github.com/Vrexira/quick_sort.git
cd quick_sort
python quick_sort.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
