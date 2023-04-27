from cefpython3 import cefpython as cef
import sys

sys.excepthook = cef.ExceptHook

cef.Initialize()
cef.CreateBrowserSync(url='file:///hello_world.html',
                      window_title='cefpython examples for beginners - Hello World!')

cef.MessageLoop()
cef.Shutdown()
