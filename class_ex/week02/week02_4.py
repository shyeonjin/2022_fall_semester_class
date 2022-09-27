def calc(first,second,tool):
    if tool=="+":
        return first+second
    elif tool=="-":
        return first-second
    elif tool=="*":
        return first*second
    else:
        return first/second
first,second,tool=input("적으세요:").split()
first=int(first)
second=int(second)
print(calc(first,second,tool))
