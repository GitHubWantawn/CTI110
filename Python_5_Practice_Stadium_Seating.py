






class_A = int(input("Enter tickets sold for Class A: "))

class_B = int(input("Enter tickets sold for Class B: "))

class_C = int(input("Enter tickets sold for Class C: "))

def expenses(a, b, c):

    total_A = a * 20
    total_B = b * 15
    total_C = c * 10

    total = total_A + total_B + total_C

    print("Profit generated from Class A =",total_A)
    print("Profit generated from Class B =",total_B)
    print("Profit generated from Class C =",total_C)
    print("\nOverall Profit generated =",total)





expenses(class_A, class_B, class_C)
