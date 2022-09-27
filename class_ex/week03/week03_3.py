from re import I


def pal(s):
    k=""
    for i in s:
        if i!=" " and i!=".":
            k+=i
    k=k.lower()
    return k==k[::-1]


print(pal("asD    d  d ds.....a"))

put=input("입력하세요:")
print(pal(put))