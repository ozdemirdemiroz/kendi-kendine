import numpy as np

# from numpy import random
liste = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"liste\n {liste}\n")

liste2 = np.array([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)])
print(f"liste2\n {liste2}\n")

print(f"liste2.shape: \t {liste2.shape}")
print(f"liste2.size : \t {liste2.size} \n")

liste3 = np.arange(20)

print(f"liste3\n {liste3}\n")

liste3 = liste3.reshape(4, 5)#4 satır 5 stün olacak şekilde tekrar şekillendir
print(f"liste3.reshape\n {liste3}\n")

random_matris = np.random.randint(20, 70, 15) # 20 ile 70 arasında 15 tane sayı üret
random_matris = random_matris.reshape(5,3)
random_matris
print(f"random_matris\n {random_matris}\n")

print ("Arimetrik:\t", np.mean(random_matris))
print ("Medyan:\t\t", np.median(random_matris))
print("Varyans:\t", np.var(random_matris))
print("Standart Sapma:\t", np.std(random_matris))



print(np.eye(5))