# Title: String Matching
# Time: 2020/10/14
# Author: Vincent

# BF算法
def bf_matching(s1, s2):
    a, b, c = 0, 0, 0
    res = []
    while a + len(s2) - 1 < len(s1):
        if s1[b] == s2[c]:
            b += 1
            c += 1
            if c == len(s2):
                res.append(a)
                a += 1
                c = 0
                b = a
        else:
            a += 1
            b = a
            c = 0
    return res


# KMP算法
def get_next(s):
    j = 0
    n = len(s)
    pnext = [0, 0]
    for i in range(1, n):
        while j > 0 and s[j] != s[i]:
            j = pnext[j]
        if s[j] == s[i]:
            j += 1
        pnext.append(j)
    return pnext
        
def kmp_matching(s1, s2):
    n, m = len(s1), len(s2)
    pnext = get_next(s2)
    j = 0
    for i in range(1, n):
        while j > 0 and s1[i] != s2[j]:
            j = pnext[j]
        if s1[i] == s2[j]:
            j += 1
            if j == len(s2):
                return i - m + 1
    return -1
    
    

if __name__ == '__main__':
    s1 = 'abcdefgbcdehhhhbcde'
    s2 = 'abcabcbac'
    print(bf_matching(s1, s2))
    print(get_next(s2))
    print(kmp_matching(s1, s2))
    