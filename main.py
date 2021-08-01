import myMatriks as M #importing myMatriks library
# program latihan matriks 
# part 1

""" ARRAY INDEX START AT 0 """ # reminder
Data = [
  [3, 6, -12, 16, 20],
  [-2, 7, 4, 6, -3]
] 
Data_2 = [
  [3, -2], 
  [6, 7], 
  [-12, 4], 
  [16, 6], 
  [20, -3]
]
A = M.matriks(val = Data) #objek matriks
print("matriks : ", A.Array)
print("Ordo : ", A.ordo())
print("diagonal [main][secondary]: ", A.diagonal())
B = A.transpose()
print(B)
C = M.matriks(val = Data_2)
A_Transpose = M.matriks(B)
print("matriks transpose : ", A_Transpose.Array)

