import plotly
import plotly.graph_objs as graph_objs


class Graph:
    def __init__(self):
        self.title = "Hello World"
        self.data = [[1, 4], [2, 6], [3, 2], [4, 1]]
        self.auto_open = False
        self.filename = "../tmp/graphs/temp-plot.html"

    def generate(self):
        data = [graph_objs.Scatter(x=self.x_data_points(), y=self.y_data_points())]
        layout = graph_objs.Layout(title=self.title)

        plotly.offline.plot(
            {"data": data, "layout": layout},
            auto_open=self.auto_open,
            filename=self.filename
        )

    def x_data_points(self):
        return list(map(lambda x: x[0], self.data))

    def y_data_points(self):
        return list(map(lambda y: y[1], self.data))


Graph().generate()
