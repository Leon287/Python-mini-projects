import imageio.v3 as iio 

filenames = ['images\\hippocorn1.png','images\\hippocorn2.png','images\\hippocorn3.png','images\\hippocorn4.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('hippocorn.gif', images, duration = 500, loop = 0)
