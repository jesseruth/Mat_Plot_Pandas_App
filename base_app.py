# -*- coding: utf-8 -*-
"""
Created on Fri May  9 17:13:07 2014

@author: edoc
"""

import logging

logger = logging.getLogger('basic logger')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
#fh = logging.FileHandler('spam.log')
#fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
# Level  	Numeric value
# CRITICAL	50 # ERROR	40 # WARNING 30 # INFO 20 # DEBUG	 10 # NOTSET 0
ch.setLevel(logging.NOTSET)
# create formatter and add it to the handlers
formatter = \
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
#fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
#logger.addHandler(fh)

# 'application' code
logger.debug('Start of imports')

#wx python module
import wx

#Matplotlib figure object
from matplotlib.figure import Figure
#numpy function for image creation
import numpy as np

# import WxAgg FigureCanvas Object, that binds fiure to backend
# in this WxPanel
from matplotlib.backends.backend_wxagg import \
    FigureCanvasWxAgg as FigureCanvas

from matplotlib.backends.backend_wx import NavigationToolbar2Wx


class MplCanvasFrame(wx.Frame):
    """Class to represent a Matplotlib Figure as a wx.Frame"""
    def __init__(self):
        # initialize the super class, the wx.Frame
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          title='Matplotlib in Wx 2',
                          size=(1000, 1000))

        self.SetBackgroundColour(wx.NamedColour("BLACK"))
        # usual matplotlib functions
        # Create matplotlib figure
        self.figure = Figure(figsize=(9, 8), dpi=80, tight_layout=True)
        # Add four suubplots to the figure
        self.axes1 = self.figure.add_subplot(221, axisbg='r')
        self.axes2 = self.figure.add_subplot(222)
        self.axes3 = self.figure.add_subplot(223)
        self.axes4 = self.figure.add_subplot(224)
        # Use Numpy to create a range of numbers
        x = np.arange(0, 6, .01)
        y = np.sin(x**2)*np.exp(-x)
        # Experimenting with plotting the stuff onto different
        # Axes.
        self.axes1.plot(x, y)
        self.axes1.annotate('arrowstyle', xy=(4, .1),  xycoords='data',
                            xytext=(-50, 30), textcoords='offset points',
                            arrowprops=dict(arrowstyle="->")
                            )
        self.axes2.plot(x * 2, y)
        self.axes2.annotate('arc3', xy=(4, .1),  xycoords='data',
                            xytext=(-30, -30), textcoords='offset points',
                            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3,rad=.2")
                            )
        self.axes3.plot(x, y)
        self.axes3.annotate('arc', xy=(4, .1),  xycoords='data',
                            xytext=(-40, 30), textcoords='offset points',
                            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc,angleA=0,armA=30,rad=10"),
                            )
        self.axes4.plot(x, y)
        self.axes4.annotate('arc', xy=(4, .1),  xycoords='data',
                            xytext=(-40, -30), textcoords='offset points',
                            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc,angleA=0,armA=20,angleB=-90,armB=15,rad=7"),
                            )
        #initialize the figure canvas
        self.canvas = FigureCanvas(self, wx.ID_ANY, self.figure)

        # Create a box sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        # add the sizer to the canvas
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)

        # Instantiate the  navigation toolbar
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        # needed for windows
        mass_txt = wx.StaticText(self.toolbar, label='m/z',
                                 pos=(230, 7), size=(25, 17))
        mass_txt.SetBackgroundColour("light gray")
        self.mass = wx.TextCtrl(self.toolbar, pos=(260, 4),
                                size=(50, 22),
                                style=wx.TE_READONLY)
        self.toolbar.SetToolBitmapSize(wx.Size(50, 50))
        self.toolbar.Realize()
        self.toolbar.Update()


        # add it to the sizer
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        # explicitly show the toolbar
        self.toolbar.Show()

        # sets the window to have the given layout sizer
        self.SetSizer(self.sizer)
        # adapt sub widget sizes to fit the window size
        # following sizer specification
        self.SetMinSize((1000, 825))
        self.Fit()


class MplApp(wx.App):
    """Define customized app for mpl canvas"""
    def OnInit(self):
        # instantiate our custom wx frame
        frame = MplCanvasFrame()
        self.SetTopWindow(frame)
        # show it
        frame.Show(True)
        # return true to continue processing
        return True

if __name__ == '__main__':
    mplapp = MplApp(False)
    logger.debug('End of program')
    # start wxWidgets MainLoope
    mplapp.MainLoop()







