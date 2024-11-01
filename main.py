def reverse_string(s):
    """Reverses a given string."""
    return s[::-1]

def is_palindrome(word):
    """Checks if a word is a palindrome."""
    cleaned_word = word.lower().replace(" ", "")
    return cleaned_word == cleaned_word[::-1]

def fibonacci(n):
    """Generates first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Test the functions
def main():
    print("Reverse String Tests:")
    print(reverse_string("Fiona"))  # Should print: anoiF
    print(reverse_string("Nolvine"))  # Should print: enivloN

    print("\nPalindrome Tests:")
    print(is_palindrome("radar"))   # Should print: True
    print(is_palindrome("hello"))   # Should print: False
    print(is_palindrome("A man a plan a canal Panama"))  # Should print: True

    print("\nFibonacci Tests:")
    print(fibonacci(6))  # Should print: [0, 1, 1, 2, 3, 5]
    print(fibonacci(10))  # Should print longer sequence

# Run the main function
if __name__ == "__main__":
    main()