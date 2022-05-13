
def valicacion(n):
    try:
        n= int(n)
    except ValueError:
        print("mal")
    else:
        if n>0:
            print("ok")

valicacion("hola")
