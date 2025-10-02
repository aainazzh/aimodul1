# Easy level

# Test case 1: Even or Odd
def check_even_odd(n): return f"The number is {'Even' if n % 2 == 0 else 'Odd'}"

# Test
print(check_even_odd(4))  # Expected: The number is Even
print(check_even_odd(7))  # Expected: The number is Odd


# Test case 2: Positive, Negative, or Zero
def check_number(n): return f"The number is {'Positive' if n > 0 else 'Negative' if n < 0 else 'Zero'}"

# Test
print(check_number(10))  # Expected: The number is Positive
print(check_number(-5))  # Expected: The number is Negative
print(check_number(0))   # Expected: The number is Zero


# Medium level

# Test case 3: Anagram
def is_anagram(str1, str2): return sorted(str1) == sorted(str2)

# Test
print(is_anagram("listen", "silent"))  # Expected: True
print(is_anagram("hello", "world"))    # Expected: False


# Test case 4: Factorial
def factorial(n): return 1 if n == 0 else n * factorial(n-1)

# Test
print(factorial(5))  # Expected: 120
print(factorial(0))  # Expected: 1


# Hard level

# Test case 5: Palindrome
def is_palindrome(s): return s == s[::-1]

# Test
print(is_palindrome("racecar"))  # Expected: True
print(is_palindrome("python"))   # Expected: False
print(is_palindrome("habibah"))  # Expected: True


# Test case 6: Armstrong number
def is_armstrong(n): return n == sum(int(d)**len(str(n)) for d in str(n))

# Test
print(is_armstrong(153))  # Expected: True
print(is_armstrong(370))  # Expected: True
print(is_armstrong(123))  # Expected: False


# Expert level

# Test case 7: Bank Account
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Invalid withdrawal amount or insufficient funds"

# Test
account = BankAccount("Name")
print(account.deposit(1000))   # Expected: Deposited 1000. New balance: 1000
print(account.withdraw(500))   # Expected: Withdrew 500. New balance: 500
print(account.withdraw(600))   # Expected: Invalid withdrawal amount or insufficient funds


# Test case 8: Student
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        return f"Grade {grade} added."

    def get_average(self):
        return f"Average grade: {sum(self.grades) / len(self.grades):.1f}"

# Test
student = Student("Alice")
print(student.add_grade(90))  # Expected: Grade 90 added.
print(student.add_grade(80))  # Expected: Grade 80 added.
print(student.add_grade(70))  # Expected: Grade 70 added.
print(student.get_average())  # Expected: Average grade: 80.0
