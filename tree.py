# encoding: utf-8

#initial version, refer to: http://www.iteye.com/topic/494257
#make some improvements for Linux
#
#TODO: handle symbol links and corrupted links/files

import os
import sys

class dir(object):
    def __init__(self):
        self.SPACE = ""
        self.list = []
      
    def getCount(self, destDir):
        files = os.listdir(destDir)
        count = 0;
        for file in files:
            pathname = destDir + os.sep + file
            if os.path.isfile(pathname):
                count += 1
        return count
        
    def getDirTree(self, destDir):
        files = os.listdir(destDir)
        fileNum = self.getCount(destDir)
        tmpNum = 0
        for file in files:
            pathname = destDir + os.sep + file   
            size = os.path.getsize(pathname)
            if os.path.isfile(pathname):
                tmpNum = tmpNum +1  
                if (tmpNum != fileNum):
                    self.list.append(str(self.SPACE) + "|--" + file + "\n")
                else:  
                    self.list.append(str(self.SPACE) + "'--" + file + "\n")
            if os.path.isdir(pathname):
                self.list.append(str(self.SPACE) + "|--" + file + "\n")
                #into sub directory
                self.SPACE = self.SPACE + "|  "
                self.getDirTree(pathname)
                # if iterator of sub directory is finished, reduce "|  "
                self.SPACE = self.SPACE[:-4]   
        return self.list

    def writeTree(self, pathname):
        f = open(pathname, 'w')
        f.writelines(self.list)
        print "ok"
        f.close()

if __name__ == '__main__':
    d = dir()
    postfix='curdir'
    paths=[]
    if len(sys.argv)<2:
        d.getDirTree("./")
    else:
        postfix=sys.argv[1]
        if postfix[0]=='/':
            postfix=postfix[1:]
        paths=postfix.split(os.sep)
        #print paths
        postfix=paths[-1]
        #print 'sys.arg:',len(sys.argv),sys.argv[1]
        d.getDirTree(sys.argv[1])
    outputname='tree_'+postfix+'.txt'
    #print outputname
    d.writeTree(outputname)
