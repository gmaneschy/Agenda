import schedule
import time as tm
from datetime import time
from schedule import repeat, every

# @repeat(every().second)
@repeat(every().second.until(time(14, 9, 2)))
def tarefa():
    print("Hora de acordar!")

# schedule.every().second.do(tarefa)
# schedule.every(10).seconds.do(tarefa)
# schedule.every(5).weeks.do(tarefa)
# schedule.every().day.at("14:09").do(tarefa)
# schedule.every().day.at(":09").do(tarefa)
# schedule.every().second.until("14:09").do(tarefa)
# schedule.every().second.until(time(hour=14, minute=9, second=2)).do(tarefa)

while True:
    schedule.run_pending()
    tm.sleep(1)