import time
root = int(input())
secs = int(input())
def aoao(root,secs) :
    time.sleep(secs / 1000)
    ans = (root)**0.5
    print (f'Square root of {root} after {secs} milliseconds is {ans}')
aoao(root,secs)