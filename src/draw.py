import math 

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource
from bokeh.palettes import Spectral8

from graph import *

WIDTH = 640
HEIGHT = 480
#CIRCLE_SIZE = 30

graph_data = Graph()
graph_data.debug_create_test_data()
#graph_data.bfs(graph_data.vertexes[0])
# print('+++', graph_data.vertexes)

N = len(graph_data.vertexes)
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

'''
debug_pallete = Spectral8
debug_pallete.append('ff0000')
debug_pallete.append('0000ff')
'''
plot = figure(title='Graph Layout Demonstration', x_range=(0, HEIGHT), y_range=(0, WIDTH),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Circle(size=20, fill_color='color')

# this is drawing the edges from start to end # in-class solution 
'''
start_indexes = []
end_indexes = []

for start_indexes, vertex in enumerate(graph_data.vertexes):
    for e in vertex.edges:
        start_indexes.append(start_index)
        end_indexes.append(graph_data.vertexes.index(e.destination))
'''

graph.edge_renderer.data_source.data = dict(
    start=[1, 2], # a list of vertex indexes to start edges from 
    end=[3, 4]) # a list of vertex indexes to end edges at 
    
for vertex in graph_data.vertexes:
        if len(vertex.edges) > 0:
            for edge in vertex.edges:
                start = graph_data.vertexes.index(vertex)
                graph.edge_renderer.data_source.data['start'].append(start)

                end = graph_data.vertexes.index(edge.destination)
                graph.edge_renderer.data_source.data['end'].append(end)

### start of layout code

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

source = ColumnDataSource(data=dict(x_pos=x, y_pos=y, names=['t1', 't2', 't3', 't4', 't5', 't6']))

labels = LabelSet(x='x_pos', y='y_pos', text='names', level='glyph', x_offset=-10, y_offset=-10, source=source, render_mode='canvas', text_align='center', text_baseline='middle')

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

plot.add_layout(labels)

output_file('graph.html')
show(plot)

