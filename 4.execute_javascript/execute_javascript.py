from cefpython3 import cefpython as cef
import sys

sys.excepthook = cef.ExceptHook

cef.Initialize()
browser = cef.CreateBrowserSync(url='file:///execute_javascript.html',
                                window_title='cefpython examples for beginners - ExecuteJavascript')

browser.ExecuteJavascript('alert("Execute a string of JavaScript code")')

cef.MessageLoop()
cef.Shutdown()
