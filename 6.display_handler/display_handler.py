from cefpython3 import cefpython as cef
import sys


class DisplayHandler(object):
    def OnConsoleMessage(self, browser, message, **_):
        print('OnConsoleMessage', message)


sys.excepthook = cef.ExceptHook

cef.Initialize()
browser = cef.CreateBrowserSync(url='file:///display_handler.html',
                                window_title='cefpython examples for beginners - DisplayHandler')

browser.SetClientHandler(DisplayHandler())
browser.ExecuteJavascript('undefined_function()')

cef.MessageLoop()
cef.Shutdown()
