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
---
## Sets

- A set is an unordered collection of unique elements.
- Sets are defined using curly braces `{}` or the `set()` function.
- They are mutable, meaning you can add or remove elements, but the elements themselves must be immutable.

### Why Use Sets?
- To store unique items without duplicates.
- For fast membership testing using the `in` keyword.
- Useful for operations like union, intersection, and difference.

### Common Sets Methods

1. **`add(value)`**
   - Adds a single value to the set.

2. **`update(iterable)`**
   - Adds multiple elements from an iterable (like a list) to the set.

3. **`remove(value)`**
   - Removes the specified value. Raises a `KeyError` if the value does not exist.

4. **`discard(value)`**
   - Removes the specified value without raising an error if the value does not exist.

5. **`pop()`**
   - Removes and returns an arbitrary element from the set. Raises a `KeyError` if the set is empty.

6. **`clear()`**
   - Removes all elements from the set.

7. **`union(*other_sets)`**
   - Returns a new set with all unique elements from all sets.
   - We can use `|` to perform union.

8. **`intersection(*other_sets)`**
   - Returns a new set with common elements between sets.
   - We can use `&` to perform intersection.

9. **`difference(*other_sets)`**
   - Returns a new set with elements only in the original set, not in the others.
   - We can use `-` to perform difference.

10. **`symmetric_difference(other_set)`**
    - Returns a new set with elements in either of the sets but not in both.
    - We can use `^` to perform symmetric difference.

11. **`issubset(other_set)`**
    - Checks if all elements of the set are in another set.

12. **`issuperset(other_set)`**
    - Checks if the set contains all elements of another set.

13. **`isdisjoint(other_set)`**
    - Checks if the two sets have no elements in common.

14. **`copy()`**
    - Creates and returns a shallow copy of the set.
---
## Dictionaries

- A dictionary is an unordered collection of key-value pairs.
- Dictionaries are defined using curly braces `{}` or the `dict()` function.
- Keys must be immutable, while values can be of any data type.
- Dictionaries are mutable, meaning you can add, remove, and modify elements.

### Why Use Dictionaries?
- To store data in key-value pairs.
- Ideal for fast lookups based on keys.
- Efficient for operations like updating values, removing keys, and checking for the existence of keys.

### Common Dictionary Methods

1. **`clear()`**
   - Removes all elements from the dictionary.

2. **`copy()`**
   - Returns a shallow copy of the dictionary.

3. **`fromkeys(keys, value=None)`**
   - Creates a new dictionary from the given sequence of keys, with optional values assigned to each key.

4. **`get(key, default=None)`**
   - Returns the value for the specified key. If the key doesn't exist, returns the default value (None by default).

5. **`items()`**
   - Returns a view object displaying a list of dictionary’s key-value tuple pairs.

6. **`keys()`**
   - Returns a view object displaying a list of all the dictionary’s keys.

7. **`pop(key, default=None)`**
   - Removes and returns the value for the specified key. If the key doesn't exist, returns the default value (None by default).

8. **`popitem()`**
   - Removes and returns the last key-value pair added to the dictionary as a tuple.

9. **`setdefault(key, default=None)`**
   - Returns the value of the key if it exists, otherwise inserts the key with a specified default value and returns the default value.

10. **`update(other_dict)`**
    - Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.

11. **`values()`**
    - Returns a view object displaying a list of all the dictionary’s values.

12. **`get(key)`**
    - Returns the value of the specified key. Returns `None` if the key does not exist.

13. **`del` (Delete)**
    - Removes the specified key-value pair from the dictionary.

14. **`in` (Membership Testing)**
    - Checks if a key exists in the dictionary.
    - Example: `key in my_dict`
---
## Operators
Python provides various types of operators for performing operations:

### 1. **Arithmetic Operators**:
| Operator | Description      | Example      |
|----------|------------------|--------------|
| `+`      | Addition         | `5 + 2 = 7`  |
| `-`      | Subtraction      | `5 - 2 = 3`  |
| `*`      | Multiplication   | `5 * 2 = 10` |
| `/`      | Division         | `5 / 2 = 2.5`|
| `//`     | Floor Division   | `5 // 2 = 2` |
| `%`      | Modulus          | `5 % 2 = 1`  |
| `**`     | Exponentiation   | `5 ** 2 = 25`|

### 2. **Comparison Operators**:
| Operator | Description                | Example      |
|----------|----------------------------|--------------|
| `==`     | Equal                      | `5 == 5`     |
| `!=`     | Not equal                  | `5 != 2`     |
| `<`      | Less than                  | `5 < 10`     |
| `>`      | Greater than               | `10 > 5`     |
| `<=`     | Less than or equal to      | `5 <= 5`     |
| `>=`     | Greater than or equal to   | `10 >= 5`    |

### 3. **Logical Operators**:
| Operator | Description            | Example             |
|----------|------------------------|---------------------|
| `and`    | Returns `True` if both conditions are true | `(5 > 2 and 10 > 5)` |
| `or`     | Returns `True` if at least one condition is true | `(5 > 10 or 10 > 5)` |
| `not`    | Reverses the result    | `not(5 > 2)`        |
---

## Python Conditions

 ### 1. **Basic If Statement**
- Execute a block of code if a condition is `True`.

### Syntax:
```python
if condition:
    # Code to execute if condition is True
 ```       
  ### 2. **If-Else Statement**
- Execute one block of code if a condition is True, and another block if it is False.

  ### Syntax:
```python
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
 ```
### 3. **If-Elif-Else Statement**
- Used to test multiple conditions sequentially

### Syntax:
```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
else:
    # Code to execute if none of the conditions are True
 ```

### 4. **Nested If**
- An if statement inside another if statement to check complex conditions.

### Syntax:
```python
if condition1:
    if condition2:
        # Code to execute if both conditions are True

 ```
### 5. **Short-Hand If**
- A concise way to write a single condition.

### Syntax:
```python
  if condition: statement
 ```

### 6. **Short-Hand If-Else (Ternary Operator)**
- Write if-else in a single line.

### Syntax:
```python
statement_if_true if condition else statement_if_false
 ```
---
## Python Loops 

 - loops allow us to execute a block of code repeatedly. 

### 1. `for` loop
- The `for` loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string). It iterates over each element in the sequence.

### Syntax:
```python
for variable in sequence:
    # code block
```
### 2. `while` loop

- The `while` loop repeatedly executes a block of code as long as a given condition is True.
### Syntax:
```python
while condition:
    # code block
```

### 3. `break` statement
- The `break` statement is used to terminate the loop prematurely when a certain condition is met

### 4. `continue` statement
- The `continue` statement skips the current iteration and moves to the next iteration in the loop.
---
# **Functions**
- A function in Python is a block of reusable code designed to perform a specific task.

### **Why Functions?**
Functions help in:
- Reducing code redundancy
- Improving readability
- Enabling modular programming

### **Syntax**
```python
def function_name(parameters):
    """
    Optional Docstring
    """
    # Function body
    return value  # Optional
```
## **Types of Functions**

### 1. **Built-in Functions**
- Predefined in Python (e.g., `len()`, `print()`, `sum()`, etc.).
- Do not require explicit definition.

### 2. **User-Defined Functions**
- Created by the user using the `def` keyword.

### 3. **Anonymous (Lambda) Functions**
- Functions without a name.
- Defined using the `lambda` keyword.
- Used for short, simple operations.

**Syntax**: 
```python
lambda arguments: expression
```
### 4. **Recursive Functions**
- Functions that call themselves.
- Used for solving problems like factorial, Fibonacci, etc.

###5. **Higher-Order Functions**
- Accept functions as arguments or return functions.
  Ex: map(), filter(), reduce().

## **Function Properties**

### 1. **Default Parameters**
- Parameters can have default values, making them optional.

**Example**: 
```python
def Myself(name="Basmala"):
    return f"Hello, {name}!"
print(Myself())  # Output: Hello, Basmala!
### 2. **Keyword Arguments**
- Arguments can be passed by name, improving readability.
```
**Example**: 
```python
def multiply(a, b):
    return a * b
print(multiply(b=3, a=2))  # Output: 6
```

### 3. **Variable-Length Arguments**
A. **`*args`**: Accepts a variable number of positional arguments.

**Example**:
```python
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4))  # Output: 10
```
### B. **`**kwargs`**: Accepts a variable number of keyword arguments.

**Example**:
```python
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="Basmala", age=20)  
# Output:
# name: Basmala
# age: 20
```
### 4. **Return Statement**
- Functions can return a value using the `return` statement.
- If no `return` statement is provided, the function returns `None` by default.

**Example**:
```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Basmala")
print(message)  # Output: Hello, Basmala!

def no_return():
    pass

result = no_return()
print(result)  # Output: None
```
---
## File Handling in Python

Python provides various tools and techniques for working with files and directories.

---

### File Modes

Python supports several file modes for different operations:

- **`"a"` (Append)**: Opens a file for appending data. Creates the file if it does not exist.
- **`"r"` (Read)**: Opens a file for reading. This is the default mode. Raises an error if the file does not exist.
- **`"w"` (Write)**: Opens a file for writing. Creates the file if it does not exist.
- **`"x"` (Create)**: Creates a file. Raises an error if the file already exists.

---

### Working with Directories

The `os` module provides functions to work with directories:

- **`os.getcwd()`**: Returns the current working directory.
- **`os.path.dirname(os.path.abspath(__file__))`**: Returns the directory of the currently executing script.
- **`os.chdir(path)`**: Changes the current working directory to the specified path.
- **`os.path.abspath(file)`**: Returns the absolute path of the specified file.

---

### Important File Operations

Here are some key file operations in Python:

- **`file.truncate(size)`**: Resizes the file to the specified size. If no size is specified, it truncates the file to the current position.
- **`file.tell()`**: Returns the current position of the file pointer.
- **`file.seek(offset)`**: Moves the file pointer to the specified offset.
- **`os.remove(path)`**: Deletes the file at the specified path.

---

### Notes

- Always close files after performing operations using `file.close()` to free up system resources.
- Use the `with` statement for better file handling, as it automatically closes the file after the operations are complete. 

### Example:
```python
with open("example.txt", "w") as file:
    file.write("Basmala")  # File is automatically closed after this block
```
---
## Python Built-in Functions
---

### 1. Input/Output Functions

- **`print()`**: Outputs text or variables to the console.
- **`input()`**: Reads input from the user as a string.

---

### 2. Type Conversion Functions

- **`int()`**: Converts a value to an integer.
- **`float()`**: Converts a value to a floating-point number.
- **`str()`**: Converts a value to a string.
- **`bool()`**: Converts a value to a boolean (`True` or `False`).

---

### 3. Mathematical Functions

- **`abs()`**: Returns the absolute value of a number.
- **`round()`**: Rounds a number to the nearest integer or specified decimal places.
- **`min()`**: Returns the smallest value in a sequence.
- **`max()`**: Returns the largest value in a sequence.
- **`sum()`**: Returns the sum of all items in a sequence.

---

### 4. Sequence Functions

- **`len()`**: Returns the length of a sequence (e.g., string, list, tuple).
- **`sorted()`**: Returns a sorted list of the specified iterable.
- **`reversed()`**: Returns a reversed iterator of a sequence.
- **`enumerate()`**: Adds a counter to an iterable and returns it as an enumerate object.

---

### 5. String Functions

- **`str.upper()`**: Converts a string to uppercase.
- **`str.lower()`**: Converts a string to lowercase.
- **`str.strip()`**: Removes leading and trailing whitespace.
- **`str.split()`**: Splits a string into a list based on a delimiter.
- **`str.join()`**: Joins elements of a list into a string.

---

### 6. List Functions

- **`list.append()`**: Adds an element to the end of a list.
- **`list.remove()`**: Removes the first occurrence of a value from a list.
- **`list.pop()`**: Removes and returns an element at a given index (default is the last element).

---

### 7. Dictionary Functions

- **`dict.keys()`**: Returns a list of all keys in a dictionary.
- **`dict.values()`**: Returns a list of all values in a dictionary.
- **`dict.items()`**: Returns a list of key-value pairs as tuples.

---

### 8. File Handling Functions

- **`open()`**: Opens a file and returns a file object.
- **`file.read()`**: Reads the entire content of a file.
- **`file.write()`**: Writes data to a file.
- **`file.close()`**: Closes the file.

---

### 9. Other Useful Functions

- **`range()`**: Generates a sequence of numbers.
- **`type()`**: Returns the type of an object.
- **`isinstance()`**: Checks if an object is an instance of a specific class.
- **`help()`**: Displays documentation for a function or module.

---

### 10. Lambda and Functional Programming

- **`map()`**: Applies a function to all items in an iterable.
- **`filter()`**: Filters items in an iterable based on a condition.
- **`reduce()`**: Applies a function cumulatively to items in an iterable (requires the `functools` module).

---
## Classes and Objects in Python

---

### Classes
A **class** is a blueprint for creating objects. It defines attributes (variables) and behaviors (methods).

#### Syntax:
```python
class ClassName:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def method_name(self):
        return f"Values: {self.param1}, {self.param2}"
```




### Objects
An **object** is an instance of a class. It has its own values for the attributes defined in the class.

---
### Key Concepts

- **Encapsulation**: Binding data (attributes) and methods together.
-  **Inheritance**: Allowing a class to inherit methods and attributes from another class.
- **Polymorphism**: Different classes can have methods with the same name but different implementations.
- **Abstraction**: Hiding implementation details and exposing only the necessary functionality.

---
## NumPy - Numerical Python

NumPy (Numerical Python) is an open-source library in Python used for handling **arrays** and **multidimensional matrices**, providing many mathematical functions for efficient processing.

###  Why Use NumPy?
- **Consumes less memory** compared to Python lists.
- **Faster performance** in mathematical operations than lists.
- **Easy to use** with a simple interface.
- **Supports element-wise operations**.
- **Stores elements contiguously in memory**, enhancing performance.
- **Highly optimized for numerical computations**.
- **Integrates well with other libraries like Pandas, SciPy, and Matplotlib**.

###  Comparison Between Python Lists and NumPy Arrays
#### Python Lists:
- **Homogeneous**: Can contain elements of the same type.
- **Heterogeneous**: Can contain elements of different types.

####  NumPy Arrays:
- All elements in an array **must be of the same type**.
- You can determine **the storage size required** for the array in advance.
- **Arrays are indexed from 0**, similar to Python lists.
- **Supports vectorized operations**, making computations more efficient.
- **Provides built-in mathematical functions** that operate on entire arrays.



###  Common NumPy Functions & Examples
#### Creating Arrays
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

#### Generating Ranges
```python
arr = np.arange(1, 10, 2)  # Generates an array [1, 3, 5, 7, 9]
print(arr)
```

#### Creating Zeros and Ones Arrays
```python
zeros = np.zeros((3, 3))  # 3x3 matrix filled with zeros
ones = np.ones((2, 2))    # 2x2 matrix filled with ones
print(zeros)
print(ones)
```

#### Mathematical Operations
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

sum_arr = arr1 + arr2  # Element-wise addition
prod_arr = arr1 * arr2  # Element-wise multiplication

print(sum_arr)
print(prod_arr)
```

#### Statistical Functions
```python
arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))  # Mean
print(np.median(arr))  # Median
print(np.std(arr))  # Standard Deviation
```


---
# 2. Introduction to Statistics

## 1. What is Statistics?
#### Definition
Statistics is the science of developing and studying methods for collecting, analyzing, interpreting, and presenting empirical data.

#### Key Features
- Highly interdisciplinary, applicable to virtually all scientific fields.
- Research questions drive the development of new statistical theories and tools.
- Relies on mathematical and computational tools, with core concepts like uncertainty and variation.
- Statistical methods analyze raw data, build models, and draw conclusions.

#### Key Terms
- **Population**: The entire dataset to be studied.
- **Sample**: A representative subset of the population.
- **Variable**: A measurable or countable data item (e.g., age, income).

---

### 2. Types of Analysis
#### Quantitative Analysis
- Focuses on numerical data, using patterns and visualizations (e.g., graphs, charts).

#### Qualitative Analysis
- Extracts insights from non-numerical sources (e.g., text, images).

---

### 3. Types of Statistics
#### Descriptive Statistics
- Summarizes data characteristics (e.g., mean, median, mode).

#### Inferential Statistics
- Uses samples to make predictions about populations (e.g., hypothesis testing, regression).

---

### 4. Core Formulas
#### Measures of Central Tendency

#### Mean (Average)
```math
Mean = \frac{\sum X}{N}
```
Where:
- \( \sum X \) is the sum of all data points
- \( N \) is the number of data points

#### Median
- If the dataset size is **odd**: The middle value after sorting.
- If the dataset size is **even**: The average of the two middle values.

#### Mode
- The most frequently occurring value in the dataset.

---

### Measures of Spread

#### Range
```math
Range = Max\ Value - Min\ Value
```

#### Variance (\( \sigma^2 \))
```math
Variance = \frac{\sum (X - \bar{X})^2}{N}
```
Where:
- \( X \) is each data point
- \(  bar{X} \) is the mean
- \( N \) is the number of data points

#### Standard Deviation (\( sigma \))
```math
Standard\ Deviation = \sqrt{Variance}
```

---

## 5. Fundamental Concepts

### Uncertainty
- Recognizes limitations in data (e.g., sampling errors).

### Variation
- Differences within datasets (measured via variance or standard deviation).

---



