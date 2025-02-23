import geopandas as gpd
import matplotlib.pyplot as plt

# 讀取 GIS 檔案
gdf = gpd.read_file("industrial area.shp")

# 繪製地圖
gdf.plot()
plt.show()
