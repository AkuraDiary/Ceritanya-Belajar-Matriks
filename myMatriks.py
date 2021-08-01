"""class matriksnya"""

class matriks:

  ## constructor ##

  def __init__(self, val=[[]]):

    ## Attribut array/matriksnya ##
    self.Array = val
    ## Atribut pendukung ##
    self.baris, self.kolom = 0, 0
    self.main_diagonal=[]
    self.secondary_diagonal=[]
    self.Arr_Transpose = []

    row = len(val)
    #untuk membuat matriks sesuai jumlah baris & memasukkan data dari parameter

    #generating ordo & diagonal
    self.baris = row#len(self.Array)
    self.kolom = 0
    if self.notEmpty():
      self.kolom= len(self.Array[0])
    
    #generating diagonal if baris & kolom nilainya sama (matriks persegi)
    self._generate_diagonal()

  ## constructor ##

  """ INI BATAS HEHE """

  ## method method ##
  def jumlah_baris(self):
    return len(self.Array)
  
  # method cek matriks persegi
  def _is_persegi(self):
    if self.baris == self.kolom:
      return True
    else:
      return False

  #method untuk mengecek apakah matriksnya kosong
  def notEmpty(self):
    if len(self.Array):
      return True
    else:
      return False

  # get ordo of the matriks
  def ordo(self):
    return self.baris, self.kolom

  # method generate diagonal (private)
  def _generate_diagonal(self):
    if self._is_persegi():#checking matrix type
      print(self.ordo())
      # main diagonal
      for i in range(self.baris):
        self.main_diagonal.append(self.Array[i][i])
      #secondary diagonal
      s_target = self.kolom -1
      for j in range(self.baris):
        self.secondary_diagonal.append(self.Array[j][s_target])
        s_target -=1
    else:
      pass
    
  #get diagonal
  def diagonal(self):
    return self.main_diagonal, self.secondary_diagonal
  
  # get item from specific location
  def get_item(self, baris, kolom):
    try:
      return self.Array[baris][kolom]
    except IndexError:
      return "item tidak ditemukan, coba cek baris dan kolom anda"
  
  #method untuk set item into specific location
  def set_item(self, baris, kolom, value):
    try:
      self.Array[baris][kolom] = value
    except IndexError:
      return "tempat item tidak ditemukan, coba cek baris dan kolom anda"
  
  # # method untuk mendapatkan elemen baris & kolom # #
  #untuk baris
  def get_elemen_baris_ke(self, baris): 
    return self.Array[baris]
  def get_elemen_kolom_ke(self, kolom):
    res = []
    for i in range(self.baris):
      res.append(self.Array[i][kolom])
    return res

  #method untuk transpose matriks
  def transpose(self):
    _kolom = self.kolom
    _baris = self.baris
    #creating the column / preparing
    for i in range(_kolom):
      self.Arr_Transpose.append([])
    
    #inserting the item
    target_item=0
    for j in range(_kolom):      
      for k in range(_baris):
        #print(k, target_item, j)
        self.Arr_Transpose[j].append(self.get_item(k, target_item)) 
      target_item += 1
      
    return self.Arr_Transpose #matriks(self.Arr_Transpose) #return object
   

#you know what it is
if __name__ == "__main__":
  A = matriks(row=4, column=4)
  print(A.Array)
  print(A.jumlah_baris())
  print(A.ordo())
  print(A.diagonal())
