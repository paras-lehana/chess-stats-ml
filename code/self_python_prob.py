f=open("prob.txt","r")
count=0
white_win=0
draw_win=0
black_win=0
total=0
for i in range(3):
    
    li=f.readline()
    
    if(count==2):
        lst=li.split(" ")
        white_win=float(lst[17])
        draw_win= float(lst[20])
        black_win= float(lst[24])
    count=count+1
total=white_win+black_win+draw_win
white=float((white_win*float(100))/total)
draw=float((draw_win*float(100))/total)
black=float((black_win*float(100))/total)
print ('the chances of white win are',white,'%')
print ('chances of draw are',draw,'%')
print ('chances of black win are',black,'%')