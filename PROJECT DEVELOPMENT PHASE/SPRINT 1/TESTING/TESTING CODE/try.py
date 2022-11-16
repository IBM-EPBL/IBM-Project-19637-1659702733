'''import ibm_db;
try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
    global userid
    msg=''
    username='Admin'   
    select_sql="SELECT * FROM REGISTER "    
    details =ibm_db.exec_immediate(conn,select_sql) 
    while ibm_db.fetch_row(details) !=False:
     if ibm_db.result(details,1)==username:
      fetch_pass=ibm_db.result(details,6)
    print(fetch_pass)
except:
    print("Unable to connect: ",ibm_db.conn_errormsg())'''
'''import ibm_db;
try:
    oldcategoryname="Stationary"
    newcategoryname="Groceries"
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
    global userid    
    count=0
    delete_sql="UPDATE CATEGORY SET (Name)=('"+newcategoryname+"') WHERE Name = '"+oldcategoryname+"' "
    ibm_db.exec_immediate(conn,delete_sql) '''


'''print("submitted connected")'''
'''msg=''
    category_name = 'Groceries'
    select_sql="SELECT * FROM CATEGORY "    
    details =ibm_db.exec_immediate(conn,select_sql) 
    while ibm_db.fetch_row(details) !=False:
        ans=ibm_db.result(details,0)
        ans=ans.strip()
        print(ans==category_name)

        
        
     
         
    print(count)'''
        
        

    
'''except:
    print("Unable to connect: ",ibm_db.conn_errormsg())'''

'''import ibm_db,sys;
try:     
     
    name="Dharshan"
    username='employee@'+name
    password=username+'123'
    mailid='dha.123@gmail.com'
    phno=9087075181
    Gender='Male'
    Role='Employee'
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
    global userid
    insert_sql="Insert into REGISTER(Name,Username,Password,Mailid,Phno,Gender,Role) values(?,?,?,?,?,?,?)"
    prep_stmt=ibm_db.prepare(conn,insert_sql)
    ibm_db.bind_param(prep_stmt,1,name)
    ibm_db.bind_param(prep_stmt,2,username)
    ibm_db.bind_param(prep_stmt,3,password)
    ibm_db.bind_param(prep_stmt,4,mailid)
    ibm_db.bind_param(prep_stmt,5,phno)
    ibm_db.bind_param(prep_stmt,6,Gender)    
    ibm_db.bind_param(prep_stmt,7,Role)    
    ibm_db.execute(prep_stmt)    
    print("Done")     
except:
    print("notdone..",sys.exc_info()[0])'''
    
'''oldproname="pencilbox"
proname="pen"     
category="Stationary"
Quantity=150
price=12.5
criticalstock=5
profit=2
import ibm_db;
try:
 conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
 global userid   
 update_sql="UPDATE PRODUCT SET (Name,Category,Quantity,Price,CriticalStock,profit)=(?,?,?,?,?,?) WHERE Name = ?"
 prep_stmt=ibm_db.prepare(conn,update_sql)
 ibm_db.bind_param(prep_stmt,1,proname)
 ibm_db.bind_param(prep_stmt,2,category)
 ibm_db.bind_param(prep_stmt,3,Quantity)
 ibm_db.bind_param(prep_stmt,4,price)
 ibm_db.bind_param(prep_stmt,5,criticalstock)
 ibm_db.bind_param(prep_stmt,6,profit)    
 ibm_db.bind_param(prep_stmt,7,oldproname)   
 ibm_db.execute(prep_stmt)    
 print("Done")      
except:
    print("not done..")

'''
from datetime import date
import ibm_db;
custname='Harini'
phno=9962822416
product='Pouch'
quantity=3
amount=0
today=date.today()
curr_quant=0
try:
 conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
 global userid 
 select_sql="SELECT Price,Quantity FROM PRODUCT WHERE NAME = '"+product+"'" 
 details=ibm_db.exec_immediate(conn,select_sql) 
 while ibm_db.fetch_row(details) !=False:
      amount=ibm_db.result(details,0)*quantity
      curr_quant=ibm_db.result(details,1)-quantity
 if curr_quant>=0:    
    update_sql="UPDATE PRODUCT SET (Quantity)=(?) WHERE Name = ?"
    prep_stmt=ibm_db.prepare(conn,update_sql)
    ibm_db.bind_param(prep_stmt,1,curr_quant)
    ibm_db.bind_param(prep_stmt,2,product)
    ibm_db.execute(prep_stmt)
    insert_sql="insert into order values(?,?,?,?,?,?)" 
    prep_stmt2=ibm_db.prepare(conn,insert_sql)
    ibm_db.bind_param(prep_stmt2,1,custname)
    ibm_db.bind_param(prep_stmt2,2,phno)
    ibm_db.bind_param(prep_stmt2,3,product)
    ibm_db.bind_param(prep_stmt2,4,quantity)
    ibm_db.bind_param(prep_stmt2,5,amount)
    ibm_db.bind_param(prep_stmt2,6,today)
    ibm_db.execute(prep_stmt2)
    print("Done")
 else:
    print("no stock") 
except:
    print("not done")


     