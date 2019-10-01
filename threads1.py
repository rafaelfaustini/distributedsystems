from threading import Thread
def PrintHello(tid):
        global subtotal
        soma = 0
	for i in range (5):
	    soma+=i
        subtotal+=soma
        
subtotal=0
threads=[]
for i in range (5):
	print ("Criando thread "+str(i))
	threads.append(Thread(target=PrintHello,args=(i,)))
	threads[-1].start()
for i in range(5):
    threads[i].join()
print(subtotal)
