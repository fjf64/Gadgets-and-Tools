try: 
    a = float(input("Measure of INterior Angle, enter nothing to find EXterior:"))
except:
    try:
        almost_a = float(input("Measure of EXterior Angle"))
        a = 180-almost_a
    except:
        pass
b = 180-a
c = (360) / b
print(c)