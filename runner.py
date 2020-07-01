### This program sorts through two inventory list and merges the rows that have the same upc

#########*       ###########*      ####*        ####"
#########*       ###########*      ####*        ####"
##3    3#*          33333*         3333*        3333"
##3    3#*          33333*         3333*        3333"
##333333333*        33333*         3333*        3333"
##3     333*        33333*         3333*        3333"
##3     333*        33333*         33333*      3333"
##333333333*     ###########*       33333333333333"
###########*     ###########*        ############"

# Big Inventory Unifier 0.2
# Runner File

# Designed and Tested by MCM-Lucky

from difflib import SequenceMatcher
import data

print "BIU Version 0.2 ALPHA"
print ""
print "Created by MCM-Lucky - 2016"
print ""

def sim(a, b):
	return SequenceMatcher(None, a, b).ratio()

x = 0
y = 0
check = 0
hcount = 0
ycount = 0
ncount = 0
bcount = 0
done=[]
notdone=[]
donehf=[]
hfu=[]
notdonehf=[]
hf = data.hf
bwgs = data.bwgs
txt = open("unified", "w")
donestr = ""

print txt

raw_input("Press Enter to Begin")
print "Intializing",
print ".",
print ".",
print ".",
print ".",
print "."

for u in range(len(hf)):
    if len(hf[u]) > 8:
       hf[u][3] = hf[u][3] + hf[u][4]
       del hf[u][4]

for q in range(len(bwgs)):
    if len(bwgs[q]) > 8:
     bwgs[q][3] = bwgs[q][3] + bwgs[q][4]
     del bwgs[q][4]


for i in range(len(hf)):
    if data.hfbrands[0] == data.hf[i][2] or data.hfbrands[1] == data.hf[i][2] or data.hfbrands[2] == data.hf[i][2] or data.hfbrands[3] == data.hf[i][2] or data.hfbrands[4] == data.hf[i][2] or data.hfbrands[5] == data.hf[i][2] or data.hfbrands[6] == data.hf[i][2] or data.hfbrands[7] == data.hf[i][2] or data.hfbrands[8] == data.hf[i][2] or data.hfbrands[9] == data.hf[i][2] or data.hfbrands[10] == data.hf[i][2] or data.hfbrands[11] == data.hf[i][2] or data.hfbrands[12] == data.hf[i][2] or data.hfbrands[13] == data.hf[i][2] or data.hfbrands[14] == data.hf[i][2] or data.hfbrands[15] == data.hf[i][2] or data.hfbrands[16] == data.hf[i][2] or data.hfbrands[17] == data.hf[i][2] or data.hfbrands[18] == data.hf[i][2]:
        done.append(data.hf[i])
    else:
        hfu.append(hf[i])

print "Total Number of Products:",
print len(hf)
print "Not Unique:",
print len(hfu)
print "Unique:",
print len(done)

raw_input("Distributor 2 Sprecific Seperation Complete - Press Enter to Continue to UPC Matching")


for index in range(len(bwgs)):
    if bwgs[index][5] == "":
        bcount = bcount + 1
    else:
        for index2 in range(len(hfu)):
            if bwgs[index][5] == hfu[index2][5]:
                ##print "MATCH CONFIRMED: " + data.bwgs[index][0] + "|" + hfu[index2][1]
                bwgs[index][1] = hfu[index2][1]
                ycount =  ycount + 1
                done.append(data.bwgs[index])
                donehf.append(hfu[index2])
     
print "Matched:",
print ycount
print "Complete:",
print len(done)

raw_input("UPC Matching Complete - Press Enter to Continue to Results")

c = len(done)

for index3 in range(len(bwgs)):
        for index4 in range(len(done)):
            if bwgs[index3][0] != done[index4][0]:
               c = c - 1
               if c == 0:
                   notdone.append(bwgs[index3])
                   c = len(done)
            else:
                c = len(done)
                break

d = len(donehf)

for index5 in range(len(hfu)):
        for index6 in range(len(donehf)):
            if hfu[index5][1] != donehf[index6][1]:
               d = d - 1
               if d == 0:
                   notdonehf.append(hfu[index5])
                   d = len(donehf)
            else:
                d = len(donehf)
                break
            


tcount = ycount + ncount + bcount
#Result posting
print "RESULTS"
print "Matched:",
print ycount
print "Complete:",
print len(done)
print "Blank UPC: ",
print bcount
print "Incomplete",
print len(notdone)
print "First Distrib. Complete:",
print len(donehf)
print "First Distrib. Not Complete:",
print len(notdonehf)

#Discription comparison
cont =raw_input("Intiate Simularity Based Matching? (Y/N)")
if cont == "n":
    for s in range(len(done)):
        donestr = donestr + "[" 
        donestr = donestr + ",".join(done[s]) + "]"
    txt.write(donestr)
    txt.close()
    print y
    exit()
elif cont == "y":
    for index6 in range(len(notdone)):
		for index7 in range(len(notdonehf)):
			sucrat = sim(notdone[index6][3], notdonehf[index7][3])
			if sucrat >= 0.9:
				print notdone[index6][3] +" " + notdonehf[index7][3]
				print 
			if sucrat >= 0.75:
				print notdone[index6][3] +" " + notdonehf[index7][3]
			        match =raw_input("Match? (Y/N)")
			        if match == "y":
			            notdone[index6][1] = notdonehf[index7][1]
			            done.append(notdone[index6])
			            donehf.append(notdonehf[index7])

##sim(notdone[index6][3], notdonehf[index7][3])
