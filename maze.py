#maze coding
import getch

miromap =  [
    [2,0,0,0,0,1],
    [0,1,0,1,1,1],
    [0,1,1,0,0,1],
    [0,0,0,1,0,1],
    [0,1,0,1,0,1],
    [1,1,0,0,0,3]
]

st = miromap[0][0]
goal = miromap[5][5]
x=0
y=0
me = '●'

def mapview(miromap):
	for line in miromap:
		for c in line:
			print(str(c).replace("0", "□").replace("1", "■"), end="")
		print('')


print ("------------------------GAME START----------------------")
mapview(miromap)
while True:
	
	if me==miromap[5][5]:
		break
	ch = getch.getch()
	#w
	if (ord(ch)==119) and (miromap[x-1][y] != 1):
		print('w')
		x-=1
		miromap[x][y] = me
		miromap[x+1][y] = 0
	#a
	elif ord(ch)==97 and miromap[x][y-1] != 1:
		print('a')
		y-=1
		miromap[x][y] = me
		miromap[x][y+1] = 0

	#s
	elif ord(ch)==115 and miromap[x+1][y] != 1:
		print('s')
		x+=1
		miromap[x][y] = me
		miromap[x-1][y] = 0
	#d
	elif ord(ch)==100 and miromap[x][y+1] != 1:
		print('d')
		y+=1			
		miromap[x][y] = me
		miromap[x][y-1] = 0

	else:
		print("w/a/s/d choice!!!! OR 벽")

	mapview(miromap)