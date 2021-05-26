import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.io.img_tiles import GoogleTiles
fig=plt.figure(figsize=(10,10))
google_tiles=GoogleTiles()
ax= plt.axes(projection=google_tiles.crs)
ax.set_extent((2.2,2.5,48.8,48.93))
zoom=12
ax.add_image(google_tiles,zoom)
ax.scatter("longitude","latitude",data=listing,s=1,transform=ccrs.PlateCarree()()),alpha=.1
