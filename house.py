name=input("Whats your name? ")

match name:
    case "Willy" | "Gitau" | "Ngigi":
        print("Sosian")
    case _:
        print("Unkown")
        