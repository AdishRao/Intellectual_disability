import plotly as py
import plotly.graph_objs as go
x = [40,39] #Scores of Ravens
y = [8,18] #Scores of BST
z = [18,48] #Scores of DST
a = [9,37] #Scores of Drawing test

data = [go.Scatterpolar(
  r = [x[0], y[0], z[0], a[0], x[0]],
    theta = ['Ravens','BST','DST','Drawing test','Ravens'],
  fill = 'toself',
  name = 'Test 1'
),
go.Scatterpolar(
    r = [x[1], y[1], z[1], a[1], x[1]],
    theta = ['Ravens','BST','DST','Drawing test','Ravens'],
    fill = 'toself',
    name = 'Test 2'
)
]

layout = go.Layout(
  polar = dict(
    radialaxis = dict(
      visible = True,
      range = [0, 50]
    )
  ),
  showlegend = True
)

fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename = "temp-plot")