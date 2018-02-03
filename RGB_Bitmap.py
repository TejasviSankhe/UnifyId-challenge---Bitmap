import requests
import random
from PIL import Image


def randomOrgCall(num,min_n=0,max_n=255):
	url="https://www.random.org/integers/?num={num}&min={min_n}&max={max_n}&col=1&base=10&format=plain&rnd=new".format(num=str(num),min_n=str(min_n),max_n=str(max_n))
	nums = requests.get(url)
	return list(map(int, nums.text.strip().split("\n"))) 

#test=randomOrgCall(2)
#print(test)
def get_rgb():
	total_px=128*128*3 								#for RGB tuples
	px=[]
	for _ in range (5): 							#total_px/max number allowed(10000)		
		n= 10000 if total_px>10000 else total_px	#max number allowed by random.org
		random_nums= randomOrgCall(n)
		#random_nums=random.choices(range(0,255),k=n)  # call for testing
		total_px-=10000
		px = px+random_nums
	#print(len(px))

	ret=[]
	for i in range(0,len(px),3):
		temp_tuple=(px[i],px[i+1],px[i+2])
		ret.append(temp_tuple)

	return ret


image_size = (128, 128)
# create new image
im = Image.new(mode="RGB", size=image_size)
#get RGB tuples
im.putdata(get_rgb())
#show and save image
im.show()
im.save("random_bitmap.jpg")