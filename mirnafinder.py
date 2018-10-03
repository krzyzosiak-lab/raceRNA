#raceRNA
f1=open((input('File name with mature miRNA sequences(FASTA format):')),'r')
while True:
    repeat=str(input('Examined repeat (3-6 nt long):'))
    if len(repeat)>6 or len(repeat)<3:
        print('Sorry, examined repeat size need to be between 3 and 6 nt.')
        continue
    else:
        break
file_out=str(input('Name of results file:'))

rev=repeat[::-1] #reversing repeat and subsequent steps to make reverse complement
rev=rev.replace('A','V')
rev=rev.replace('T','A')
rev=rev.replace('U','A')
rev=rev.replace('V','U')
rev=rev.replace('G','D')
rev=rev.replace('C','G')
rev=rev.replace('D','C')

a=f1.readlines()
f1.close()

if len(rev)==3:
    rev=rev+rev
elif len(rev)==4:
    rev=rev+rev[0:2]
else:
    rev=rev+rev[0:1]

word=rev*2
unit_length=len(rev)
d={}
for i in range(0,unit_length): #frame dictionary generator
    d["frame{0}".format(i)]=word[i:-(unit_length-i)]

exist=False
ile=1
for i in a:
    if ile%2==1: #sequence header
        ii=i.split('|')
        name=ii[0].strip('\n')
    else: #sequence row
        for j in list(d.values()): #extracting all possible variants of the SSR motif
            seed=i[1:8] #extracting seed sequence (nucleotides position 2-7)
            if j in seed:
                f2=open(file_out,'a')
                f2.write(name+'\n'+i)
                f2.close()
                exist=True
                break
    ile+=1

if exist==False: #if no miRNAs with matches were found generate a file reporting no matches
    f2=open(file_out,'a')
    f2.write('No matches between miRNA sequences and the chosen repeat were found')
    f2.close()
