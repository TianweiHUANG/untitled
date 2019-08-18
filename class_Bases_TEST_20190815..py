"""
 object
   H
D     G
C     F
B     E
   A
"""
class H(object):
    #pass
    def test(self):
        print("test in H..")
class G(H):
    pass
    #def test(self):
        #print("test in G..")
class F(G):
    pass
    #def test(self):
        #print("test in F..")
class E(F):
    pass
    #def test(self):
        #print("test in E..")
class D(H):
    pass
    #def test(self):
        #print("test in D..")
class C(D):
    pass
    #def test(self):
        #print("test in C..")
class B(C):
    pass
    #def test(self):
        #print("test in B..")
class A(B,E):
    pass
    #def test(self):
        #print("test in A..")
a=A()
a.test()