def greet(input):
    if "hello" in input:
      return"hello, there"
    else:
       return"I'm not sure what you mean"


def main():
   greeting = greet("hey")
   print( greeting + ", Will")

main()