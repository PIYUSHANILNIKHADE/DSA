A = [2, 5, 1, 4, 6, 8]
N = len(A)

def set_min(A):
    mini = float('inf')
    for num in A:  # Iterate over A, not mini
        if num < mini:
            mini = num
    return mini

def set_max(A):
    maxi = float('-inf')
    for num in A:  # Iterate over A, not maxi
        if num > maxi:
            maxi = num
    return maxi

print("Maximum value:", set_max(A))
print("Minimum value:", set_min(A))
