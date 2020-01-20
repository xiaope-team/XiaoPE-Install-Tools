import os
print ("XiaoPE 安装工具")
print ("(c) 2020 XiaoPE。保留所有权利。")
print ("[1] 下载XiaoPE [2] 将XiaoPE写入到U盘 [3]退出")
choose = input("")
choose = int(choose)
if choose == 1:
    download = input ("请选择一个盘符以供下载临时文件（大写）（如下载到D盘就输入D)：")
    os.system("mkdir " + download + ":\XiaoPE-Download")
    download = download + ":\XiaoPE-Download"
    os.system("aria2c.exe -s 2 -x 2 -j 10 -d " + download + " https://d.xiaope.net/cn_xiaope_9.1_191228_x64.iso")
    os.system("pause")
if choose == 2:
    print ("警告!接下来将不会有任何提示!安装时将会格式化您的U盘!")
    drive = input ("请输入将要安装的U盘盘符（大写）（如要安装到F盘就输入F)：")
    drive = drive + ":"
    download = input ("请输入下载时输入的临时文件存储盘符（大写）（如下载到D盘就输入D)：")
    download = download + ":\XiaoPE-Download\cn_xiaope_9.1_191228_x64.iso"
    os.system("format " + drive +" /q /FS:FAT32 /y")
    os.system("7z.exe x " + download + " -o" + drive)
    print ("目前应该已经安装成功，请查看U盘下文件是否已经生成。")
    print ("如果遇到无法正常从U盘启动的问题，请自行使用相关工具修复引导。")
    os.system("pause")