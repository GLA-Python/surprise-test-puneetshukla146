def expanding(l):
        diff= l[1]-l[0]
        for i in range(2,len(l)):
            if abs(l[i]-l[i-1])>diff:
                diff=abs(l[i]-l[i-1])
            else:
                return False
        return True    
#
def rotate(m):
    n=[[0 for i in range(len(m))] for i in range(len(m))]
    for i in range(len(m)):
            for j in range(len(m)):
                n[i][j]=m[j][i]
    for i in range(len(n)):
             n[i]=n[i][::-1]
    return n     
#
def accordian(l):
        try:
            diff= abs(l[1]-l[0])
            if abs(l[2]-l[1])>diff:
                flag = True
            else:
                flag = False
        except IndexError:
            return True
        
        for i in range(2,len(l)):
            if flag and  abs(l[i]-l[i-1])>diff:
                      diff=abs(l[i]-l[i-1])
                      flag = not flag 
            elif not flag and abs(l[i]-l[i-1])<diff:            
                      diff=abs(l[i]-l[i-1])
                      flag= not flag
                        
            else:    
                      return False
            
        return True      