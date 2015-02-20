ERR_MSG = 'Invalid Input  '

def main():
    try:
        n = int(raw_input())
        d = int(raw_input())
    except:
        print ERR_MSG
        quit()
    if not (0 < n <= 100):
        print ERR_MSG
        quit()
    if not (0 < d <= 100):
        print ERR_MSG
        quit()
    ans = work(n, d)
    print ans

def work(n, dd):
    obtain = 100 - n
##    obtain = n
##    print obtain
    if not 6 <= obtain <= 63:
        return 'Invalid Input'
    st = [1, 2, 4, 8, 16, 32]
    d = 63 - obtain
##    print d
    i = 5
    while d > 0:
##        print i, d
        cal = 2 ** i - 1
        if d > cal:
            st[i] -= cal
            d -= cal
        else:
            st[i] -= d
            d -= cal
        i -= 1
##        d -= 2 ** i - 1
##        if d < 0:
##            d = 0
##        st[i] -= d
##        i -= 1
##    print st
    st.append(n)
    st.sort()
    final = list()
    ans = str()
    for val in st:
        ans += str(val) + ' '
    ans.strip()
    ans += '\n'
    i = 6
##    print st
    while dd > 0:
        if st[i] <= dd:
            dd -= st[i]
            final.append(st[i])
##            print st[i], i, dd
        i -= 1
    for val in sorted(final):
        ans += str(val) + ' '
    ans.strip()
    return ans

main()
