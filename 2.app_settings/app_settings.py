from cefpython3 import cefpython as cef
import sys

sys.excepthook = cef.ExceptHook

settings = {
    'background_color': int('0xFFBBBBBB', 16),
    'context_menu': {'enabled': False},
    'product_version': 'cefpython exampls/1.0',
}

cef.Initialize(settings=settings)
cef.CreateBrowserSync(url='file:///app_settings.html',
                      window_title='cefpython examples for beginners - Application Settings')

cef.MessageLoop()
cef.Shutdown()
