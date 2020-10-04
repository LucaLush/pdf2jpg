from pdf2image import convert_from_path
import os
import zipfile
import send2trash

#当前工程目录
cwd = os.getcwd()
#当前工程pdf文件夹
input_path = cwd +"\\PDF\\"
#中间过程目录
destination_path = cwd +"\\PPM\\"
#图像文件目录
image_save_path = cwd +"\\PPM 2 JPG\\"

def conversion(input_files):#输入pdf源文件列表
    """
    docstring
    """
    try:
        for x in input_files:#迭代pdf源文件
            source_file = input_path + x#获取绝对路径
            #获取图片文件夹应该叫什么名字
            jpg_filefolder = x
            jpg_filefolder = jpg_filefolder.replace('.pdf', '')
            #创建图片文件夹
            os.makedirs(image_save_path + jpg_filefolder)
            #转换PDF到目标文件夹
            convert_from_path(source_file,200,image_save_path + jpg_filefolder,fmt="JPEG", output_file="p", thread_count=6)

            f = zipfile.ZipFile(image_save_path + jpg_filefolder+ '.zip', 'w', zipfile.ZIP_DEFLATED)
            #f.write(image_save_path + jpg_filefolder)
            for d in os.listdir(image_save_path + jpg_filefolder):
                f.write(image_save_path + jpg_filefolder + '\\' + d , jpg_filefolder+'\\'+d)

            f.close()

            #压缩完成后将文件移送到回收站
            send2trash.send2trash(image_save_path + jpg_filefolder)
            
    except:
        return "Exception Occured"

    else:
        return "conversion successfull"

input_files = [f for f in os.listdir(input_path) if f.endswith('.pdf')]


if len(input_files)>0:
    print(conversion(input_files))
else:
    print("There are no input PDF files. Please paste some files in PDF Folder")


       
#convert_from_path('DORIHEDO18.pdf', 200, "output", fmt="JPEG", output_file="das", thread_count=6)
