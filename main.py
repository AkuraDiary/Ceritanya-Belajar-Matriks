import myMatriks as M #importing myMatriks library
# program latihan matriks 
# part 1

""" ARRAY INDEX START AT 0 """ # reminder
Data = [
  [3, 6, -12, 16, 20],
  [-2, 7, 4, 6, -3]
] 

A = M.matriks(val = Data) #objek matriks
print("matriks : ", A.Array)
print("Ordo : ", A.ordo())
print("diagonal [main][secondary]: ", A.diagonal())
B = M.matriks(A.transpose())
print("matriks transpose : ", B.Array)
# masih eror
C = M.matriks(B.transpose())
print(C.Array) 

