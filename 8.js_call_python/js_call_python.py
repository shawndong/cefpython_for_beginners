from cefpython3 import cefpython as cef
import sys


class DisplayHandler(object):
    def OnConsoleMessage(self, browser, message, **_):
        print('OnConsoleMessage', message)


def ask_python_sum(a, b, js_callback):
    # this function will bind to JavaScipt for calling by JavaScript
    sum_ = a + b
    js_callback.Call(a, b, sum_)


sys.excepthook = cef.ExceptHook

cef.Initialize()
browser = cef.CreateBrowserSync(url='file:///js_call_python.html',
                                window_title='cefpython examples for beginners - JS call Python')

browser.SetClientHandler(DisplayHandler())

bindings = cef.JavascriptBindings(bindToFrames=False, bindToPopups=False)
bindings.SetFunction("ask_python_sum", ask_python_sum)
browser.SetJavascriptBindings(bindings)

cef.MessageLoop()
cef.Shutdown()
