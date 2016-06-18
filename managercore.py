import mysqlcore as mc
class core:
    def __init__(self, Loops=None, PerCycleTime=None, StartTime=None, User=None, Passwd=None):
        self.team = range(1, 8)
        if (Loops.isdigist() and PerCycleTime.isdigist() and StartTime and len(StartTime.split(':')) == 2 and
                StartTime.split(':')[0].isdigist() and StartTime.split(':')[1].isdigist() and
                        0 <= int(StartTime.split(':')[0]) < 24 and 0 <= int(StartTime.split(':')[1]) < 59 and
                User and Passwd):
            self.loops = int(Loops)
            self.pertime = int(PerCycleTime)
            self.StartHour = int(StartTime.split(':')[0])
            self.StartMin = int(StartTime.split(':')[1])
            self.mysql = mc.core(user=User, passwd=Passwd)
            if self.mysql.error != "":
                return False
            self.qlist = self.mysql.GetQidList()
            if not self.qlist:
                return False
            return True
        return False

    def start(self):

        pass

    def test(self):
        return self.mysql.Test()
