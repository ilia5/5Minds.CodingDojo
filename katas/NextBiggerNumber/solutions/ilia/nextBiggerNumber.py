def nextBigger(n):
    sol = -1 # The solution
    num = list(str(n)) # Numbers list
    for i in range(len(num)-1 ,0, -1): 
        if (num[i-1] < num[i]):
            minInt = num[i] 
            minIntIndex = i
            for j in range(i,len(num)): # Searching for smaller number bigger than the selected one
                if (num[i-1] < num[j]):
                    if (num[j] < minInt):
                        minInt = num[j]
                        minIntIndex = j
            num[minIntIndex], num[i-1] = num[i-1], num[minIntIndex]
            
            for k in range(i,len(num)): # Bubble sorting the right numbers
                for l in range(i, len(num)-1):
                    if num[l] > num[l + 1] :
                        num[l], num[l+1] = num[l + 1], num[l]
            sol = ''.join(num) # Converting the list to string
            return sol
    return sol 
    
print(nextBigger(59884848459853)) # Getting the expected result!
