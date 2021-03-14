import networkx as nx
import osmnx as ox


point = (53.3498, -6.2603)
G1 = ox.graph_from_point(point, dist=15000, dist_type='bbox',
                         network_type='all', simplify=True,
                         retain_all=True, truncate_by_edge=False,
                         clean_periphery=False,
                         custom_filter='["natural"~"water"]')
G2 = ox.graph_from_point(point, dist=15000, dist_type='bbox',
                         network_type='all', simplify=True,
                         retain_all=True, truncate_by_edge=False,
                         clean_periphery=False,
                         custom_filter='["waterway"~"river"]')
Gwater = nx.compose(G1, G2)


u = []
v = []
key = []
data = []
for uu, vv, kkey, ddata in Gwater.edges(keys=True, data=True):
    u.append(uu)
    v.append(vv)
    key.append(kkey)
    data.append(ddata)


colours = []
widths = []

for item in data:
    if "name" in item.keys():
        if item["length"] > 400:
            colour = "#23297a"
            linewidth = 2
        else:
            colour = "#23297a"
            linewidth = 0.5
    else:
        colour = "#23297a"
        linewidth = 0.5
    colours.append(colour)
    widths.append(linewidth)


fig, ax = ox.plot_graph(Gwater, node_size=0, figsize=(27, 40),
                        dpi=300, save=False, edge_color=colours,
                        edge_linewidth=widths, edge_alpha=1)

fig.tight_layout(pad=0)
fig.savefig("dublinwatercourses.png", dpi=300, bbox_inches='tight',
            format="png", facecolor=fig.get_facecolor(),
            transparent=True)
