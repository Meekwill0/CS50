def main():
    x=int(input("what's x? "))
    print("EVEN") if is_even(x) else print("ODD")


def is_even(n):
    return n%2==0 
    

main()