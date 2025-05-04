import imageio.v3 as iio 

filenames = ['images\\image1.png','images\\image2.png','images\\image3.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('wojakmeme.gif', images, duration = 500, loop = 0)
