#install pandas to read the appropriate dataset
import pandas as pd
#create dataframe object named 'data' to store after reading data using pandas
#Use the path of the downloaded or created data
data=pd.read_csv(r"C:\bhargab drive\bhargab pypi packages\S2L.csv")

#install package and sub-module
from bhargabchipkg import chitest_rs

#object creating

obj=chitest_rs.ChiTest2(data,'salesman_id', 'saleflag', 'matched_table')
#method calling by taking two objects (table and intrprt)
table,intrprt=obj.chi_test()
#See the outputs
print("Interpreted result")
print(intrprt)
print("table result")
print(table)