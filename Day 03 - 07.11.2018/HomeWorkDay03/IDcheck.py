def checkLimit(IDnum):
    Len = len(IDnum)
    if Len > 9:
        print ("Please enter up to 9 digits!")
        main()
    else:
        IDconvert(IDnum)
def IDconvert(IDnum):
    IDnumINT = [0,0,0,0,0,0,0,0,0]
    Len = len(IDnum)-1
    Arr = [int(i) for i in IDnum]
    for i in range(0,Len+1):
        IDnumINT[8-i] = Arr[Len-i]
    IDWeights(IDnumINT)
def IDWeights(IDnum):
    arr1 = 1,2,1,2,1,2,1,2,1
    arr2 = [0,0,0,0,0,0,0,0,0]
    Len = len(IDnum)-1
    for i in range(0,Len+1):
        arr2[Len-i] = IDnum[Len-i]*arr1[Len-i]
    SumID(arr2)
def SumID(IDnum):
    Sum=0
    Len = len(IDnum)-1
    for i in range (0,Len+1):
        if IDnum[i] > 9:
            x = (IDnum[i] %10)+ IDnum[i]//10
            Sum+=x
        else:
            Sum+=IDnum[i]
    checkID(Sum)
def checkID(Sum):
    if Sum % 10 == 0:
        print ("The ID number is valid")
    else:
        print ("The ID number is incorrect!")

def main():
    IDnum=input("Enter an ID number: ")
    checkLimit(IDnum)
main()  