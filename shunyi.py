




import csv
import random

    

alpha = 0.0001


def createMatrix(A, B , operation):   
    
    if operation == 'random':
        random_matrix = []
        for i in range (A):
            rowList = []
            for j in range (B):
                rowList.append(random.random())
            random_matrix.append(rowList)
        
        return random_matrix 
    
    if operation == 'multiply':
    
        if len(A[0]) != len(B):
            assert 'incorrect dimensions'
    
        new_matrix = []
        for i in range(len(A)):
            Row = []
            for j in range(len(B[0])):
                q = 0
                for k in range(max(len(A[0]), len(B))):
                    q += A[i][k] * B[k][j]
                Row.append(q)
            new_matrix.append(Row)
        return new_matrix
    
    if operation == 'minus':
        if len(A[0]) != len(B[0]) or len(A) != len(B):
            assert 'incorrect dimensions'
    
        new_matrix = []
        for i in range(len(A)):
            Row = []
            for j in range(len(A[0])):
                q = A[i][j] - B[i][j]
                Row.append(q)
            new_matrix.append(Row)
        return new_matrix
    
    if operation == 'plus':
        if len(A[0]) != len(B[0]) or len(A) != len(B):
            assert 'incorrect dimensions'
    
        new_matrix = []
        for i in range(len(A)):
            Row = []
            for j in range(len(A[0])):
                q = A[i][j] + B[i][j]
                Row.append(q)
            new_matrix.append(Row)
        return new_matrix
    
    
    
    
def ChangeMatrix ( A , operation):
    
    if operation == 'transpose':
        Transpose = []
        for _ in range(len(A[0])):
            tR = []
            for _ in range(len(A)):
                tR.append(None)
            Transpose.append(tR)
    
        for i in range(len(A[0])):
            for j in range(len(A)):
                Transpose[i][j] = A[j][i]
        return Transpose
    
    if operation == 'scalar_multiply':
        new_matrix = []
        for i in range(len(A)):
            Row = []
            for j in range(len(A[0])):
                q = A[i][j] * alpha
                Row.append(q)
            new_matrix.append(Row)
        return new_matrix
         
    
def Loss(e):
    loss = []
    for i in e:
        sampleLoss = 0
        for j in i:
            sampleLoss += j
        loss.append(sampleLoss)
    return sum(loss) / len(loss)   
    


 
    
with open('PRSA_Data_Shunyi_20130301-20170228.csv','r') as shunyi:
    
    reader = csv.reader(shunyi, delimiter=',', quotechar='|')
    
    
    input_dataset=[]
    output_dataset=[]
    # here I wanna read each row of the dataset
    for i, row in enumerate(reader):
        input_sample=[]
        output_sample=[]
        if i > 0 :
            NA_value=False
            for N_column , value in enumerate(row):
                if value == 'NA':
                    NA_value = True
                    break
                if N_column in [2, 4, 11, 12, 13, 16]:
                    input_sample.append(float(value))
                if N_column in [5,6,7,8,9,10]:
                    output_sample.append(float(value))
            
            if NA_value == False:
                input_dataset.append(input_sample)
                output_dataset.append(output_sample)           


for i in input_dataset:
    i.append(1)

X = input_dataset
Y = output_dataset
B= createMatrix (7,6, 'random')




Episode = 0
while Episode < 100:
    
    y = createMatrix(X, B , 'multiply')
    Error = createMatrix(Y, y, 'minus')
    delta = createMatrix(ChangeMatrix(X , 'transpose'), Error,'multiply')
    delta = ChangeMatrix(delta , 'scalar_multiply')
    B = createMatrix(B, delta , 'plus')
    loss = Loss(Error)
#    
    print('Episode: %d, Loss value is: %.4f' % (Episode, loss))
#    
    Episode+=1
    print(Episode)
#    
#    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



























                
                