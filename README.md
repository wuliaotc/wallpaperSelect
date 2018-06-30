# wallpaperSelect

#依赖:
Python 3.7
pillow

#教程:
python官网下载 python 3.7  https://www.python.org/downloads/release/python-370/
  windows系统:
    更新pip:cmd命令 python -m pip install --upgrade pip
    安装pillow模块: cmd命令 python -m pip intsall pillow

#用法:使用文本编辑器更改wallpaper.py中设置项(文本编辑器推荐使用notepad++)

  H_width=1920  #设备分辨率宽度
  H_length=1080 #设备分辨率长度

  value=1.2 #不一定有完全符合比例要求的图片,使用此项完成模糊筛选

  path='F:\壁纸' #来源图片顶级目录,即我们从这个目录里选择图片
  exts=('png','jpg','bmp')#筛选图片扩展名

  targetDir='F:\筛选'#筛选出的图片的输出目录(清晰度较高的)

  targetDir_Low='F:\筛选\low'#筛选出的图片中清晰度较低的输出目录

  对于清晰度较低的二次元图片,建议使用waifu2x扩展分辨率

警告:
  大小过大的图片会被脚本跳过,以防止图片炸弹攻击
