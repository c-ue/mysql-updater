import tkinter as tk

import managercore as mc


class ui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.ui()


    def ui(self):
        self.Usertext = tk.Label(self)
        self.Usertext['text'] = "User"
        self.Usertext.grid(row=0, column=0)

        self.UserInput = tk.Entry(self)
        self.UserInput['width'] = 10
        self.UserInput.grid(row=0, column=1)

        self.Passwdtext = tk.Label(self)
        self.Passwdtext['text'] = "Password"
        self.Passwdtext.grid(row=0, column=2)

        self.PasswdInput = tk.Entry(self)
        self.PasswdInput['width'] = 10
        self.PasswdInput.grid(row=0, column=3)

        self.Test = tk.Button(self)
        self.Test['text'] = "test"
        self.Test.grid(row=0, column=4)
        self.Test['command'] = self.test

        self.Start = tk.Button(self)
        self.Start['text'] = "start"
        self.Start.grid(row=0, column=5)
        self.Start['command'] = self.start

        self.UnitTime = tk.Label(self)
        self.UnitTime['text'] = "Per Cycle time(min)"
        self.UnitTime.grid(row=1, column=0)

        self.UnitTimeInput = tk.Entry(self)
        self.UnitTimeInput['width'] = 10
        self.UnitTimeInput.grid(row=1, column=1)

        self.LoopTimes = tk.Label(self)
        self.LoopTimes['text'] = "Loop Times"
        self.LoopTimes.grid(row=1, column=2)

        self.LoopInput = tk.Entry(self)
        self.LoopInput['width'] = 10
        self.LoopInput.grid(row=1, column=3)

        self.StartTime = tk.Label(self)
        self.StartTime['text'] = "Start Time(mm:ss)"
        self.StartTime.grid(row=1, column=4)

        self.StartInput = tk.Entry(self)
        self.StartInput['width'] = 10
        self.StartInput.grid(row=1, column=5)

        self.Msg = tk.Label(self)
        self.Msg['text'] = ""
        self.Msg.grid(row=2, column=0, columnspan=6)

    def start(self):
        if not self.test():
            return False
        connectobj = mc.core(Loops=self.LoopInput.get(), PerCycleTime=self.UnitTimeInput.get(),
                             StartTime=self.StartInput.get(), User=self.UserInput.get(), Passwd=self.PasswdInput.get())
        if (connectobj.start()):
            return True
        return False

    def test(self):
        connectobj = mc.core(Loops=self.LoopInput.get(), PerCycleTime=self.UnitTimeInput.get(),
                             StartTime=self.StartInput.get(), User=self.UserInput.get(), Passwd=self.PasswdInput.get())
        if connectobj.error is not None:
            self.Msg['text'] = connectobj.error
            return False
        if connectobj.test():
            self.Msg['text'] = 'Connect successed!'
            return True
        return False
