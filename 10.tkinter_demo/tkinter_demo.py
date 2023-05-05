from tkinter import *
from cefpython3 import cefpython as cef
import sys
import ctypes


class Main(object):
    def __init__(self):
        sys.excepthook = cef.ExceptHook

        self.root = Tk()
        self.root.title('cefpython examples for beginners - tkinter demo')
        self.root.geometry('1200x600')
        self.root.bind("<Configure>", self.on_configure)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.frm_browser = BrowserFrame(self.root)
        self.frm_browser.pack(fill=BOTH, expand=YES)

        cef.Initialize()
        self.root.mainloop()
        cef.Shutdown()

    def on_configure(self, event):
        if self.frm_browser and self.frm_browser.browser:
            ctypes.windll.user32.SetWindowPos(self.frm_browser.browser.GetWindowHandle(), 0,
                                              0, 0, event.width, event.height, 0x0002)
            self.frm_browser.browser.NotifyMoveOrResizeStarted()

    def on_close(self):
        if self.frm_browser:
            if self.frm_browser.browser:
                self.frm_browser.browser.CloseBrowser(True)
                self.frm_browser.browser = None
            else:
                self.frm_browser.destroy()
            self.frm_browser = None
        else:
            self.root.destroy()


class BrowserFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.browser = None

        self.bind("<Configure>", self.on_configure)

    def on_configure(self, event=None):
        if not self.browser:
            self.embed_browser()

    def embed_browser(self):
        rect = [0, 0, self.winfo_width(), self.winfo_height()]
        window_info = cef.WindowInfo()
        window_info.SetAsChild(self.get_window_handle(), rect)
        self.browser = cef.CreateBrowserSync(window_info, url="file:///tkinter_demo.html")
        assert self.browser
        self.message_loop_work()

    def message_loop_work(self):
        cef.MessageLoopWork()
        self.after(10, self.message_loop_work)

    def get_window_handle(self):
        if self.winfo_id() > 0:
            return self.winfo_id()
        else:
            raise Exception("Couldn't obtain window handle")


if __name__ == "__main__":
    main = Main()
