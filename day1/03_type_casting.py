# =============================================================================
# DAY 1 - TOPIC 03: Type Casting (Type Conversion)
# =============================================================================
# Ek data type ko doosre data type mein convert karne ko Type Casting kehte hain.
# =============================================================================

# 1. Implicit Conversion (Python khud automatic kar leta hai)
num_int = 10      # int
num_float = 2.5   # float
result = num_int + num_float  # Python ne int ko automatically float bana diya
print("result:", result, "| type:", type(result))  # 12.5 (<class 'float'>)

# 2. Explicit Conversion (Hum zabardasti convert karte hain)

# String se Integer:
str_num = "100"
converted_int = int(str_num)
print("converted_int + 50 =", converted_int + 50)  # 150

# Integer se String:
points = 95
str_points = str(points)
print("Score: " + str_points)

# String ya Int se Float:
x = float("12.34")
y = float(5)
print("float x:", x)  # 12.34
print("float y:", y)  # 5.0

# Boolean Conversion (Truthy vs Falsy):
# 0, empty string "", None -> False bante hain
# Baaki sab -> True bante hain
print("bool(1) :", bool(1))     # True
print("bool(0) :", bool(0))     # False
print("bool('') :", bool(""))   # False
print("bool('hi'):", bool("hi")) # True
