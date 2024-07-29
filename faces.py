def main():
    text=input()
    result=convert(text)
    print(result)


def convert(text):
    sms1=text.replace(":)",'🙂')
    sms2=sms1.replace(":(",'🙁')
    return sms2


main()

