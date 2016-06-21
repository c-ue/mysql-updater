import time

import mysqlcore as mc


class core:
    def __init__(self, Loops=None, PerCycleTime=None, StartTime=None, User=None, Passwd=None):
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
        while (int(time.strftime("%H")) * 60 + int(time.strftime("%M")) < self.StartMin + self.StartHour * 60):
            time.sleep(5)
        while(self.loops != 0):
            self.loops-=1
            if not self.process():
                return False
            time.sleep(self.pertime*60)
    def process(self):
        QidList=self.mysql.GetQidList()
        if QidList==False:
            self.error = self.mysql.error
            return False
        for i in QidList:
            TeamList = self.mysql.GetTeamByQid(i['uq'], i['lq'])
            QidScore = self.mysql.GetScoreByQid(i['uq'], i['lq'])
            if TeamList == False or QidList==False:
                return False
            elif TeamList == None:
                continue
            PartOfScore = QidScore[0]['score'] / len(TeamList)
            for j in TeamList:
                if not self.mysql.AddRoundScore(j['tid'], PartOfScore):
                    return False
                if not self.mysql.CalcTotalScore(j['tid']):
                    return False
        return True

    def test(self):
        return self.mysql.Test()
