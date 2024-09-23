# SJTU Schedule -> iCal 📅
A user-friendly way to export SJTU lecture schedules as iCalender files.

将你的交大课程表导出为 .ics 文件，以便导入到任何一个日程管理软件中！

## Usage/使用方法 🚀
For Windows users, you can directly download and double click the .EXE file. For Mac or Linux users you may need to download the .py script and run it using your own interpreter. No matter what platform you are on, **please make sure you have Internet connection when using it.**

如果你是 Windows 用户，你可以直接下载 .exe 文件并双击运行；如果你是 Mac 或者 Linux 用户，你需要下载 Python 脚本并且在你本地的解释器运行。但是无论如何，在运行时请确保有互联网连接。

After you get the iCalendar file, you can open it to check whether it is right or not. Then you can import it into your calendar applications such as Google Calendar Apple Calendar and Windows Calendar. For this step there are lots of tutorials on the Internet, so I would not list it here.

文件将默认导出到桌面，你可以打开来查看文件的记录是否正确。在此之后，你可以将其导入到任何一个支持导入 .ics 文件的日程管理软件之中，包括谷歌日历、苹果系统日历和微软日历。这一步有诸多教程可以查阅，在此处暂不列举。

## Tips/提示 💡

1. **The beginning date of the term is always the first Monday of the first week. 需要注意，学期开始日总是第一周的周一。**
2. Do not use VPN or proxy when using this tool. It may cause some issues while logging in. 使用时请勿使用代理VPN，否则可能导致登陆失败。
3. For iOS/iPadOS devices, you can drag the file to the "Calendar" app to import it. To delete all the imported events, delete the tag holding all the events in the "Calendar" app. Recommendation: import the events into a new tag for better organization. 对于 iOS/iPadOS 设备，你可以将文件拖动到 “Calendar” 应用中导入。要删除导入的日程，在 “Calendar” 应用中删除日程所属的标签。建议：导入你的课程日程到一个新的标签中，以便更好地管理。
4. For Windows devices, you can double click the file to import it into the "Calendar" app. 对于 Windows 设备，你可以直接双击文件导入到 “Calendar” 应用中。

## How it works/原理 🧠

1. The program uses the pysjtu library to get the schedule data from SJTU by starting a session.
2. The program then converts the data into an iCalendar file.
3. The iCalendar file is saved to your desktop.

## Afterword/另
The main fabric of the code comes from PhotonQuantum's pysjtu project. I fixed some bugs and changed the logic of file saving, and also made it user-friendlier.
Please also visit [PhotonQuantum-pysjtu](https://github.com/PhotonQuantum/pysjtu) to know more about pysjtu!

代码主要来自于 PhotonQuantum 的 pysjtu 项目中的 export.py，并由 UserDetained 修改了 bug 和文件保存逻辑，提升了易用性。
要了解更多关于 pysjtu 的信息，请访问 [PhotonQuantum-pysjtu](https://github.com/PhotonQuantum/pysjtu)。
