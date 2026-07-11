        # Remaining topic of numpy
import numpy as np;
import matplotlib.pyplot as plt 



# plotting 3D graphs
# meshgrids
a = np.linspace(-10,9,20)
b = np.linspace(-10,9,20)
xx,yy=np.meshgrid(a,b)
print(xx)
print("\n")
print(yy)
plt.scatter(xx,yy)
# plt.show()

import plotly.express as px
import plotly.graph_objects as go

def func(x,y):
    return x**2 + y**2
zz = func(xx,yy)
fig =px.scatter_3d()
fig.add_trace(go.Surface(x=xx,y=yy,z=zz))
# fig.show()

# working with random
# randint
# seed
# shuffle
# choice
print(np.random.random((2,3))) # it creates a numpy array of 2x3 matrix that conatins random value
print("\n")
print(np.random.random((2,3,2))) #  it creates 3-d numpy array
 # for integer
print(np.random.randint(1,100,12).reshape(3,4))


print("\n Seed -> using seed ")
np.random.seed(0) # if seed mai 0 dalenga toa random integer constant hoa jeyga means jbb dubara call krenga toa woa value change nhi hoga.
print(np.random.randint(1,100,12).reshape(3,4))
# constant for all random after applying seed =0

print("\n Shuffle array ->  it will permanent change the order")
a = np.array([12,41,33,67,89,100])
print(a)
np.random.shuffle(a)
print(a)

print("\n choice random value from array")
# Here 3 represents how many ele you have to pick
print(np.random.choice(a,3,replace=False)) # here replace don't allow to pick same value twice . If replace is true then it pick the element 
# and then wapas array mai daal deta hai jsha hum whi element phr sa pick kr leta hai.


print("\n working with images")
"""
    800x800 means there are 640000 pixels. Each pixel have value in range [0-255]

    800x800x3 ; Here 3 -> refers as rgb, Which means how much layer we have. Total_pixels = 800*800*

    If we work on these numpy arrays or manipulate them this field is called computer vision.
"""
import cv2
# to import cv2 to we have to do -> pip install opencv-python

img_np = cv2.imread(r"C:\Users\prana\OneDrive\Pictures\Screenshots\Screenshot 2026-07-11 111912.png")
print(img_np)
print("\nShape of image =",img_np.shape)
plt.imshow(img_np)
# plt.imshow(np.flip(img_np,axis=0)) # it rotates the image
print("\n clip -> fade or reduce brightness")
plt.imshow(np.clip(img_np,0,100)) 

print("\n negative")
plt.imshow(255-img_np)

print("\n trim -> cropping the image")
plt.imshow(img_np[100:500,50:900,:])
plt.show()

print("\n plot histogram")

krish_img = cv2.imread(r"C:\Users\prana\OneDrive\Pictures\ImageInfo.jpg")
plt.hist(krish_img.flatten(),bins=255)
plt.show()

print("\n Structured arrays")

k = np.array([1,'hello',True,1.5])
print(k) # ['1' 'hello' 'True' '1.5'] but the output is homogenous means every element is string.
# name,iq,cgpa,placed

dt = np.dtype(
    [ # to make hetrogenous array . we have to give instruction to column which data type you can store
        ('name','U20'),
        ('iq',np.int32),
        ('cgpa',np.float64),
        ('placed','U20')
    ]
)
stu = np.array(
    [
        ('nitish',100,6.66,'Yes'),
        ('ankit',120,8.9,'Yes'),
        ('rahul',80,7.3,'No')
    ],dtype=dt # here we told the data type of stu
)
print(stu)
print("\nIndividual row :- \n")
# Now we can print any individual row
print(stu[0])

print("\n Element in that row :-\n")
print(stu[1][0])