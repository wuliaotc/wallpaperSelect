# wallpaperSelect

#依赖:<br>
>>##Python 3.7<br>
  ##pillow<br>

#教程:<br>
>>##python官网下载 python 3.7  https://www.python.org/downloads/release/python-370<br>
  ##windows系统:<br>
  ###更新pip:cmd命令 python -m pip install --upgrade pip<br>
  ###安装pillow模块: cmd命令 python -m pip intsall pillow<br>

#用法:使用文本编辑器更改wallpaper.py中设置项(文本编辑器推荐使用notepad++)<br>
>>##H_width=1920  #设备分辨率宽度<br>
  ##H_length=1080 #设备分辨率长度<br>
  ##value=1.2 不一定有完全符合比例要求的图片,使用此项完成模糊筛选<br>
  ##path='F:\壁纸' 来源图片顶级目录,即我们从这个目录里选择图片<br>
  ##exts=('png','jpg','bmp')筛选图片扩展名<br>
  ##targetDir='F:\筛选'筛选出的图片的输出目录(清晰度较高的)<br>
  ##targetDir_Low='F:\筛选\low'筛选出的图片中清晰度较低的输出目录<br>
  ###对于清晰度较低的二次元图片,建议使用waifu2x扩展分辨率<br>

#警告:<br>
>>##大小过大的图片会被脚本跳过,以防止图片炸弹攻击<br>
