# x: int = 0


# def f() -> None:
#   x: int = 1


# f()
# print(x)

x: str = "global"


def test(para: str) -> str:
    # global x
    x = "local_global"
    print(x)
    return(x)


print(x)
test("argument")
print(x)