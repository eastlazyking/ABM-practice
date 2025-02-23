import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# ======= 讀取地圖 =======
# 讀取土地坵塊的 shp 檔案 → gdf
gdf = gpd.read_file("industrial area_joined.shp")

# ======= 讀取代理人 =======
# 讀取工廠位置的 CSV 檔案 → gdf_agents 
df_agents = pd.read_csv("10 for test.csv", encoding="big5")

# 將 'x' 和 'y' 轉換為 GeoPandas Point
df_agents['geometry'] = df_agents.apply(lambda row: Point(row['x'], row['y']), axis=1)

# 將 Pandas DataFrame 轉換為 GeoPandas GeoDataFrame
gdf_agents = gpd.GeoDataFrame(df_agents, geometry='geometry', crs="EPSG:4326")  # WGS84

# 檢查 GeoDataFrame
print(gdf_agents.head())

# ======= 製造畫面 =======
ax = gdf.plot() # 繪製地圖
gdf_agents.plot(ax = ax, color="orange", markersize=10, label="Factory Agent") # 在地圖上繪製代理人
# plt.legend() # 繪製圖例
plt.show()


