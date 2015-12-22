import sys
from PyQt4 import QtCore, QtGui
from GUI import *
import core
import excel
import threading



class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pB_ok,QtCore.SIGNAL("clicked()"), self.ok_clicked)
        QtCore.QObject.connect(self.ui.pB_close,QtCore.SIGNAL("clicked()"), self.close_clicked)
        self.index=['0','11','51','36','17','34','31','75','15','32','33','35','61','63','62','64','98','19','21','18','81','82','52','53','94','91','14','76','73','72','74','71','13','16','12']
        self.ui.timer.timeout.connect(self.elapsedTime)
        self.time=-1
        self.statstr=''
        self.ui.timer.start(1000)

    def elapsedTime(self):
        if self.time!=-1:
            self.time += 1
            self.ui.statusbar.showMessage(self.statstr+'. Elapsed Time: '+str(self.time)+' s')
            QtGui.QApplication.processEvents()

    def ok_clicked(self):
	#self.ui.statusbar.showMessage(str(self.ui.cB_province.currentText()))
        self.ui.pB_ok.setDisabled(True)
        QtGui.QApplication.processEvents()
        path = str(QtGui.QFileDialog.getExistingDirectory(None, "Select Directory"))
        class myThread (threading.Thread):
            def __init__(self, ui,index,path,parent):
                threading.Thread.__init__(self)
                self.ui = ui
                self.index=index
                self.path=path
                self.parent=parent
            def run(self):
                df=core.data_fetch()
                filename="BKP_Report_for_"+str(self.ui.cB_province.currentText()).strip()+"_"+str(self.ui.cB_month.currentText())+"_"+str(self.ui.cB_year.currentText())
                if self.path[-1]=='\\':
                    ee=excel.excel_export(self.path+filename)
                else:
                    ee=excel.excel_export(self.path+'\\'+filename)
                ee.create_template()
                ee.month=str(self.ui.cB_month.currentText())
                ee.year=str(self.ui.cB_year.currentText())
                row=1
                if self.ui.cB_province.currentIndex()>0:
                    self.parent.statstr="Getting data for "+str(self.ui.cB_province.currentText())
                    self.parent.time=0
                    self.ui.statusbar.showMessage("Getting data for "+self.ui.cB_province.currentText())
                    df.getdata(self.index[self.ui.cB_province.currentIndex()],str(self.ui.cB_month.currentText()),str(self.ui.cB_year.currentText()),'SALE')
                    row=ee.write_sale_price(df.headings,df.datasets,row)
                    df.getdata(self.index[self.ui.cB_province.currentIndex()],str(self.ui.cB_month.currentText()),str(self.ui.cB_year.currentText()),'RETAIL')
                    row=ee.write_retail_price(df.headings,df.datasets,row)
                elif self.ui.cB_province.currentIndex()==0:
                    for i in range(1,len(self.index)):
                        self.parent.statstr="Getting data for "+str(self.ui.cB_province.currentText())
                        self.parent.time=0
                        self.ui.statusbar.showMessage("Getting data for "+self.ui.cB_province.itemText(i))
                        df.getdata(self.index[i],str(self.ui.cB_month.currentText()),str(self.ui.cB_year.currentText()),'SALE')
                        row=ee.write_sale_price(df.headings,df.datasets,row)
                        df.getdata(self.index[i],str(self.ui.cB_month.currentText()),str(self.ui.cB_year.currentText()),'RETAIL')
                        row=ee.write_retail_price(df.headings,df.datasets,row)
                ee.close_file()
                self.parent.time=-1
                self.ui.statusbar.showMessage("Done! Check excel file:"+filename+".xlsx")
                self.ui.pB_ok.setDisabled(False)

        thread1 = myThread(self.ui,self.index,path,self)
        thread1.start()

    def close_clicked(self):
        QtCore.QCoreApplication.instance().quit()




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    myapp.ui.cB_province.currentIndex()
    sys.exit(app.exec_())
