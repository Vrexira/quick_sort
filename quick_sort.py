def quick_sort(data, key=None):
    if all(isinstance(item, dict) for item in data):
        # Sorting a list of dictionaries
        if key is None:
            # Default: sort by the first key in the first dictionary
            if data:
                key = next(iter(data[0]))
            else:
                return data
        # Ensure the sorting key exists in each dictionary, fallback to None
        data.sort(key=lambda x: x.get(key, None))
      
    else:
        # Sorting a regular list
        if key in ['alphabet', 'a', None]:
            # Sort alphabetically, treating all items as strings
            data.sort(key=lambda x: (not isinstance(x, str), str(x) if isinstance(x, str) else x))
        elif key in ['numeric', 'n']:
            # First sort numerically, then sort alphabetically
            data.sort(key = lambda x: (float(x) if isinstance(x, (int, float)) else float('inf'), not isinstance(x, str), str(x) if isinstance(x, str) else x))
        else:
            # Default sorting (depends on the Python version and types in list)
            data.sort()
          
    return data


if __name__ == "__main__":
    # For a normal list
    list_only = [3, 1, 2, "a", "c", "b"]
    # For a list of dictionaries
    dicts_in_list = [
        {'ArticleNumber': 3, 'Name': 'Product B'},
        {'ArticleNumber': 1, 'Name': 'Product A'},
        {'ArticleNumber': 2, 'Name': 'Product C'}
    ]
    
    quick_sort(list_only, "n")
    # Numerical Output: [1, 2, 3, 'a', 'b', 'c']
    quick_sort(list_only, "a")
    # Alphabetical Output: ['a', 'b', 'c', 1, 2, 3]
    quick_sort(dicts_in_list)
    # Default Dict Output: [{'ArticleNumber': 1, 'Name': 'Product A'}, {'ArticleNumber': 2, 'Name': 'Product C'}, {'ArticleNumber': 3, 'Name': 'Product B'}]
    quick_sort(dicts_in_list, 'Name')
    # Dict by Key Output: [{'ArticleNumber': 1, 'Name': 'Product A'}, {'ArticleNumber': 3, 'Name': 'Product B'}, {'ArticleNumber': 2, 'Name': 'Product C'}]
