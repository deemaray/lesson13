def quadraticcFormula1(a,b,c):
    delta = b**2 - 4*a*c  # calculating the discriminant
    if delta >=0:         # checking if the discriminant is not a negative num
        root1= (-b + delta**0.5 / 2*a)   # calculating the first root
        return (root1)
    else:
        return None



def quadraticcFormula2(a,b,c):
    delta = b**2 - 4*a*c  # calculating the discriminant
    if delta >=0:         # checking if the discriminant is not a negative num
        root2 = (-b + delta**0.5 / 2*a)    # calculating the second root
        return (root2)
    else:
        return None

 # Testing
a = 4
b = 6
c = 2

root1 = quadraticcFormula1(a, b, c)
print("root 1:", root1)

root2 = quadraticcFormula2(a,b,c)
print("root2:", root2 )
quit()



