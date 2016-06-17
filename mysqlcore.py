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
            sql = "select teamid as tid from tqinfo where uq=%d and lq=%d;"
            row = cc.execute(sql, (uq, lq))
            if row == 0:
                return None
            return cc.fetchall()

    def AddRoundScore(self, teamid, score):
        with self.c.cursor() as cc:
            sql = "select roundscore as score from teaminfo where teamid=%d;"
            row = cc.execute(sql, (teamid,))
            if row == 0:
                return 'Data Schema error'
            result = cc.fetchall()
            sql = "UPDATE teaminfo SET roundscore=%d WHERE teamid=%d;"
            cc.execute(sql, (result['score'] + score, teamid))
        self.c.commit()
        return True

    def GetLqScore(self, lq):
        pass

    def CalcTotalScore(self, teamid):
        pass


a = core(user="root", passwd="toortoor")
print(a.error)
