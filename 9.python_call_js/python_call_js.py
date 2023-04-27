from cefpython3 import cefpython as cef
import sys


class DisplayHandler(object):
    def OnConsoleMessage(self, browser, message, **_):
        print('OnConsoleMessage', message)


class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        print('OnLoadingStateChange', is_loading)
        if not is_loading:
            # Loading is complete. DOM is ready.
            browser.ExecuteFunction('ask_javascript_sum', 2, 1)


def javascript_answer_sum(a, b, sum_):
    print(f'{a} + {b} = {sum_}')


sys.excepthook = cef.ExceptHook

cef.Initialize()
browser = cef.CreateBrowserSync(url='file:///python_call_js.html',
                                window_title='cefpython examples for beginners - Python call JS')

browser.SetClientHandler(LoadHandler())
browser.SetClientHandler(DisplayHandler())

bindings = cef.JavascriptBindings(bindToFrames=False, bindToPopups=False)
bindings.SetFunction("javascript_answer_sum", javascript_answer_sum)
browser.SetJavascriptBindings(bindings)

cef.MessageLoop()
cef.Shutdown()
