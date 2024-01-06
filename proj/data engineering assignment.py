

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle




data = pd.read_csv(r'GrowLocations.csv')


# # bounding box definition 

# In[40]:


min_long = 50.681
max_long = 57.985
min_lat = -10.592
max_lat = 1.6848




filtered_grow_df = grow_df[
    (grow_df['Latitude'] >= latitude_min) & (grow_df['Latitude'] <= latitude_max) &
    (grow_df['Longitude'] >= longitude_min) & (grow_df['Longitude'] <= longitude_max)
]







# bringing every thing together 

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(map_pic, extent=[min_long, max_long, min_lat, max_lat])

ax.scatter(good_data['Longitude'], good_data['Latitude'], zorder=1, alpha=0.6, 
           c='green', s=50, marker='p', edgecolors='black', linewidth=0.5)

ax.set_title('Sensor Locations on UK Map')
ax.set_xlim(min_long, max_long)
ax.set_ylim(min_lat, max_lat)

box = Rectangle((min_long, min_lat),
                max_long - min_long,
                max_lat - min_lat,
                fill=False, color="red", linewidth=2)

ax.add_patch(box)

plt.show()






# # github link : https://github.com/HarryRichard08/uk_map-plotting-using-python-and-matlpotlib/tree/main/proj




