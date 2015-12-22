import sys
import core
import excel


index=['0','11','51','36','17','34','31','75','15','32','33','35','61','63','62','64','98','19','21','18','81','82','52','53','94','91','14','76','73','72','74','71','13','16','12']


def get_data(month,year):
    df=core.data_fetch()
    filename="BKP_Report_for_All_"+month+"_"+year
    ee=excel.excel_export(filename)
    ee.create_template()
    ee.month=month
    ee.year=year
    row=1
    for i in range(1,len(index)):
    #for i in range(1,3):
        df.getdata(index[i],month,year,'SALE')
        row=ee.write_sale_price(df.headings,df.datasets,row)
        df.getdata(index[i],month,year,'RETAIL')
        row=ee.write_retail_price(df.headings,df.datasets,row)
    ee.close_file()

dates=[#['09','2012'],
      #['10','2012'],
      #['11','2012'],
      #['12','2012'],
      #['01','2013'],
      #['02','2013'],
      #['03','2013'],
      #['04','2013'],
      #['05','2013'],
      #['06','2013'],
      #['07','2013'],
      #['08','2013'],
      #['09','2013'],
      #['10','2013'],
      #['11','2013'],
      #['12','2013'],
      #['01','2014'],
      #['02','2014'],
      #['03','2014'],
      #['04','2014'],
      #['05','2014'],
      #['06','2014'],
      #['07','2014'],
      #['08','2014'],
      #['09','2014'],
      #['10','2014'],
      #['11','2014'],
      #['12','2014'],
      #['01','2015'],
      #['02','2015'],
      #['03','2015'],
      #['04','2015'],
      ['05','2015'],
      ['06','2015'],
      ['07','2015'],
      ['08','2015']
      ]

for date in dates:
    get_data(date[0],date[1])

#get_data('04','2015')
