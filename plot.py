import plotly as py
import plotly.graph_objs as go
x = [40,20] #Scores of Ravens
y = [8,18] #Scores of BST
z = [18,48] #Scores of DST
a = [9,37] #Scores of Drawing test

data = [go.Scatterpolar(
  r = [20, 97, 21, 20],
  theta = ['Ravens','BST','DST','Drawing test'],
  fill = 'toself',
  name = 'Test on 23/08/97'
),
go.Scatterpolar(
    r = [23, 110, 23, 10],
    theta = ['Ravens','BST','DST','Drawing test'],
    fill = 'toself',
    name = 'Test on 27/04/98'
)
]

layout = go.Layout(
  polar = dict(
    radialaxis = dict(
      visible = True,
      range = [0,120]
    )
  ),
  showlegend = True
)

fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename = "temp-plot.html")