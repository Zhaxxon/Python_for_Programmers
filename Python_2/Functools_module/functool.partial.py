from functools import partial
def add(x, y):
    return x + y

p_add = partial(add, 2)
print(p_add(4))

import wx

class MainFrame(wx.Frame):
    """
    This app shows a group of buttons
    """

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super(MainFrame, self).__init__(parent=None, title='Partial')
        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        btn_labels = ['one', 'two', 'three']
        for label in btn_labels:
            btn = wx.Button(panel, label=label)
            btn.Bind(wx.EVT_BUTTON, partial(self.onButton, label=label))
            sizer.Add(btn, 0, wx.ALL, 5)

        panel.SetSizer(sizer)
        self.Show()

    def onButton(self, event, label):
        """
        Event handler called when a button is pressed
        """
        print('You pressed ' + str(label))

def add(x, y):
    """"""
    return x + y


def multiply(x, y):
    """"""
    return x * y


def run(func):
    """"""
    print(func())


def main():
    """"""
    a1 = partial(add, 1, 2)
    m1 = partial(multiply, 5, 8)
    run(a1)
    run(m1)

if __name__ == "__main__":
    main()