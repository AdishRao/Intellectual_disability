from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import plotly.io as pio

import os
import numpy as np
init_notebook_mode(connected=True)

trace1 = go.Bar(
    x=['Ravens','BST','DST','Drawing test'],
    y=[23, 110, 23, 10],
    name='Test on 23/08/97'
)
trace2 = go.Bar(
    x=['Ravens','BST','DST','Drawing test'],
    y=[20, 97, 21, 20],
    name='Test on 27/04/98',
    marker=dict(
        color=['rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)',
               'rgba(222,45,38,0.8)', 'rgba(0,255,0,1.0)'])
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
pio.write_image(fig, 'fig1.png')