# AI Level 0 Concepts 
---



#  1. Python Summary

## Python Basics
This summary provides an overview of Python fundamentals

1. `print()` => Used to display text or values on the screen.  
2. `input()` => Used to get input from the user as a string.  
3. `#` => Used to add comments in the code.  

---

## Data Types in Python
1. **String**
   - Used to store text.
   - Enclosed in single `' '` or double `" "` quotes.  
   
2. **Numbers**
   - `int` => Integer (10)  
   - `float` => Floating point number (10.1)  

3. **Booleans**
   - Represents two values: `True` or `False`.  

4. **Lists**
   - Used to store multiple items in a single variable.  
   EX: `Grades = ['A', 'B', 'C', 'D', 'F']`

5. **Dictionaries**
   - Store data in key-value pairs.  
   EX: `person = {"name": "Basmala", "age": 19}`  

6. **Sets**
   - An unordered collection of unique items.  
   EX: `colors = {"red", "blue", "green"}`  

7. **Tuples**
   - Similar to lists, but immutable (cannot be changed).  
   EX: `dimensions = (1920, 1080)`  

---

## Strings
Strings are sequences of characters enclosed in either single quotes (`'`) or double quotes (`"`).

### Common String Methods

1. **`len()`**  
   - Returns the length of the string.  

2. **`strip()`**  
   - Removes leading and trailing spaces.  
   - `rstrip()` → Remove spaces from the right.  
   - `lstrip()` → Remove spaces from the left.  

3. **`lower()`**  
   - Converts all characters to lowercase.  

4. **`upper()`**  
   - Converts all characters to uppercase.  

5. **`replace(old, new, count)`**  
   - Replaces occurrences of a substring with another.  

6. **`split(separator)`**  
   - Splits the string into a list based on the specified separator.  
   EX:  
   ```python
   text = "Basmala  Saeed Mohammed "
   print(text.split(","))  # Output: ['Basmala ', 'Saeed ', 'Mohammed']
7. **`find(substring, start, end)`**  
   - Returns the index of the first occurrence of the substring. Returns `-1` if not found.  
   - **`rfind(substring, start, end)`** → Searches for the substring from the right.
     

8. **`count(substring)`**  
   - Counts the occurrences of a substring in the string.

9. **`startswith(prefix)`**  
   - Checks if the string starts with the specified prefix.

10. **`endswith(suffix)`**  
   - Checks if the string ends with the specified suffix.

11. **`capitalize()`**  
   - Converts the first character to uppercase and the rest to lowercase.

12. **`title()`**  
   - Converts the first character of each word to uppercase.

13. **`isalpha()`**  
   - Returns `True` if the string contains only letters otherwise, returns `False`.

14. **`isdigit()`**  
   - Returns `True` if the string contains only digits otherwise, returns `False`.

15. **`isalnum()`**  
    - Returns `True` if the string contains only letters and digits otherwise, returns `False`.

16. **`isspace()`**  
    - Returns `True` if the string contains only whitespace otherwise, returns `False`.

17. **`format()`**  
    - Formats the string by inserting specified values.

19. **`split(separator, maxsplit)`**  
    - Splits the string into a list using the specified separator.  
    - **`rsplit(separator, maxsplit)`** → Starts splitting the string from the right using the specified separator.


20. **`join(iterable)`**  
    - Joins elements of an iterable with the string.

21. **`swapcase()`**  
    - Swaps uppercase characters to lowercase and vice versa.

22. **`center(width, fillchar)`**  
    - Centers the string in a field of the specified width.

23. **`zfill(width)`**  
    - Pads the string with zeros to the left to fill the specified width.

24. **`partition(separator)`**  
    - Splits the string into three parts: before, the separator, and after.
---

## Lists 

A list is a collection of items in an ordered sequence. Below are the common list methods you can use in Python:
### Common Lists Methods
1. **`append(item)`**
   - Adds an item to the end of the list.
   
2. **`extend(iterable)`**
   - Adds all elements of an iterable (like another list or a tuple) to the end of the list.
   
3. **`insert(index, item)`**
   - Inserts an item at a specified index.


4. **`remove(item)`**
   - Removes the first occurrence of an item in the list. If the item is not found, it returns a `ValueError`.
  

5. **`pop(index)`**
   - Removes and returns the item at the specified index. If no index is provided, it removes and returns the last item.
   

6. **`clear()`**
   - Removes all items from the list.

7. **`index(item)`**
   - Returns the index of the first occurrence of an item. Raises a `ValueError` if the item is not found.
 .

8. **`count(item)`**
   - Returns the number of times an item appears in the list.

9. **`sort()`**
   - Sorts the items of the list in ascending order. You can specify a custom sort order using the `reverse` and `key` parameters.
  

10. **`reverse()`**
    - Reverses the elements of the list in place.

11. **`copy()`**
    - Returns a shallow copy of the list.

12. **`join(iterable)`**
    - Joins all items in the list into a string, with the specified separator between each item.

13. **`list()`**
    - Converts an iterable (like a string, tuple, or set) into a list.

14. **`min()`**
    - Returns the smallest item in the list.

15. **`max()`**
    - Returns the largest item in the list.
    

16. **`sum()`**
    - Returns the sum of all items in the list (only works for numeric values).

17. **`enumerate()`**
    - Returns an iterator that produces pairs of an index and an item from the list.

18. **`copy()`**
    - Creates a shallow copy of the list.
---

## Tuples

### What are Tuples?
- A tuple is an unchangeable collection of items, where each item can be of a different data type.
- Tuples are defined using parentheses `()` and are faster and more memory-efficient than lists.
  - **Why?** Becouse tuples are immutable (cannot be modified), they are inherently faster.

### Why Use Tuples?
- **To store fixed collections of data**: When the data shouldn't be changed after creation.
- **Efficiency**: They are faster and use less memory compared to lists.
- **Dictionary Keys**: Tuples can be used as keys in dictionaries because they are immutable.

---

### Common Tuples Methods

1. **`len()`**  
   - Returns the number of elements in the tuple.  
     ```python
     len((1, 2, 3))  # Output: 3
     ```

2. **`index(value)`**  
   - Returns the first index of the specified value.  
   

3. **`count(value)`**  
   - Counts how many times a value appears in the tuple.  
    

4. **`tuple()`**  
   - Converts an iterable (like a list) into a tuple.  
     ```python
     tuple([1, 2, 3])  # Output: (1, 2, 3)
     ```

5. **Slicing**  
   - Extracts a portion of the tuple using slicing (`[start:end:step]`).  
     ```python
     (1, 2, 3, 4)[1:3]  # Output: (2, 3)
     ```

6. **Concatenation**  
   - Combines two tuples using the `+` operator.  
     ```python
     (1, 2) + (3, 4)  # Output: (1, 2, 3, 4)
     ```

7. **Repetition**  
   - Repeats the tuple multiple times using the `*` operator.  
     ```python
     (1, 2) * 2  # Output: (1, 2, 1, 2)
     ```
   - **Note**: This also works with strings and lists.

8. **Membership Testing**  
   - Checks if a value exists in the tuple using the `in` keyword.  
     ```python
     2 in (1, 2, 3)  # Output: True
     ```

9. **Max and Min**  
   - **`max(tuple)`**: Returns the maximum value.  
   - **`min(tuple)`**: Returns the minimum value.  
     ```python
     max((1, 2, 3))  # Output: 3
     min((1, 2, 3))  # Output: 1
     ```
