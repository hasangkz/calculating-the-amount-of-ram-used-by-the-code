import tracemalloc                                                                      #Ram miktarını ölçmek için kullanılan kütüphane
import matplotlib.pyplot as plt                                                         #Grafik çizdirmek için kullanılan kütüphane


def recursionFibonacci(n):                                                              #Recursive fonksiyon ile fibonacci serisini bulma
   if n <= 1:
       return n
   else:
       return(recursionFibonacci(n-1) + recursionFibonacci(n-2))                        #Fibonacci hesabının yapılması

iter2 = 5                                                                               #Recursive olarak kaç adım bulunacağını tutan değişken
recursiveMemory = []                                                                    #3 farklı adımı hesaplarken kullanılan ram miktarlarını tutan dizi
recursiveIteration = []                                                                 #Ram miktarlarını hesaplarken kullanılan adım sayısını tutan dizi grafik çizdirmek için gerekli
for i in range(3):                                                                      #Recursive fonksiyonda 3 farklı değer için memeory kullanımını bulan döngü
    tracemalloc.start()                                                                 #Kullanılan memory bulmak için kullanılan özel fonksiyon başlangıcı
    recursiveIteration.append(iter2)                                                    #Grafik çizdirmek için kullanılan değerlerin listeye atılması

    for i in range(iter2):                                                              #Fibonacci serisini bulmak için çağrılan fonksiyon
            recursionFibonacci(i)

    current, recursivePeak = tracemalloc.get_traced_memory()                            #Kullanılan memoryi bulan özel fonksiyon
    recursiveMemory.append(recursivePeak / 10**6)
    tracemalloc.stop()
    iter2 *= 2                                                                          #Denenilen değerlerin arttırılması



iter = 10                                       #iterative olarak hesaplanılacak ram miktarları için kaç adım hesaplanacağını tutan değişken (İterative fonksiyon çok daha az yer kapladığı için daha büyük sayılar ile işlem yapıyoruz)
iterativeMemory = []                                                                    #İterative olarak fibonacci hesaplanırken kullanılan memorylerin dizide tutulması   
iterativeIteration = []                                                                 #iterative olarak fibonacci hesabında kaç adım hesaplandıysa onları tutan dizi grafik çizdirmek için gerekli
for j in range(3):                                                                      #Iterative fonksiyonda 3 farklı değer için memeory kullanımını bulan döngü
    tracemalloc.start()                                                                 #Kullanılan memory bulmak için kullanılan özel fonksiyon başlangıcı
    iterativeIteration.append(iter)                                                     #Grafik çizdirmek için kullanılan değerlerin listeye atılması
    first = 1                                                                           #Fibonacci serisinin ilk elemanı
    second = 1                                                                          #Fibonacci serisinin ikinci elemanı

    for i in range(iter):                                                               #Fibonacci serisinin iterative olarak bulunması
        third = first + second                                                          #Fibonacci serisinde sonraki elemanın hesaplanması
        #print(third)
        first = second                                                                  #Her döngü bittiğinde sonraki elemanlar önceki elemanlara eşit oluyo
        second = third

    current, iterativePeak = tracemalloc.get_traced_memory()                            #Kullanılan memoryi bulan özel fonksiyon
    iterativeMemory.append(iterativePeak / 10**6)
    iter *= 10                                                                          #Denenilen değerlerin arttırılması
    tracemalloc.stop()


print(iterativeMemory)                                                                  #Grafik çizdirme işlemleri
plt.subplot(1,2,1)
plt.stem(iterativeIteration,iterativeMemory)                                            #Grafik çizdiren kod
plt.title("Iterative Fonksiyon")                                                        #Grafikleri isimlendirme
plt.xlabel("Iteration")
plt.ylabel("MB")



plt.subplot(1,3,3)
plt.stem(recursiveIteration,recursiveMemory)                                            #Grafik çizdiren kod
plt.title("Recursive Fonksiyon")                                                        #Grafikleri isimlendirme
plt.xlabel("Iteration")
plt.ylabel("MB")
plt.show()

