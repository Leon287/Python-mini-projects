import imageio.v3 as iio 

filenames = ['images\\image1.jpg','images\\image2.jpg','images\\image3.jpg']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('wojak-meme.gif', images, duration = 500, loop = 0)
