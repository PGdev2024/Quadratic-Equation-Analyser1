import math
class Analyser:
   def __init__(self,a,b,c):
      self.a=a
      self.b=b
      self.c=c
   def Discriminant(self):
      D=self.b**2 - 4*self.a*self.c
      if D < 0 :
         return D,"Discriminant is negative"
      if D > 0 :
         if math.isqrt(D)==math.sqrt(D):
           return D,"Discriminant is positive and a perfect square"
         else:
           return D,"Discriminant is positive and not a perfect square"
      if D == 0:
         return D,"Discriminant is zero"
   def vertex(self):
      Vx=-self.b/(self.a*2)
      Vy=-(self.b**2 - 4*self.a*self.c)/self.a*4
      return Vx,Vy
   def roots(self):
      D=self.b**2 - 4*self.a*self.c
      if D>0:
        x1=(-self.b+math.sqrt(D))/(self.a*2)
        x2=(-self.b-math.sqrt(D))/(self.a*2)
        if math.sqrt(D)==math.isqrt(D):
           return "The roots are real and rational",x1,x2
        else:
           return "The roots are real and irrational",x1,x2
      if D<0:
         x1=str(-self.b/(self.a*2))+"+"+str(math.sqrt(-D)/(self.a*2))+"i"
         x2=str(-self.b/(self.a*2))+"-"+str(math.sqrt(-D)/(self.a*2))+"i"
         return "The roots are complex and conjugates of each other",x1,x2
      if D==0:
         root=-self.b/(self.a*2)
         return "There is a single repeated root",root
   def intercept(self):
      ic=self.c
      return ic
   def Direction(self):
      if self.a>0:
         return "Opening Upwards"
      if self.a<0:
         return "Opening Downwards"
   def AnalyserC(self):
      Disc,DiscN=self.Discriminant()
      VX,VY=self.vertex()
      rootsN=self.roots()
      Ic=self.intercept()
      Dir=self.Direction()
      if len(rootsN)==3:
         rN,r1,r2=rootsN
         return {"Discriminant":Disc,
                 "Nature of Discriminant":DiscN,
                 "Vertex X Coordinate":VX,
                 "Vertex Y Coordinate":VY,
                 "Intercept":Ic,
                 "Direction":Dir,
                 "Nature of Roots":rN,
                 "Root1":r1,
                 "Root2":r2}
      else:
         rN,r=rootsN
         return {"Discriminant":Disc,
                 "Nature of Discriminant":DiscN,
                 "Vertex X Coordinate":VX,
                 "Vertex Y Coordinate":VY,
                 "Intercept":Ic,
                 "Direction":Dir,
                 "Nature of Roots":rN,
                 "Root":r}
      
                 
