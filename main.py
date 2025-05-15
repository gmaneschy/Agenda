import schedule
import time as tm
from datetime import time
from schedule import repeat, every

# schedule.every().second.do(tarefa)
# schedule.every(10).seconds.do(tarefa)
# schedule.every(5).weeks.do(tarefa)
# schedule.every().day.at("14:09").do(tarefa)
# schedule.every().day.at(":09").do(tarefa)
# schedule.every().second.until("14:09").do(tarefa)
# schedule.every().second.until(time(hour=14, minute=9, second=2)).do(tarefa)
# @repeat(every().second)

"""
class Agenda:
    def __init__(self, descricao, hora):
        self.descricao = descricao
        self.hora = hora


    def tarefa(self):
        def_desc = input("Descrição:")
        self.descricao = def_desc

        s = int(input(""))
        time = s
        self.hora = time
        schedule.every(self.hora).seconds(self.descricao)
        print(f"{self.descricao} às {self.hora}")

Agenda(descricao= None, hora= None)

while True:
    schedule.run_pending()
    tm.sleep(1)
"""
"""@repeat(every().second.until(time(14, 9, 2)))
def tarefa():
    print("Hora de acordar!")

while True:
    schedule.run_pending()
    tm.sleep(1)"""

