import numpy as np
def f(mat):
   return (mat[0]**2 -mat[1]**2+5*mat[2]**3)
def finite_difference(f,x, epsilon = 0.5e-5):
    grad = [0]*len(x)
    for i in range(len(x)):
        xplus = x.copy()
        xminus = x.copy()
        xplus[i] += epsilon
        xminus[i] -= epsilon
        grad[i] = (f(xplus)-f(xminus))/(epsilon*2)
    return grad
step = 0.1
input =  [5,7,8]
print(finite_difference(f,input))
# for b in range(1000):
#     gradv = finite_difference(f,input )
#     for i in range(len(gradv)):
#        input[i] = input[i]- step*gradv[i]
# print(input)
# def unflatten(mat):
#     if (len(mat)%2 != 0):
#         raise ValueError("The array must have an even amount of entries.")
#     y=[]
#     x=[]
#     for i in range(0,len(mat)):
#         if (i%2 != 0):
#             y.append(mat[i])
#         else:
#             x.append(mat[i])
#     arr = np.column_stack((x,y))
#     return arr.tolist()
# chub =[5,6,7,8,2,5,76,22]
# lub = unflatten(chub)
# print(lub)
# flat = [item for sublist in lub for item in sublist]
# print(flat)