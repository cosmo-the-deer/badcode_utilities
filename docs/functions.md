# Functions

## can_str_be_int(string)
**Description:**  
Checks if the given string can be converted to an integer.

**Parameters:**  
- `string` (str): The string to check.

**Returns:**  
- `True` if the string can be converted to an integer, otherwise `False`.

---

## str_to_int_or_none(string)
**Description:**  
Converts the given string to an integer if possible, otherwise returns `None`.

**Parameters:**  
- `string` (str): The string to convert.

**Returns:**  
- `int` if conversion is possible, otherwise `None`.

---

## get_yn_bool(text)
**Description:**  
Prompts the user for a yes/no input (`y` or `n`). Returns `True` for yes, `False` for no.

**Parameters:**  
- `text` (str): The prompt to display.

**Returns:**  
- `True` if user inputs `y`, `False` if user inputs `n`.

---

## get_yn_str(text)
**Description:**  
Prompts the user for a yes/no input (`y` or `n`). Returns the string entered.

**Parameters:**  
- `text` (str): The prompt to display.

**Returns:**  
- `'y'` or `'n'` as entered by the user.

---

## print_info()
**Description:**  
Prints project and contact information to the console.

**Parameters:**  
- None

**Returns:**  
- None

---

## generate_key(length=10, characters=characters_standard)
**Description:**  
Generates a random key of specified length using the provided set of characters.

**Parameters:**  
- `length` (int, optional): Length of the key (default is 10).
- `characters` (list, optional): List of characters to use (default is `characters_standard`).

**Returns:**  
- `str`: The generated key.

---

## is_string_bad(string)
**Description:**  
Checks if the given string contains any words from the bad words list.

**Parameters:**  
- `string` (str): The string to check.

**Returns:**  
- `True` if any bad word is found, otherwise `False`.

---

## load_badwords()
**Description:**  
Loads the list of bad words from the `badwords.txt` file included in the package.

**Parameters:**  
- None

**Returns:**  
- `list`: List of bad words.

---