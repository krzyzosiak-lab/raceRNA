# raceRNA
f1=open((input('File name with sequences(FASTA format):')),'r')
repeat=str(input('Examined repeat:'))
repeat_size=int(input('Min repeat tract size:'))
file_out=str(input('Name of results file:'))

a=f1.readlines()
f1.close()
word=repeat*(repeat_size+1)
unit_length=len(repeat)
d={}
for i in range(0,unit_length): #frame dictionary generator
    d["frame{0}".format(i)]=word[i:-(unit_length-i)]

ile=1
for i in a:
    if ile%2==1: #sequence header
        ii=i.split('|')
        name=ii[0].strip('\n')
    else: #sequence row
        for j in list(d.values()): #extracting all possible variants of the SSR motif
            if j in i:
                f2=open(file_out,'a')
                f2.write(name+'\n'+i)
                f2.close()
                break
    ile+=1
