import matplotlib.pyplot
import numpy
x = numpy.linspace(-1, 1, 100)
y = numpy.tan(x)
matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.xlabel("x")
matplotlib.pyplot.ylabel("tan(x)")
matplotlib.pyplot.title("Tangente")
matplotlib.pyplot.show()