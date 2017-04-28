import re
import xlsxwriter

workbook=xlsxwriter.Workbook('data_new.xlsx')
worksheet=workbook.add_worksheet()
i=0
game=0
wmove=0
bmove=0

f=open('10kprocess.txt','r')
found=1
str_move=''
ignore=0
count=0
for fi in iter(f):
    if len(fi.strip()) == 0 :   #string is empty
        found=0
        ignore=0
    else:
        if found==1 and ignore==0:
            if(count >= 15):
                ignore=1
                count=0
                
            

            if re.search('[0-9]+[\.][ ][A-Z]?[a-z]+[0-9]',fi):
                count=count+1
                index1=fi.find('{')
                move=fi[0:index1]
                str_move=str_move+move
                #print (str_move)
                
                index2=fi.find('-')
                index3=fi.find('+')
                if index2!=-1:
                    index4=fi.find(']')
                    if index4!=-1:
                        eval_score=fi[index2:index4]
                elif index3!=-1:
                    if index3<index1:
                        index3=fi.find('+',index3+1)
                    index4=fi.find(']')
                    if index4!=-1:
                        eval_score=fi[index3:index4]

                wmove=wmove+1
                print(game,end=' '),
                
                print(wmove)   
                
                worksheet.write(i,0, game)
                worksheet.write(i,1, str(wmove)+"a")
                worksheet.write(i,2, str_move.strip())
                worksheet.write(i,3, eco)
                worksheet.write(i,4, eval_score)
                worksheet.write(i,5, welo)
                worksheet.write(i,6, ans)
                i=i+1         
            elif re.search('[0-9]+[\.][ ][\.][\.][\.][ ][O][-][O]',fi):
                count=count+1
                index1=fi.find('{')
                move=fi[0:index1]
                str_move=str_move+move
                #print (str_move)
                
                index2=fi.find('-',index1+1)
                index3=fi.find('+')
                if index2!=-1:
                    index4=fi.find(']')
                    if index4!=-1:
                        eval_score=fi[index2:index4]
                elif index3!=-1:
                    if index3<index1:
                        index3=fi.find('+',index3+1)
                    index4=fi.find(']')
                    if index4!=-1:
                        eval_score=fi[index3:index4]

                wmove=wmove+1
                print(game,end=' '),
                
                print(wmove)   
                
                worksheet.write(i,0, game)
                worksheet.write(i,1, str(wmove)+"a")
                worksheet.write(i,2, str_move.strip())
                worksheet.write(i,3, eco)
                worksheet.write(i,4, eval_score)
                worksheet.write(i,5, welo)
                worksheet.write(i,6, ans)
                i=i+1
                
            elif re.search('[0-9][\.] [\.][\.][\.][ ][A-Z]?[a-z]+[0-9][+]?',fi):
                count=count+1
                index1=fi.find('{')
                if index1==-1:
                    continue
                index1=fi.find('{')
                move=fi[0:index1]
                str_move=str_move+move
                #print (str_move)
                
                index2=fi.find('-')
                index3=fi.find('+')
                if index2!=-1:
                    index4=fi.find(']')
                    eval_score=fi[index2:index4]
                elif index3!=-1:
                    if index3<index1:
                        index3=fi.find('+',index3+1)
                        
                    index4=fi.find(']')
                    eval_score=fi[index3:index4]
                
                bmove=bmove+1
                print(game,end=' '),
                
                print(bmove)
                
                worksheet.write(i,0, game)
                worksheet.write(i,1, str(bmove)+"b")
                worksheet.write(i,2, str_move.strip())
                worksheet.write(i,3, eco)
                worksheet.write(i,4, eval_score)
                worksheet.write(i,5, belo)
                worksheet.write(i,6, ans)
                i=i+1
            elif re.search('[0-9]+[\.][ ][\.][\.][\.][ ][O][-][O]',fi):
                count=count+1
                index1=fi.find('{')
                if index1==-1:
                    continue
                index1=fi.find('{')
                move=fi[0:index1]
                str_move=str_move+move
                #print (str_move)
                
                index2=fi.find('-')
                index3=fi.find('+')
                if index2!=-1:
                    index4=fi.find(']')
                    eval_score=fi[index2:index4]
                elif index3!=-1:
                    if index3<index1:
                        index3=fi.find('+',index3+1)
                        
                    index4=fi.find(']')
                    eval_score=fi[index3:index4]
                
                bmove=bmove+1
                print(game,end=' '),
                
                print(bmove)
                
                worksheet.write(i,0, game)
                worksheet.write(i,1, str(bmove)+"b")
                worksheet.write(i,2, str_move.strip())
                worksheet.write(i,3, eco)
                worksheet.write(i,4, eval_score)
                worksheet.write(i,5, belo)
                worksheet.write(i,6, ans)
                i=i+1
                
            elif re.search('[R][e][s][u][l][t] ".+"',fi):
                print ("---------------------------------------------------------------------------------------")
                
                if fi.find("1/2-1/2")!=-1:
                    ans=0.5
                elif fi.find("0-1")!=-1:
                    ans=0
                elif fi.find("1-0")!=-1:
                    ans=1
                #print (ans)
            elif re.search('[W][h][i][t][e][E][l][o] ".+"',fi):
                lst=re.findall('[0-9]+',fi)
                string=lst[0]
                welo=(int(string))
            elif re.search('[B][l][a][c][k][E][l][o] ".+"',fi):
                lst=re.findall('[0-9]+',fi)
                string=lst[0]
                belo = (int(string))
            elif re.search('[E][C][O] ".+"',fi):
                lst=re.findall('[A-Z][0-9]+',fi)
                eco=lst[0]                
                    
        elif found==0:
            if fi[0:2]=='1.':
                game=game+1
                
                               
                found=1 #create new game anaylysis
                str_move=''
                index1=fi.find('{')
                move=fi[0:index1]
                str_move=str_move+move
                #print (str_move)
            
                
                index2=fi.find('-')
                index3=fi.find('+')
                if index2!=-1:
                    index4=fi.find(']')
                    if index4!=-1:
                        eval_score=fi[index2:index4]
                    
                        
                elif index3!=-1:
                    if index3<index1:
                        index3=fi.find('+',index3+1)
                    index4=fi.find(']')
                if index4!=-1:
                    
                        
                    eval_score=fi[index2:index4]

                wmove=wmove+1
                print(game,end=' '),
                
                print(wmove)
                
                worksheet.write(i,0, game)
                worksheet.write(i,1, str(wmove)+"a")
                worksheet.write(i,2, str_move.strip())
                worksheet.write(i,3, eco)
                worksheet.write(i,4, eval_score)
                worksheet.write(i,5, welo)
                worksheet.write(i,6, ans)
                i=i+1
            
            
            elif fi[0]=='[':
                if re.search('[R][e][s][u][l][t] ".+"',fi):
                  
                    if fi.find("1/2-1/2")!=-1:
                        ans=0.5
                    elif fi.find("0-1")!=-1:
                        ans=0
                    elif fi.find("1-0")!=-1:
                        ans=1
                    print (ans)
                elif re.search('[W][h][i][t][e][E][l][o] ".+"',fi):
                    lst=re.findall('[0-9]+',fi)
                    string=lst[0]
                    welo=string
                elif re.search('[B][l][a][c][k][E][l][o] ".+"',fi):
                    lst=re.findall('[0-9]+',fi)
                    string=lst[0]
                    belo=string
                elif re.search('[E][C][O] ".+"',fi):
                    lst=re.findall('[A-Z][0-9]+',fi)
                    string=lst[0]
                    eco=string
            else:
                
                found=1
        
workbook.close()

                
