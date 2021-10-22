import numpy as np
from PIL import Image

# Create 3dnumpy array of zeros, then replace zeros (black) with yellow
data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print (data)

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')