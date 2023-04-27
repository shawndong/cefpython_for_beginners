from cefpython3 import cefpython as cef
import sys


def on_after_created(browser, **_):
    print('OnAfterCreated')


sys.excepthook = cef.ExceptHook

cef.Initialize()
cef.SetGlobalClientCallback('OnAfterCreated', on_after_created)
cef.CreateBrowserSync(url='file:///on_after_created.html',
                      window_title='cefpython examples for beginners - OnAfterCreated')

cef.MessageLoop()
cef.Shutdown()
