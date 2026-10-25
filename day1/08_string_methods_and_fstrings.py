# =============================================================================
# DAY 1 - TOPIC 08: String Methods & Modern f-strings
# =============================================================================
# Strings par kaam karne ke liye Python bohot saare handy built-in methods deta hai.
# f-strings string ke andar variables ko beautifully embed karne ka sabse clean tareeqa hai.
# =============================================================================

message = "   Hello Python Developers!   "

# 1. Common String Methods
print("Original   :", repr(message))
print("strip()    :", repr(message.strip()))      # Aage aur peeche ke faltu spaces hata deta hai
print("lower()    :", message.lower())            # Sab lowercase
print("upper()    :", message.upper())            # Sab uppercase
print("replace()  :", message.replace("Python", "World"))  # Word replace karna
print("count('e') :", message.count("e"))         # 'e' kitni baar aaya

# 2. split() and join()
csv_data = "apple,banana,mango,orange"
fruits_list = csv_data.split(",")                 # String ko list mein convert kar diya
print("\nsplit() result :", fruits_list)

joined_text = " - ".join(fruits_list)             # List ko wapas string bana diya
print("join() result  :", joined_text)

# 3. Modern f-strings (Python 3.6+)
# String ke aage 'f' lagao aur {} curly braces ke andar variables likh do!
user = "Sapna"
day = 1
topics_count = 12

summary = f"Student {user} has completed Day {day} with {topics_count} core topics!"
print("\n--- f-string Demo ---")
print(summary)

# f-string mein calculation aur formatting:
price = 499.5678
print(f"Discounted Price: Rs {price:.2f}")  # .2f ka matlab decimal ke baad sirf 2 digits
