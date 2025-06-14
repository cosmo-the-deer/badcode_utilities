# Functions

## can_str_be_int(string)
**Description:**  
Checks if the given string can be converted to an integer.

**Parameters:**  
- `string` (str): The string to check.

**Returns:**  
- `True` if the string can be converted to an integer, otherwise `False`.

**Example:**
```python
can_str_be_int("123")    # True
can_str_be_int("abc")    # False
```

---

## str_to_int_or_none(string)
**Description:**  
Converts the given string to an integer if possible, otherwise returns `None`.

**Parameters:**  
- `string` (str): The string to convert.

**Returns:**  
- `int` if conversion is possible, otherwise `None`.

**Example:**
```python
str_to_int_or_none("42")     # 42
str_to_int_or_none("hello")  # None
```

---

## get_yn_bool(text)
**Description:**  
Prompts the user for a yes/no input (`y` or `n`). Returns `True` for yes, `False` for no.

**Parameters:**  
- `text` (str): The prompt to display.

**Returns:**  
- `True` if user inputs `y`, `False` if user inputs `n`.

**Example:**
```python
answer = get_yn_bool("Continue? (y/n): ")
# User enters 'y' -> answer is True
# User enters 'n' -> answer is False
```

---

## get_yn_str(text)
**Description:**  
Prompts the user for a yes/no input (`y` or `n`). Returns the string entered.

**Parameters:**  
- `text` (str): The prompt to display.

**Returns:**  
- `'y'` or `'n'` as entered by the user.

**Example:**
```python
answer = get_yn_str("Continue? (y/n): ")
# User enters 'y' -> answer is 'y'
# User enters 'n' -> answer is 'n'
```

---

## print_info()
**Description:**  
Prints project and contact information to the console.

**Parameters:**  
- None

**Returns:**  
- None

**Example:**
```python
print_info()
# Output:
#     #-------------------------------------#
#     made by cosmo-the-deer 2025 mit license
#     ...
```

---

## generate_key(length=10, characters=characters_standard)
**Description:**  
Generates a random key of specified length using the provided set of characters.

**Parameters:**  
- `length` (int, optional): Length of the key (default is 10).
- `characters` (list, optional): List of characters to use (default is `characters_standard`).

**Returns:**  
- `str`: The generated key.

**Example:**
```python
generate_key()           # e.g., 'a8F3kLm2Qz'
generate_key(5)          # e.g., 'X9p2B'
```

---

## is_string_bad(string)
**Description:**  
Checks if the given string contains any words from the bad words list.

**Parameters:**  
- `string` (str): The string to check.

**Returns:**  
- `True` if any bad word is found, otherwise `False`.

**Example:**
```python
is_string_bad("hello world")        # False
is_string_bad("some badword here")  # True (if 'badword' is in badwords.txt)
```

---

## filter_string(string, replacement_charator="", words=bad_words)
**Description:**  
Replaces each bad word in the string with a replacement character repeated to match the word's length.

**Parameters:**  
- `string` (str): The string to filter.
- `replacement_charator` (str, optional): The character to use for replacement (e.g., '*').
- `words` (list, optional): List of words to filter (default is `bad_words`).

**Returns:**  
- `str`: The filtered string with bad words replaced.

**Example:**
```python
filter_string("this is shit", "*")  # 'this is ****'
filter_string("badword here", "#")   # '####### here' (if 'badword' is in bad_words)
```
