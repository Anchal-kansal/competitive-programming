def matmult(m1,m2):
  mult=[len(m2[0])*[0] for i in range(0,len(m1))]
  for i in range(0,len(m1)):
    for j in range(0,len(m2[0])):
      mult[i][j]=0
      for k in range(0,len(m1[0])):
        mult[i][j]=mult[i][j]+m1[i][k]*m2[k][j]
  return(mult)
