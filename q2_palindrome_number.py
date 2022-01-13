"""# leetcode palindrome number"""

def run(num):
    """
    :type: int
    :rtype: bool
    """
    if(num < 0) or (num % 10 == 0 and num != 0):
        return False
    reversed_number = 0
    while num > reversed_number:
        reversed_number = reversed_number*10 + num % 10
        num = int(num/10)
    print(num)
    print(reversed_number)
    return num == reversed_number or num == int(reversed_number/10)
