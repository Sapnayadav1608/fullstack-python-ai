# =============================================================================
# DAY 03 - PROBLEM 05: String Compression & Run-Length Encoding (RLE)
# =============================================================================
# Classic Technical Interview Problem (LeetCode #443 Variation)
# Consecutive characters ko count karke compress karna.
# Example: "aabcccccaaa" -> "a2b1c5a3"
# =============================================================================

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

print("=" * 60)
print("[DAY 03 - PROBLEM 05] String Compression & Run-Length Encoding")
print("=" * 60)

# -----------------------------------------------------------------------------
# ALGORITHM: String Compression
# Consecutive characters count karo, aur agar compressed string chhota hai
# tabhi compress karo, warna original return karo (Production Rule).
# -----------------------------------------------------------------------------
def compress_string(s: str) -> str:
    if not s:
        return ""
        
    compressed_parts = []
    consecutive_count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            consecutive_count += 1
        else:
            compressed_parts.append(f"{s[i - 1]}{consecutive_count}")
            consecutive_count = 1
            
    # Aakhiri group ko append karna mat bhoolna!
    compressed_parts.append(f"{s[-1]}{consecutive_count}")
    
    compressed_result = "".join(compressed_parts)
    
    # Interview Rule: Agar compressed version original se bada hai toh original hi return karo
    return compressed_result if len(compressed_result) < len(s) else s

print("--- String Compression Tests ---")
examples = ["aabcccccaaa", "WWWWWWWWWWWWBWWWWWWWWWWWWBBB", "abcde"]
for ex in examples:
    print(f"Original  : {ex} (len: {len(ex)})")
    print(f"Compressed: {compress_string(ex)} (len: {len(compress_string(ex))})\n")


# -----------------------------------------------------------------------------
# REVERSE ALGORITHM: String Decompression / Expansion
# Example: "a3b2c1" -> "aaabbc"
# -----------------------------------------------------------------------------
def decompress_string(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        
        # Multi-digit numbers handle karne ke liye (jaise a12)
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
            
        count = int(count_str) if count_str else 1
        result.append(char * count)
        
    return "".join(result)

compressed_sample = "a4b2c6d1"
print("--- String Decompression (Reverse) ---")
print("Compressed :", compressed_sample)
print("Decompressed:", decompress_string(compressed_sample))
