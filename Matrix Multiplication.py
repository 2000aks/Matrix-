m1 = [[1,2,4,2],
      [2,5,5,1],
      [1,2,3,4],
      [5,6,8,9]]
m2 = [[1],
      [0],
      [0],
      [0]]

def matrix_mul(mat1,mat2):
    if len(mat1[0]) == len(mat2):        
        result = []        
        for i in range (len(mat1)):
            lst = []  
            for j in range(len(mat2[0])):
                temp = 0
                for k in range(len(mat2)):   
                    aij = mat1[i][k]*mat2[k][j]
                    temp = temp+aij
                lst.append(temp)   
            result.append(lst)     
        for f in range(len(mat1)):
            print(result[f])   
    else:
        print("Multiplication is not possible")    
           
matrix_mul(m1,m2) 


