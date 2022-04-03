import math
from multiprocessing.dummy import Event
from os import system
import pygame
from pygame.locals import *

wide=600
height=400
color=(250, 11, 8 )



crash=False
pygame.init()
surf=pygame.display.set_mode((wide, height))


class figura:
    def __init__(self,nom,alto,x,y, color):
        self.nom=nom
        self.alto=alto
        self.x=x
        self.y=y
        self.perimetro=0
        self.area=0
        self.color=color

    def getNombre(self):
        return self.nom
    def getAlto(self):
        return self.alto
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getPerimetro(self):
        return self.perimetro
    def getArea(self):
        return self.area
    
    def setNombre(self, x):
        self.nom=x
    def setAlto(self, x):
            self.alto=x
    def setPerimetro(self, x):
            self.perimetro=x
    def setArea(self, x):
            self.area=x
    def setX(self,i):
        self.x=i
    def setY(self,j):
        self.y=j
            
    def calcularPF(self):
        P=self.alto*4
        self.setPerimetro(P)
        print("El perimetro es :", self.getPerimetro()) 
    
    def calcularAF(self):
        A=self.alto*self.alto
        self.setArea(A)
        print("El area es :", self.getArea())

    def draw(self):
        pygame.draw.rect(surf,self.color,[self.x, self.y,self.alto,self.alto])
    
class Triangulo(figura):
    def __init__(self, base, nom, alto,x,y, color ):
        figura.__init__(self,nom,alto,x,y, color)
        self.base=base
        self.tipo=" "
        
    def getBase(self):
        return self.base
    def getTipo(self):
        return self.tipo
    
    def setBase(self, x):
            self.base=x
    def setTipo(self,x):
            self.tipo=x
    
         
    def calulaA(self):
        A=(self.base*self.alto)/2
        self.setArea(A)
        print("El area es :",self.getArea())
    
    def calulaP(self):
        P=self.base*3
        self.setPerimetro(P)
        print("El perimetro es :", self.getPerimetro()) 
  
    def draw(self):
            pygame.draw.polygon(surf,self.color,[[self.x, self.y],[ (self.x+(self.base/2)), (self.y-self.alto)], [(self.x+self.base), self.y]])
      
class trianguloIsosceles(Triangulo):
    def __init__(self, lado2, base,nom,alto,x,y,color):
        Triangulo.__init__(self,base, nom, alto,x,y,color )
        self.lado2=lado2
        
    def getlado2(self):
            return self.lado2
    def setlado2(self, x):
            self.lado2=x  
             
    def calulaPTI(self):
        P=self.base+(self.lado2 * 2)
        self.setPerimetro(P)
        print("El perimetro es :", self.getPerimetro()) 
        
    def draw(self):
             pygame.draw.polygon(surf,self.color,[[self.x, self.y],[ (self.x+(self.base/2)), (self.y-self.alto)], [(self.x+self.base), self.y]])
      
class trianguloEscaleno(trianguloIsosceles):
    def __init__(self, lado3,lado2, base,nom,alto,x,y,color):
        trianguloIsosceles.__init__(self,lado2, base,nom,alto,x,y,color)
        self.lado3=lado3
        
    def getlado3(self):
            return self.lado2
    def setlado3(self, x):
            self.lado2=x  
    
    def calulaPTE(self):
        P=self.base+self.lado2+self.lado3
        self.setPerimetro(P)
        print("El perimetro es :", self.getPerimetro())    
           
    def draw(self):
            pygame.draw.polygon(surf,self.color,[[self.x, self.y],[ (self.x+self.lado3), (self.y-self.alto)], [(self.x+self.base), self.y]])
      
            
class Rectangulo(figura):
    def __init__(self, nom, alto, x,y,color,largo):
        self.largo=largo
        figura.__init__(self,nom,alto, x, y, color)
        
    def getlargo(self):
            return self.largo
    def setlargo(self, x):
            self.largo=x 
            
    def calcularPR(self):
        P=(self.alto*2)+(self.largo*2)
        self.setPerimetro(P)
        print("El perimetro es :", self.getPerimetro()) 
    
    def calcularAR(self):
        A=self.alto*self.largo
        self.setArea(A)
        print("El area es :", self.getArea())
    def draw(self):
            pygame.draw.rect(surf,self.color,[self.x, self.y,self.alto,self.largo])    
       
class Circulo(figura):
    def __init__(self, nom, alto,x,y,color):
        figura.__init__(self,nom,alto,x,y,color)
        self.radio=0
       
        
    def getRadio(self):
            return self.radio
    def setRadio(self, x):
            self.radio=x 
    def calcularPC(self):
        P=(self.alto*3.1416)
        self.setPerimetro(P)
        print("El perimetro es :", self.getPerimetro()) 
    
    def calcularAC(self):
        r=self.alto/2
        self.setRadio(r)
        A=(3.1416)*(math.pow(self.getRadio(),2))
        self.setArea(A)
        print("El area es :", self.getArea()) 
  
    def draw(self):
        pygame.draw.circle(surf,self.color,(self.x, self.y),self.alto/2) 

class Trapecio(figura):
    def __init__(self, nom, alto,x,y,color, bMayor,bMenor,lados):
        figura.__init__(self,nom,alto, x,y,color)
        self.bMayor=bMayor
        self.bMenor=bMenor
        self.lados=lados
        
    def getBMayor(self):
            return self.bMayor
    def getBMenor(self):
            return self.bMenor
    def getLados(self):
        return self.lados
    def setBMayor(self, x):
            self.bMayor=x
    def setBMenor(self, x):
            self.bMenor=x 
    def setLados(self,x):
            self.lados=x
            
    def calcularPT(self):
        P=self.bMayor+self.bMenor+(self.lados*2)
        self.setPerimetro(P)
        print("El perimetro es :", self.getPerimetro()) 
    
    def calcularAT(self):
        A=((self.alto)*(self.bMayor+self.bMenor))/2
        self.setArea(A)
        print("El area es :", self.getArea()) 
    
    def draw(self):
        pygame.draw.polygon(surf,self.color,[[self.x, self.y],[(self.x+((self.bMayor-self.bMenor)/2)),(self.y-self.alto)],[(self.x+self.bMenor), (self.y-self.alto)],[(self.x+self.bMayor), self.y]])
      
class Rombo(figura):
    def __init__(self, nom, alto,x,y,color, Dm,lado):
        figura.__init__(self,nom,alto,x,y,color)
        self.Dmenor=Dm
        self.lado=lado
        
    def getDmenor(self):
            return self.Dmenor
    def getLado(self):
            return self.lado
    def setDmenor(self, x):
            self.bMayor=x
    def setLado(self, x):
            self.lado=x 
            
    
    def calcularAR(self):
        A=(self.alto*self.Dmenor)/2
        self.setArea(A)
        print("El area es :", self.getArea())    
        
    def draw(self):
        pygame.draw.polygon(surf,self.color,[[self.x, self.y],[ (self.x+(self.alto/2)), (self.y-self.alto)], [(self.x+self.alto), self.y], [ (self.x+(self.alto/2)), (self.y+self.alto)]])
       
        
triangulo1=Triangulo(60,"yellow",50,220,175,(101,200,250))
pos_x2=triangulo1.getX()
pos_y2=triangulo1.getY()
print("<-- Triangulo Equilatero -->")
triangulo1.calulaP()
triangulo1.calulaA()

triangulo2=trianguloIsosceles(70,40,"violet",50,290,175,(101,200,250))
pos_x3=triangulo2.getX()
pos_y3=triangulo2.getY()
print("<-- Triangulo Isosceles -->")
triangulo2.calulaPTI()
triangulo2.calulaA()

triangulo3=trianguloEscaleno(60,45,100,"pink",30,340,175,(101,200,250))
pos_x4=triangulo3.getX()
pos_y4=triangulo3.getY()
print("<-- Triangulo Escaleno -->")
triangulo3.calulaPTE()
triangulo3.calulaA()

cuadrado1=figura("rojo",50,160,125,(101,200,250))
pos_x=cuadrado1.getX()
pos_y=cuadrado1.getY()
print("<-- Cuadrado -->")
cuadrado1.calcularPF()
cuadrado1.calcularAF()

rectangulo1=Rectangulo("rojo",70,80,125,(101,200,250),50) 
pos_x7=rectangulo1.getX()
pos_y7=rectangulo1.getY()
print("<-- Rectangulo -->")
rectangulo1.calcularPR()
rectangulo1.calcularAR()

circle1=Circulo("ostia",50,50,150,(101,200,250))
pos_x1=circle1.getX()
pos_y1=circle1.getY()
print("<-- Circulo -->")
circle1.calcularPC()
circle1.calcularAC()

trapecio1=Trapecio("white",50,450,175,(101,200,250),80,70,40)
pos_x5=trapecio1.getX()
pos_y5=trapecio1.getY()
print("<-- Trapecio -->")
trapecio1.calcularPT()
trapecio1.calcularAT()

rombo1=Rombo("Orange",40,550,150,(101,200,250),20,30)
pos_x6=rombo1.getX()
pos_y6=rombo1.getY()
print("<-- Rombo -->")
rombo1.calcularPF()
rombo1.calcularAR()


while not(crash):
    
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            crash=True
        if evento.type==pygame.KEYDOWN: 
           if evento.key==pygame.K_a:
               pos_x1+=5
           if evento.key==pygame.K_q:
                   pos_y1-=5       
           if evento.key==pygame.K_d:
                pos_x+=5
           if evento.key==pygame.K_e:
                   pos_y-=5      
           if evento.key==pygame.K_f:
                   pos_x2+=5
           if evento.key==pygame.K_r:
               pos_y2-=5  
           if evento.key==pygame.K_g:
                pos_x3+=5
           if evento.key==pygame.K_t:
               pos_y3-=5     
           if evento.key==pygame.K_h:
                pos_x4+=5
           if evento.key==pygame.K_y:
               pos_y4-=5        
           if evento.key==pygame.K_j:
                    pos_x5+=5
           if evento.key==pygame.K_u:
               pos_y5-=5     
           if evento.key==pygame.K_k:
                    pos_x6+=5
           if evento.key==pygame.K_i:
               pos_y6-=5  
           if evento.key==pygame.K_s:
                    pos_x7+=5
           if evento.key==pygame.K_w:
               pos_y7-=5  
               
    cuadrado1=figura("rojo",50,pos_x,pos_y,(101,200,250))   
    circle1=Circulo("ostia",50,pos_x1,pos_y1,(101,200,250))  
    triangulo1=Triangulo(60,"yellow",50,pos_x2,pos_y2,(101,200,250))     
    triangulo2=trianguloIsosceles(70,40,"violet",50,pos_x3,pos_y3,(101,200,250)) 
    triangulo3=trianguloEscaleno(60,45,100,"pink",30,pos_x4,pos_y4,(101,200,250))
    trapecio1=Trapecio("white",50,pos_x5,pos_y5,(101,200,250),80,70,40)
    rombo1=Rombo("Orange",40,pos_x6,pos_y6,(101,200,250),20,30)  
    rectangulo1=Rectangulo("rojo",70,pos_x7,pos_y7,(101,200,250),50)
    surf.fill(color)
    circle1.draw()
    rectangulo1.draw()
    cuadrado1.draw()
    triangulo1.draw()
    triangulo2.draw()
    triangulo3.draw()
    rombo1.draw()
    trapecio1.draw()
    pygame.display.update()
pygame.quit
system.exit(0)