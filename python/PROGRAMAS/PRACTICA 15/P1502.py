def produ(n1,n2):
	if (len(str(n1)) == 1 or len(str(n2)) == 1):
		return n1*n2
	else:
		n = max(len(str(n1)),len(str(n2)))
		n12 = n / 2
		
		a = n1 / 10**(n12)
		b = n1 % 10**(n12)
		c = n2 / 10**(n12)
		d = n2 % 10**(n12)
		
		ac = produ(a,c)
		bd = produ(b,d)
		ad = produ(a+b,c+d) - ac - bd
        
		prod = ac * 10**(2*n12) + (ad * 10**n12) + bd

		return prod
#Programa principal
print "========MULTIPLICACION DIVIVDE Y VENCERAS=========="
n1=int(raw_input("Ingrese multiplicando: "))
n2=int(raw_input("Ingrese multiplicador: "))
print "RESULLTADO: ",produ(n1, n2)

