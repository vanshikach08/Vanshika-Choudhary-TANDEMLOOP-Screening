def generate_modified_series(a):
    n = a if a % 2 != 0 else a - 1
    return [2*i + 1 for i in range((n + 1) // 2)]

# Example usage
print(generate_modified_series(3))  
print(generate_modified_series(4))  
print(generate_modified_series(5))  
