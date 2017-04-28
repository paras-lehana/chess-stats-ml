#code to count no of lines in the file
count=0
with open ('nitin.txt','rb') as f:
    for line in f:
        count+=1


f=open('nitin.txt','r')
count=count-3
d={}
for i in range(count):
    
    fi=f.readline()
    if i != 0:
        lst=(fi.split())
        st=str(lst[4])
            
        st=st.strip('%')
        
        d[float(st)]=str(lst[1])
        
print ('the ouptut of dict is')
for key in sorted(d):
    print (key, d[key])