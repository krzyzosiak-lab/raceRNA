#raceRNA
f1=open((input('TargetScan result file name:')),'r')
f3=open((input('File name of file with miRNA names: miR-[number] format (eg. miR-940), each miRNA in separate line:')),'r')
zm=int(input('Min. MRE number in RNA sequence:'))
file_out=str(input('Name of results file:'))
counting=0
cerna_list=[]
poz_list=[]
jest=False

list_mirna=[]
z=f3.readlines()
for i in z:
    list_mirna.append(i.strip('\n')+'/')

a=f1.readline()
while a!='':
    aa=a.split('\t')
    cerna=aa[0]
    mirna=aa[1]
    for i in list_mirna: #sprawdzanie listy mirna potencjalnie wiazacych sie do danego ciagu powtorzen
        if i in mirna: #if miRNA is on the list
            poz=int(aa[3]) #MRE position
            for j in poz_list:
                if j>=poz and j<=poz+6: #if there is another miRNA @ position
                    jest=True
            if jest==False:
                cerna_list.append(i) #adding miRNA to the list
                counting+=1
            poz_list.append(poz)
    b=f1.readline()
    bb=b.split('\t')
    if bb[0]==aa[0]: #if there is still the same miRNA
        a=b
        jest=False
    else: #summary of the RNA seq (ceRNA)
        if len(cerna_list)>=zm: #write to file if fulfills criteria
            f2=open(file_out,'a')
            jakie_mirna=''
            for j in cerna_list:
                jakie_mirna+=j+' '
            f2.write(cerna+'\t'+str(counting)+'\t'+jakie_mirna+'\n')
            f2.close()
            a=b #going to next RNA
            counting=0
            cerna_list=[]
            poz_list=[]
            jest=False
        else:
            a=b
            counting=0
            cerna_list=[]
            poz_list=[]
            jest=False
            
        
