import math 

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, LabelSet, ColumnDataSource
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
print('+++', graph_data.vertexes)

N = len(graph_data.vertexes)
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)


debug_pallete = Spectral8
debug_pallete.append('ff0000')
debug_pallete.append('0000ff')

plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0, 500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=10, width=10, fill_color='color')

graph.edge_renderer.data_source.data = dict(
    start=[],
    end=[])
    
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

labels = LabelSet(x='x_pos', y='y_pos', text='names', level='glyph', x_offset=-10, y_offset=-10, source=source, render_mode='canvas')

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

plot.add_layout(labels)

output_file('graph.html')
show(plot)

