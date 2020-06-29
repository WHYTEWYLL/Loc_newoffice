import folium
def usamap(m,data_usa,dict_colors):
    for i, row in data_usa.iterrows():
        folium.Circle(
            location=row[["latitude","longitude"]],
            tooltip=row["state_code"],
            radius=100,
            popup=row["name"],
            color=dict_colors[row["category_code"]]
        ).add_to(m)
