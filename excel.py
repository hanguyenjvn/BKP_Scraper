__author__ = 'manh-ha'
import xlsxwriter

class excel_export:
    def __init__(self,name):
        self.name=name
        self.workbook = xlsxwriter.Workbook(name+'.xlsx',{'constant_memory': True})
        self.worksheet = self.workbook.add_worksheet()
        self.normal_format = self.workbook.add_format({
            'border': 1})
        self.month=''
        self.year=''
    def create_template(self):
        merge_format = self.workbook.add_format({
            'border': 1,
            'align': 'center',
            'valign': 'vcenter'})
        normal_format = self.workbook.add_format({
            'border': 1})
        print self.name
        #self.worksheet.merge_range('A1:E1', self.name, merge_format)
        self.worksheet.write(0,0,"Province",normal_format)
        self.worksheet.write(0,1,"District/City",normal_format)
        self.worksheet.write(0,2,"Commodity",normal_format)
        self.worksheet.write(0,3,"Month",normal_format)
        self.worksheet.write(0,4,"Year",normal_format)
        self.worksheet.write(0,5,"Price Type",normal_format)
        self.worksheet.write(0,6,"Price",normal_format)
        self.worksheet.write(0,7,"Unit",normal_format)
        self.worksheet.write(0,8,"Period",normal_format)
        self.worksheet.write(0,9,"Currency",normal_format)
        self.worksheet.write(0,10,"Data Source",normal_format)
        return;

    def write_retail_price(self,headings,datasets,row):
        for dataset in (datasets):
            for col in range(3,len(dataset)):
                self.worksheet.write(row,0,dataset[1],self.normal_format)
                self.worksheet.write(row,1,dataset[2],self.normal_format)
                self.worksheet.write(row,2,headings[col],self.normal_format)
                self.worksheet.write(row,3,self.month,self.normal_format)
                self.worksheet.write(row,4,self.year,self.normal_format)
                self.worksheet.write(row,5,"Retail",self.normal_format)
                self.worksheet.write_number(row,6,int(dataset[col]),self.normal_format)
                self.worksheet.write(row,7,'Rp/Kg',self.normal_format)
                self.worksheet.write(row,8,"Monthly",self.normal_format)
                self.worksheet.write(row,9,"IDR",self.normal_format)
                self.worksheet.write(row,10,"BKP",self.normal_format)
                row += 1
        return row;

    def write_sale_price(self,headings,datasets,row):
        for dataset in (datasets):
            for col in range(3,len(dataset)):
                self.worksheet.write(row,0,dataset[1],self.normal_format)
                self.worksheet.write(row,1,dataset[2],self.normal_format)
                self.worksheet.write(row,2,headings[col],self.normal_format)
                self.worksheet.write(row,3,self.month,self.normal_format)
                self.worksheet.write(row,4,self.year,self.normal_format)
                self.worksheet.write(row,5,"WholeSale",self.normal_format)
                self.worksheet.write_number(row,6,int(dataset[col]),self.normal_format)
                self.worksheet.write(row,7,'Rp/Kg',self.normal_format)
                self.worksheet.write(row,8,"Monthly",self.normal_format)
                self.worksheet.write(row,9,"IDR",self.normal_format)
                self.worksheet.write(row,10,"BKP",self.normal_format)
                row += 1
        return row;
    def close_file(self):
        self.workbook.close()
