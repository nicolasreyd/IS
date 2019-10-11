#Devuelve que tipo de triangulo es, antes valida que sea un triangulo
def getTypeofTriangule(x,y,z):
    if isTriangule(x,y,z):
        if x == y == z:
            return "Equilatero"
        elif x==y or y==z or z==x:
            return "Isosceles"
        else:
            return "Escaleno" 
    else:
        return "No es un triangulo"    

#Valida las propiedades de los lados de un triangulo
def isTriangule(x,y,z):
     if (x>y+z) or (y>z+x) or (z>x+y):
        return False
     elif (x==z+y) or (y==x+z) or (z==x+y):
        return True     
     else:
        return True