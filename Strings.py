
def string_before(str1, str2, case_sensitive = True):
    s1=str1
    s2=str2
    if case_sensitive == True:
        s1 = str1
        s2 = str2
    else:
        s1=str1.lower()
        s2=str2.lower()

    if s2 in s1:
        i=s1.find(s2)
        S=str1[:i]
    else:
        S = ''
    return S

def string_after(str1,str2, case_sensitive = True):
    s1=str1
    s2=str2
    if case_sensitive == True:
        s1 = str1
        s2 = str2
    else:
        s1=str1.lower()
        s2=str2.lower()

    if s2 in s1:
        i=s1.find(s2)
        S=str1[i+len(s2):]
    else:
        S = ''
    return S


str1 = "aaabbbaaaaaaaBbbaaaaa"
str2 = "Bbb"

print string_before(str1,str2,False)
print string_after(str1,str2,False)