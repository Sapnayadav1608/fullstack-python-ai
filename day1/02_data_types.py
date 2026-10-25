# =============================================================================
# DAY 1 - TOPIC 02: Python Data Types
# =============================================================================
# Data Types batate hain ki variable ke andar kis type ki value store hai.
# type() function se hum kisi bhi variable ka data type check kar sakte hain.
# =============================================================================

# 1. Integer (int) -> Bina decimal wale poore numbers (positive ya negative)
count = 100
negative_num = -50

# 2. Float (float) -> Decimal wale numbers
price = 99.50
pi_value = 3.14159

# 3. String (str) -> Text (Single ya Double quotes ke andar)
course_name = "Full Stack Development"
symbol = '@'

# 4. Boolean (bool) -> Sirf do values: True ya False (T aur F Capital hona chahiye)
is_logged_in = True
is_admin = False

# 5. NoneType (None) -> Matlab "kuch nahi" / Empty value
user_address = None

# Checking Types using type() function
print("count ka type       :", type(count))          # <class 'int'>
print("price ka type       :", type(price))          # <class 'float'>
print("course_name ka type :", type(course_name))    # <class 'str'>
print("is_logged_in ka type:", type(is_logged_in))   # <class 'bool'>
print("user_address ka type:", type(user_address))   # <class 'NoneType'>
