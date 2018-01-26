# coding=utf-8
__author__ = 'lbs'
from win32com import client as wc
import os


def wordsToHtml(dir):
    # 批量把文件夹的word文档转换成html文件
    # 金山WPS调用，抢先版的用KWPS，正式版WPS
    word = wc.Dispatch('Word.Application')
    for path, subdirs, files in os.walk(dir):
        for wordFile in files:
            wordFullName = os.path.join(path, wordFile)
            doc = word.Documents.Open(wordFullName)
            wordFile2 = unicode(wordFile, "gbk")
            dotIndex = wordFile2.rfind(".")
            if (dotIndex == -1):
                print '********************ERROR: 未取得后缀名！'
            fileSuffix = wordFile2[(dotIndex + 1):]
            if (fileSuffix == "doc" or fileSuffix == "docx"):
                fileName = wordFile2[: dotIndex]
                htmlName = fileName + ".html"
                htmlFullName = os.path.join(unicode(path, "gbk"), htmlName)
                print u'生成了html文件：' + htmlFullName
                doc.SaveAs(htmlFullName, 8)
                doc.Close()
    word.Quit()
    print ""
    print "Finished!"

if __name__ == '__main__':
    wordsToHtml('f:/word')
