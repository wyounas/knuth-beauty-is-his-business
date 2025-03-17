def knuth_p2(n):
    """
    Implements Knuth's P2 algorithm to find the shortest decimal
    representation of n/2^16.
    
    Args:
        n: An integer in the range 0 < n < 2^16
        
    Returns:
        A tuple (decimal_fraction, digits, k) where:
        - decimal_fraction is a string representation
        - digits is the list of digits
        - k is the number of digits
    """
    assert 0 < n < 2**16, "n must be in range 0 < n < 2^16"
    
    j = 0
    s = 10 * n + 5
    t = 10
    digits = []
    
    print(f"Initial values: s={s}, t={t}")
    
    while True:
        # Check if we need to adjust s for optimality in the next step
        if t > 65536:
            s = s + 32768 - (t // 2)
            print(f"Adjusted s to {s} (t > 65536)")
        
        j += 1
        d = s // 65536
        
        # Check the invariant
        invariant1 = 0 <= d <= 9
        invariant2 = s > 2**16 * d
        invariant3 = s - t < 2**16 * d + 2**16
        invariant_satisfied = invariant1 and invariant2 and invariant3
        
        print(f"Iteration {j}: d={d}, s={s}, t={t}")
        print(f"  Invariant checks: 0<=d<=9: {invariant1}, s>2^16*d: {invariant2}, s-t<2^16*d+2^16: {invariant3}")
        print(f"  Overall invariant satisfied: {invariant_satisfied}")
        
        if not invariant_satisfied:
            print(f"  WARNING: Invariant violated!")
        
        digits.append(d)
        s = 10 * (s % 65536)
        t = 10 * t
        
        if s <= t:
            break
    
    # Format the result as a decimal fraction
    decimal = "." + "".join(str(d) for d in digits)
    return decimal, digits, j

# Test with n = 8132
result, digits, k = knuth_p2(8132)
print("\nResult for n=8132:")
print(f"Decimal fraction: {result}")
print(f"Digits: {digits}")
print(f"k (number of digits): {k}")

# For manual verification, let's compute n/2^16 directly
exact_value = 8132 / 2**16
print(f"\nExact value of n/2^16: {exact_value}")
decimal_value = float(result)
print(f"Our decimal representation as float: {decimal_value}")
print(f"Difference: {abs(exact_value - decimal_value)}")

# Let's also implement the P1 algorithm to convert back
def knuth_p1(decimal_str):
    """
    Implements Knuth's P1 algorithm to convert a decimal fraction
    back to n/2^16 form.
    
    The algorithm processes digits from right to left (last to first).
    """
    # Remove the decimal point
    digits = decimal_str.strip('.')
    l = min(len(digits), 17)
    m = 0
    
    # Process digits from right to left (last to first)
    for i in range(l-1, -1, -1):
        d = int(digits[i])
        m = (131072 * d + m) // 10
    
    n = (m + 1) // 2
    return n

# Check if our decimal converts back correctly
converted_n = knuth_p1(result)
print(f"\nConverting back using P1: {converted_n}")
print(f"Original n: 8132")
print(f"Match: {converted_n == 8132}")