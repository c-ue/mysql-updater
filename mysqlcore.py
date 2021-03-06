import pymysql as pm
class core:
    def __init__(self, user=False, passwd=False):
        self.error = None
        if not (user and passwd):
            self.error = "Field is Empty"
            return
        try:
            self.c = pm.connect(host='localhost',
                                user=user,
                                password=passwd,
                                db='is',
                                charset='utf8mb4',
                                cursorclass=pm.cursors.DictCursor
                                )
        except:
            self.error = "Mysql account Error"


    def GetTeamByQid(self, uq, lq):
        with self.c.cursor() as cc:
            sql = "select teamid as tid from tqinfo where uq=%s and lq=%s;"
            row = cc.execute(sql, (uq, lq))
            if row == 0:
                self.error = "Team not exist"
                return None
            return cc.fetchall()

    def AddRoundScore(self, teamid, score):
        with self.c.cursor() as cc:
            sql = "select roundscore as score from teaminfo where teamid=%s;"
            row = cc.execute(sql, (teamid,))
            if row != 1:
                self.error = 'Data Schema error'
                return False
            result = cc.fetchall()
            sql = "UPDATE teaminfo SET roundscore=%s WHERE teamid=%s;"
            cc.execute(sql, (result[0]['score'] + score, teamid))
        self.c.commit()
        return True

    def GetScoreByQid(self, uq, lq):
        with self.c.cursor() as cc:
            sql = "SELECT phase1score as score FROM qinfo WHERE uq=%s AND lq=%s"
            row = cc.execute(sql, (uq, lq))
            if row == 0:
                self.error = "Question not exist"
                return False
            return cc.fetchall()

    def CalcTotalScore(self, teamid):
        with self.c.cursor() as cc:
            sql = "SELECT (SELECT phasescore as score FROM teaminfo WHERE teamid=%s)+(SELECT roundscore as score FROM teaminfo WHERE teamid=%s) as score"
            row = cc.execute(sql, (teamid, teamid))
            if row != 1:
                self.error = "Too many score of same team"
                return False
            score = cc.fetchall()
            sql = "UPDATE teaminfo SET totalscore=%s WHERE teamid=%s;"
            cc.execute(sql, (score[0]['score'], teamid))
        self.c.commit()
        return True

    def GetQidList(self):
        with self.c.cursor() as cc:
            sql = "SELECT uq,lq FROM qinfo q;"
            row = cc.execute(sql)
            if row == 0:
                self.error = "Data schema error"
                return False
            return cc.fetchall()

    def Test(self):
        with self.c.cursor() as cc:
            sql = "Select NOW()"
            row = cc.execute(sql)
            if row != 1:
                self.error = "Not Connect"
                return False
            return True
