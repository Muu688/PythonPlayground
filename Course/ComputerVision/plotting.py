# from CaptureVideo_MotionDetection import df
from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure, show, output_file
import pandas
from bokeh.models import HoverTool, ColumnarDataSource



df=pandas.read_csv("Times.csv", parse_dates=["Start","End"])
cds=ColumnDataSource(df)


# print(df)

p = figure(x_axis_type='datetime', height=100, width=500, sizing_mode="scale_width", title="Motion Graph")

p.yaxis.minor_tick_line_color=None
# p.ygrid[0].ticket.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start", "@Start"),("End", "@End")])
p.add_tools(hover)

q = p.quad(left=["Start"], right=["End"], bottom=0, top=1, color="green", source=cds)

output_file=("Graph.html")
show(p)
