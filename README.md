# SJTU Schedule -> iCal 📅
A user-friendly way to export SJTU lecture schedules as iCalender files.

将你的交大课程表导出为 .ics 文件，以便导入到任何一个日程管理软件中！

## Important
The executable file for Windows users is not ready yet. I'm still looking for a way to upload the 40MB file to GitHub. 

.exe 文件尚未可用。由于文件过大，我正在寻找办法将它上传到 GitHub 上。当然，你仍然可以使用脚本。如果你有缩小打包 Python 脚本文件大小的方法，请提示我！

## Usage/使用方法 🚀
For Windows users, you can directly download and double click the .EXE file. For Mac or Linux users you may need to download the .py script and run it using your own interpreter. No matter what platform you are on, **please make sure you have Internet connection when using it.**

如果你是 Windows 用户，你可以直接下载 .exe 文件并双击运行；如果你是 Mac 或者 Linux 用户，你需要下载 Python 脚本并且在你本地的解释器运行。但是无论如何，在运行时请确保有互联网连接。

After you get the iCalendar file, you can open it to check whether it is right or not. Then you can import it into your calendar applications such as Google Calendar Apple Calendar and Windows Calendar. For this step there are lots of tutorials on the Internet, so I would not list it here.

文件将默认导出到桌面，你可以打开来查看文件的记录是否正确。在此之后，你可以将其导入到任何一个支持导入 .ics 文件的日程管理软件之中，包括谷歌日历、苹果系统日历和微软日历。这一步有诸多教程可以查阅，在此处暂不列举。

## Afterword/另
The main fabric of the code comes from PhotonQuantum's pysjtu project. I fixed some bugs and changed the logic of file saving, and also made it user-friendlier.
Please also visit [PhotonQuantum-pysjtu](https://github.com/PhotonQuantum/pysjtu) to know more about pysjtu!

代码主要来自于 PhotonQuantum 的 pysjtu 项目中的 export.py，并由 UserDetained 修改了 bug 和文件保存逻辑，提升了易用性。
要了解更多关于 pysjtu 的信息，请访问 [PhotonQuantum-pysjtu](https://github.com/PhotonQuantum/pysjtu)。
