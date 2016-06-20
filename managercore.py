import mysqlcore as mc
import time
class core:
    def __init__(self, Loops=None, PerCycleTime=None, StartTime=None, User=None, Passwd=None):
        self.team = range(1, 8)
        if (Loops.isdigit() and PerCycleTime.isdigit() and StartTime and len(StartTime.split(':')) == 2 and
                StartTime.split(':')[0].isdigit() and StartTime.split(':')[1].isdigit() and
                        0 <= int(StartTime.split(':')[0]) < 24 and 0 <= int(StartTime.split(':')[1]) < 59 and
                User and Passwd):
            self.loops = int(Loops)
            self.pertime = int(PerCycleTime)
            self.StartHour = int(StartTime.split(':')[0])
            self.StartMin = int(StartTime.split(':')[1])
            self.mysql = mc.core(user=User, passwd=Passwd)
            self.error=None
            if self.mysql.error is not None:
                self.error=self.mysql.error
                return
            return
        self.error='Field Entry Error'
        return

    def start(self):
        while(time.strftime('%H:%M') != str(self.StartHour) + ':' + str(self.StartMin)):
            time.sleep(5)
        while(self.loops != 0):
            self.loops-=1
            if not self.process():
                return False
            time.sleep(self.pertime*60)
    def process(self):
        QidList=self.mysql.GetQidList()
        if QidList==False:
            return False
        for i in QidList:
            TeamList=self.mysql.GetTeamByQid(i[0],i[1])
            QidScore=self.mysql.GetScoreByQid(i[0],i[1])
            if TeamList == False or QidList==False:
                return False
            PartOfScore=QidScore/len(TeamList)
            for j in TeamList:
                if not self.mysql.AddRoundScore(j, PartOfScore):
                    return False
                if not self.mysql.CalcTotalScore(j):
                    return False
        return True

    def test(self):
        return self.mysql.Test()
