import imageio.v3 as iio 

filenames = ['images\\img1.png','images\\img2.png']\
img = []

for filename in filenames:
    img.append(iio.imread(filename))
