def fizzbuzz_checker(limit):
    for i in range(1, limit + 1):
        if ((i % 3) == 0) and ((i % 5) == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
            
print("FizzBuzz from 1 to 20:")      
fizzbuzz_checker(20)