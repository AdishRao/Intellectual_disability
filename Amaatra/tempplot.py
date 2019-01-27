from plotly import tools
import plotly as py
import plotly.graph_objs as go
import plotly.io as pio

trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
trace2 = go.Scatter(x=[20, 30, 40], y=[50, 60, 70])
trace3 = go.Scatter(x=[300, 400, 500], y=[600, 700, 800])
trace4 = go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000])

data = [trace1,trace2,trace3,trace4]


fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Plot 1', 'Plot 2','Plot 3', 'Plot 4'))

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 2, 2)

fig['layout'].update(height=600, width=600, title='Multiple Subplots' +' with Titles')
pio.write_image(fig, 'Report.png')

#py.offline.plot(fig, filename='make-subplots-multiple-with-titles.html')