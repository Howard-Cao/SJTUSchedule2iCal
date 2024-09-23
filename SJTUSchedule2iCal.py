'''
@author: UserDetained
@date: 2024-2-19
@version: 1.0
@description: 用于将 SJTU 教学安排自动转换为 iCal 文件
@license: GPL-3.0

@version: 1.1
@description: 增加了对报错信息的输出，与完成输出后提示语的延时

代码主要来自于 PhotonQuantum 的 pysjtu 项目中的 export.py，并由 UserDetained 修改了 bug 和文件保存逻辑，提升了易用性。
要了解关于此项目的更多信息，请访问 https://github.com/PhotonQuantum/pysjtu
'''

from pysjtu import Session, Client
import arrow
from ics import Calendar, Event
from datetime import datetime, timezone, timedelta, time, date
import collections.abc
from pathlib import Path
import time as t

desktopDir = Path.home() / "Desktop" # 此处涉及到路径问题，如果想要保存在其他位置，请修改此处

lesson_time = (((8, 0), (8, 45)),
               ((8, 55), (9, 40)),
               ((10, 0), (10, 45)),
               ((10, 55), (11, 40)),
               ((12, 0), (12, 45)),
               ((12, 55), (13, 40)),
               ((14, 0), (14, 45)),
               ((14, 55), (15, 40)),
               ((16, 0), (16, 45)),
               ((16, 55), (17, 40)),
               ((18, 0), (18, 45)),
               ((18, 55), (19, 40)),
               ((19, 55), (20, 40)),
               ((20, 55), (21, 40)))

def flatten(obj):
    for el in obj:
        if isinstance(el, collections.abc.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


# 循环输入用户名和密码，直到登录成功
while True:
    try:
        client = Client(Session(username=input("请输入 Jaccount 用户名:"), password=input("请输入 Jaccount 密码:"))) 
        break
    except Exception as error:
        print('登录失败，请检查用户名和密码是否正确，或关闭VPN代理后重试。')
        print('详细报错：'+error)

# 循环输入学年和学期，直到以正确的格式输入
while True:
    try:
        year, term = input("请输入学年和学期，如 2023-2024 学年第二学期请输入 2023-2:").split('-')
        schedule = client.schedule(int(year), int(term)-1)
        # 如果返回的 schedule 为空，说明输入的学年和学期不存在，需要重新输入
        if not schedule:
            raise SyntaxError
        break
    except SyntaxError:
        print("输入的学年和学期不存在，请检查是否输入了正确的学年和学期。")
    except:
        print("输入格式错误，请检查是否输入了正确的学年和学期。")

# term_start = client.term_start_date 
# 此处的逻辑有问题，需要手动输入学期开始日

# 循环输入学期开始日，直到以正确的格式输入     
while True:
    try:
        term_start_year, term_start_month, term_start_day = input("请输入学期开始日，格式为 YYYY-MM-DD:").split("-")
        term_start = date(int(term_start_year), int(term_start_month), int(term_start_day))
        break
    except:
        print("输入格式错误，请检查是否输入了正确的学期开始日。")

c = Calendar()
local_tz = datetime.now(timezone.utc).astimezone().tzinfo
for lesson in schedule:
    if "暂不开课" not in lesson.remark:
        for week in list(flatten(lesson.week)):
            lesson_day = term_start + timedelta(days=lesson.day + (week - 1) * 7-1)
            begin_time = time(*lesson_time[lesson.time[0]-1][0])
            end_time = time(*lesson_time[lesson.time[-1]-1][1])
            e = Event()
            e.name = lesson.name
            e.begin = arrow.get(datetime.combine(lesson_day, begin_time, local_tz))
            e.end = arrow.get(datetime.combine(lesson_day, end_time, local_tz))
            e.location = lesson.location
            c.events.add(e)

fn = desktopDir / "schedule.ics"
with open(fn, mode="w", encoding="utf-8") as f:
    f.write(c.serialize())
print(f"已生成 iCal 文件到 {fn}，后续导入请参考网络教程。祝你生活愉快 =)")
t.sleep(10)