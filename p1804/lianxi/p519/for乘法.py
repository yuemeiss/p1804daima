import sys,time
for i in range(1,10):
    for a in range(1,i+1):
        print("%d ×　%d = %d"% (a,i,a*i),end='\t')
        sys.stdout.flush()
        time.sleep(0.1)
    print("")

