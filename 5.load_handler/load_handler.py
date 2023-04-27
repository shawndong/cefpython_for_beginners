from cefpython3 import cefpython as cef
import sys


class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        print('OnLoadingStateChange', is_loading)


sys.excepthook = cef.ExceptHook

cef.Initialize()
browser = cef.CreateBrowserSync(url='file:///load_handler1.html',
                                window_title='cefpython examples for beginners - LoadHandler')

browser.SetClientHandler(LoadHandler())

cef.MessageLoop()
cef.Shutdown()
