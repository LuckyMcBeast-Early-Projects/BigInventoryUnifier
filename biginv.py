import data

hf = data.hf
bwgs = data.bwgs
hfbrands = data.hfbrands

def datafix(a, b, c):
	data = a
	for u in range(len(a)):
		if len(a[u]) > c:
			data[u][b] = a[u][b] + a[u][b+1]
			del data[u][b+1]
	return data
	
def truedata(a, b):
	boo = True
	for x in range(len(a)):
		if len(a[x]) > b:
			boo = False
	return boo

def datacheck(a, b, c):
	data = a
	count = 0
	if truedata(a, c) == True:
		return data
	else:
		while truedata(data, c) == False:
			data = datafix(a, b, c)
			count += 1
			print count
	return data

####################################
newdata = datacheck(hf, 3, 8)
test = truedata(newdata, 8)
print test
####################################
print len(hf)

def unmatched(a, b, c): #a is main file, b is matched file, c is key (0)
	l = len(b)
	unmat = []
	for index3 in range(len(a)):
		for index4 in range(len(b)):
			if a[index3][c] != b[index4][c]:
				l = l - 1
				if l == 0:
					unmat.append(a[index3])
					l = len(b)
			else:
				l = len(b)
				break
	return unmat
	
def uniquebrands(a, b, c):
	done = []
	notdone = []
	real = a
	for x in range(len(b)):
		for i in range(len(a)):
			if b[x] in a[i]:
		#if data.hfbrands[0] == data.hf[i][2] or data.hfbrands[1] == data.hf[i][2] or data.hfbrands[2] == data.hf[i][2] or data.hfbrands[3] == data.hf[i][2] or data.hfbrands[4] == data.hf[i][2] or data.hfbrands[5] == data.hf[i][2] or data.hfbrands[6] == data.hf[i][2] or data.hfbrands[7] == data.hf[i][2] or data.hfbrands[8] == data.hf[i][2] or data.hfbrands[9] == data.hf[i][2] or data.hfbrands[10] == data.hf[i][2] or data.hfbrands[11] == data.hf[i][2] or data.hfbrands[12] == data.hf[i][2] or data.hfbrands[13] == data.hf[i][2] or data.hfbrands[14] == data.hf[i][2] or data.hfbrands[15] == data.hf[i][2] or data.hfbrands[16] == data.hf[i][2] or data.hfbrands[17] == data.hf[i][2] or data.hfbrands[18] == data.hf[i][2]:
				done.append(a[i])
	notdone = unmatched(a, done, c)
	return [done, notdone]

unique = uniquebrands(newdata, hfbrands, 2)
print len(unique[0]) + len(unique[1])

def idmatcher(a, b, c): #UPC is 5 (c)
	data_a = a
	data_b = b
	done = []
	doneb = []
	ycount = 0
	ncount = 0
	for index in range(len(a)):
		if a[index][c] == "":
			ncount = ncount + 1
		else:
			for index2 in range(len(b)):
				if a[index][c] == b[index2][c]:
					data_a[index][1] = data_b[index2][1]
					ycount =  ycount + 1
					done.append(data_a[index])
					doneb.append(data_b[index2])
	data_a = unmatched(a, done, 0)
	data_b = unmatched(b, doneb, 1)
	return [done, data_a, data_b, ycount, ncount]

matched = idmatcher(bwgs, newdata, 5)
print len(matched[1]), len(matched[2]), len(matched[0]), matched[3], matched[4]
					
					
					
					