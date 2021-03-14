import osmnx as ox

point = (53.3498, -6.2603)
G = ox.graph_from_point(point, dist=10000, retain_all=True,
                        simplify=True, network_type='drive')

u = []
v = []
key = []
data = []
for uu, vv, kkey, ddata in G.edges(keys=True, data=True):
    u.append(uu)
    v.append(vv)
    key.append(kkey)
    data.append(ddata)

colours = []
widths = []

for item in data:
    if "length" in item.keys():
        if item["length"] <= 100:
            linewidth = 0.10
            colour = "#53565A"

        elif item["length"] > 100 and item["length"] <= 200:
            linewidth = 0.15
            colour = "#0E73B9"

        elif item["length"] > 200 and item["length"] <= 400:
            linewidth = 0.25
            colour = "#9BC3CA"

        elif item["length"] > 400 and item["length"] <= 800:
            colour = "#A7D1A7"
            linewidth = 0.35
        else:
            colour = "#245391"
            linewidth = 0.45
    else:
        colour = "#a6a6a6"
        linewidth = 0.10

    colours.append(colour)
    widths.append(linewidth)

latitude = 53.3498
longitude = -6.2603

background = "#23297a"

fig, ax = ox.plot_graph(G, node_size=0, figsize=(27, 40),
                        dpi=300, bgcolor=background,
                        save=False, edge_color=colours,
                        edge_linewidth=widths, edge_alpha=1)


fig.tight_layout(pad=0)
fig.savefig("dublinstreets.png", dpi=300, bbox_inches='tight',
            format="png", facecolor=fig.get_facecolor(), transparent=False)
