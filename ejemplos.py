#ejemplo 4


def convertir_a_segundos(h,m,s):

    return h* 3600 + m * 60 +s

def convertir_a_HMS(seg):
    h = seg//3600
    seg = seg - h *3600
    m = seg//60
    seg = seg - m*60
    s = seg

    return h,m,s

while True:
    print("1.convertir a segundos")
    print("2. convertir a horas, minutos y segundos")
    print("3. salir")

    opcion = int(input())

    if opcion ==1:
        hor = int(input("Horas:"))
        minu = int(input("minutos:"))
        minu = int(input("segundos:"))
        print("corresponde a", hor, ":", minu,)