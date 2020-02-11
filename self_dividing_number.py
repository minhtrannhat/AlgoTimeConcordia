def selfDividingNumbers(left: int, right: int): 
        output = []
        for i in range(left, right + 1, 1):
            for ch in str(i):
                if int(ch)==0 or i % int(ch)!=0:
                    break
            else:
                output.append(i)
        
        return output

print(selfDividingNumbers(1, 22))
print(selfDividingNumbers(1500, 1600))

