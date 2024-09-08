import re

class MyFunctions:

    @staticmethod
    def is_nan(num):
        """Check if the number is NaN."""
        return num != num
    
    @staticmethod
    def is_even(num):
        """Check if the number is even."""
        return isinstance(num, int) and (num & 1) == 0
    
    @staticmethod
    def is_odd(num):
        """Check if the number is odd."""
        return not MyFunctions.is_even(num)
    
    @staticmethod
    def is_hex(value):
        """Check if the value is a valid hexadecimal number (0x prefix)."""
        return bool(re.match(r'^0[xX][0-9a-fA-F]+$', value))
    
    @staticmethod
    def is_octal(value):
        """Check if the value is a valid octal number (0o prefix)."""
        return bool(re.match(r'^0[oO][0-7]+$', value))

    @staticmethod
    def is_binary(value):
        """Check if the value is a valid binary number (0b prefix)."""
        return bool(re.match(r'^0[bB][01]+$', value))
    
    @staticmethod
    def is_list(value):
        """Check if the value is a list."""
        return isinstance(value, list)

    @staticmethod
    def is_tuple(value):
        """Check if the value is a tuple."""
        return isinstance(value, tuple)
    
    @staticmethod
    def is_dict(value):
        """Check if the value is a dictionary."""
        return isinstance(value, dict)
    
    @staticmethod
    def is_set(value):
        """Check if the value is a set."""
        return isinstance(value, set)

    @staticmethod
    def is_js_safe_integer(num):
        """Check if the value is falls within the JS safe integer range."""
        JS_SAFE_INTEGER_MAX = 2**53 - 1

        return isinstance(num, int) and abs(num) <= JS_SAFE_INTEGER_MAX

    @staticmethod
    def is_float(value):
        """Check if the value is a float."""
        return isinstance(value, float)
    
    @staticmethod
    def is_negative_number(value):
        """Check if the value is a negative number (int or float)."""
        return isinstance(value, (int, float)) and value < 0
    
    @staticmethod
    def sign(value):
        """Check the sign of the value."""
        if isinstance(value, (int, float)):
            return 1 if value > 0 else -1 if value < 0 else 0
        return float('nan')

    @staticmethod
    def is_power_of_two(value):
        """Check if the value is a power of two."""
        return isinstance(value, int) and value > 0 and (value & (value - 1)) == 0

    @staticmethod
    def is_power_of_three(value):
        """Check if the value is a power of two."""
        if not isinstance(value, int) and value <= 0:
            return False
        
        while value % 3 == 0:
            value //= 3

        return value == 1

# Test Cases
def test_my_functions():
    # Testing is_nan
    print("Testing is_nan:")
    print(MyFunctions.is_nan(float('nan')))  # True
    print(MyFunctions.is_nan(1))             # False
    print(MyFunctions.is_nan('nan'))         # False (string 'nan')

    # Testing is_even
    print("\nTesting is_even:")
    print(MyFunctions.is_even(2))  # True
    print(MyFunctions.is_even(3))  # False
    print(MyFunctions.is_even(2.2))  # False


    # Testing is_odd
    print("\nTesting is_odd:")
    print(MyFunctions.is_odd(2))  # False
    print(MyFunctions.is_odd(3))  # True
    print(MyFunctions.is_even(3.2))  # False

    # Testing is_hex
    print("\nTesting is_hex:")
    print(MyFunctions.is_hex("0x1a2b"))   # True
    print(MyFunctions.is_hex("0XABCDEF")) # True
    print(MyFunctions.is_hex("123"))      # False
    print(MyFunctions.is_hex("0x1G2"))    # False

    # Testing is_octal
    print("\nTesting is_octal:")
    print(MyFunctions.is_octal("0o123"))  # True
    print(MyFunctions.is_octal("0O456"))  # True
    print(MyFunctions.is_octal("123"))    # False
    print(MyFunctions.is_octal("0o89"))   # False

    # Testing is_binary
    print("\nTesting is_binary:")
    print(MyFunctions.is_binary("0b1010"))  # True
    print(MyFunctions.is_binary("0B0011"))  # True
    print(MyFunctions.is_binary("1010"))    # False
    print(MyFunctions.is_binary("0b102"))   # False

    # Testing is_list
    print("\nTesting is_list:")
    print(MyFunctions.is_list([1, 2, 3]))  # True
    print(MyFunctions.is_list((1, 2, 3)))  # False
    print(MyFunctions.is_list("hello"))    # False

    # Testing is_tuple
    print("\nTesting is_tuple:")
    print(MyFunctions.is_tuple([1, 2, 3]))  # False
    print(MyFunctions.is_tuple((1, 2, 3)))  # True
    print(MyFunctions.is_tuple("hello"))    # False

    # Testing is_dict
    print("\nTesting is_dict:")
    print(MyFunctions.is_dict({'a': 1}))    # True
    print(MyFunctions.is_dict([1, 2, 3]))  # False
    print(MyFunctions.is_dict("hello"))    # False

    # Testing is_set
    print("\nTesting is_set:")
    print(MyFunctions.is_set({1, 2, 3}))   # True
    print(MyFunctions.is_set([1, 2, 3]))  # False
    print(MyFunctions.is_set("hello"))    # False

    # Testing is_js_safe_integer
    print("\nTesting is_js_safe_integer:")
    print(MyFunctions.is_js_safe_integer(12))   # True
    print(MyFunctions.is_js_safe_integer(12_448_494_123_258_848_949)) # False
    print(MyFunctions.is_js_safe_integer("yj6j")) # False

    # Testing is_float
    print("\nTesting is_float:")
    print(MyFunctions.is_float(12))   # False
    print(MyFunctions.is_float(1.12)) # True
    print(MyFunctions.is_float("yj6j")) # False

    # Testing is_negative_number
    print("\nTesting is_negative_number:")
    print(MyFunctions.is_negative_number(-5))         # True (negative int)
    print(MyFunctions.is_negative_number(-5.5))       # True (negative float)
    print(MyFunctions.is_negative_number(5))          # False (positive int)
    print(MyFunctions.is_negative_number(5.5))        # False (positive float)
    print(MyFunctions.is_negative_number(0))          # False (zero)
    print(MyFunctions.is_negative_number(3 + 4j))    # False (complex number)
    print(MyFunctions.is_negative_number('string'))   # False (string)

    # Testing sign
    print("\nTesting sign:")
    print(MyFunctions.sign(5))           # 1
    print(MyFunctions.sign(-5))          # -1
    print(MyFunctions.sign(0))           # 0
    print(MyFunctions.sign('string'))    # nan

    # Testing is_power_of_two
    print("\nTesting is_power_of_two:")
    print(MyFunctions.is_power_of_two(1))         # True
    print(MyFunctions.is_power_of_two(2))         # True
    print(MyFunctions.is_power_of_two(3))         # False
    print(MyFunctions.is_power_of_two(16))        # True

    # Testing is_power_of_three
    print("\nTesting is_power_of_three:")
    print(MyFunctions.is_power_of_three(1))         # True
    print(MyFunctions.is_power_of_three(3))         # True
    print(MyFunctions.is_power_of_three(9))         # True
    print(MyFunctions.is_power_of_three(27))        # True
    print(MyFunctions.is_power_of_three(2))         # False
    print(MyFunctions.is_power_of_three(10))        # False


# Run the tests
test_my_functions()








    




