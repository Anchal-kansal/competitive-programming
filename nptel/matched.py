def matched(s):
    for i in s:
        j=0
        if i == "(":
            j=j+1
        elif i == ")":
            j=j-1
            if j<0:
                return(False)
    return(True)