from cefpython3 import cefpython as cef
import sys

sys.excepthook = cef.ExceptHook

cef.Initialize()
browser = cef.CreateBrowserSync(url='file:///set_property.html',
                                window_title='cefpython examples for beginners - SetProperty')

python_string = 'This is a string defined in Python'
bindings = cef.JavascriptBindings(bindToFrames=False, bindToPopups=False)
bindings.SetProperty('python_string', python_string)
browser.SetJavascriptBindings(bindings)

cef.MessageLoop()
cef.Shutdown()
