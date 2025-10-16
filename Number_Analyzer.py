def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def is_perfect(n):
    return n==sum(i for i in range(1,n) if n%i == 0)
def is_palindrome(n):
    s = str(n)
    return s==s[::-1]
def is_armstrong(n):
    s = str(n)
    length=len(s)
    return n==sum(int(d)**length for d in s)
def is_perfect_square(n):
    return int(n**0.5)**2==n
def number_analyzer():
    n=int(input("Enter a number:--"))
    print("prime" if is_prime(n) else "not prime")
    print("perfect" if is_perfect(n) else "not perfect")
    print("even" if n % 2 == 0 else "odd")
    print("palindrome" if is_palindrome(n) else "not palindrome")
    print("armstrong" if is_armstrong(n) else "not armstrong")
    print("perfect square" if is_perfect_square(n) else "not perfect square")
number_analyzer()