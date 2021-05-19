import matplotlib.pyplot as plt
import numpy as np
array_image=np.random.randint(0,255,(1000,1000,3)).astype("uint8")
plt.imshow(array_image)
plt.savefig("mon_image.jpg")
