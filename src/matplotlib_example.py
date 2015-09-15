import matplotlib.pyplot as plt


class PlotData(object):
    def __init__(self):
        self.xs = []
        self.ys = []
        self.urls = []

    def add(self, x, y, url):
        self.xs.append(x)
        self.ys.append(y)
        self.urls.append(url)


if __name__ == '__main__':
    f = plt.figure()
    pd = PlotData()
    pd.add(1, 4, '19')
    pd.add(2, 5, '20')
    pd.add(3, 6, '21')
    s = plt.scatter(pd.xs, pd.ys)
    s.set_urls(pd.urls)
    f.canvas.print_figure('matplotlib_example.svg')
