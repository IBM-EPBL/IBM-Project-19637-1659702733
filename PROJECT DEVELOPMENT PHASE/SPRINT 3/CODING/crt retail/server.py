from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')
@app.route('/login',methods=['POST','GET'])
def login():
  import ibm_db;
  try:    
    fetch_pass=''
    username = request.form['username']
    password = request.form['password']
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
    global userid
    select_sql="SELECT * FROM REGISTER "    
    details =ibm_db.exec_immediate(conn,select_sql) 
    while ibm_db.fetch_row(details) !=False:
     if ibm_db.result(details,1)==username:
      fetch_pass=ibm_db.result(details,2)
      role=ibm_db.result(details,6)
   
    if fetch_pass== password and role=="Admin":
     return render_template('retailerhome.html')
    elif fetch_pass==password and role=="Employee":
      return render_template('employeehome.html')
    else:
      message='username/password incorect'
      return render_template('index.html',message)
      
  except:
   
    return render_template('index.html',message='exception')
@app.route('/openaddcategory')
def openaddcategory():
  return render_template('categoryadd.html')

    
@app.route('/addcat',methods=['POST','GET'])
def addcat():  
    import ibm_db,sys;
    try:     
     
     categoryname = request.form.get("category_name")       
     conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
     global userid
     insert_sql="INSERT INTO CATEGORY VALUES(?)"
     prep_stmt=ibm_db.prepare(conn,insert_sql)
     ibm_db.bind_param(prep_stmt,1,categoryname)
     ibm_db.execute(prep_stmt) 
     
     return render_template('retailerhome.html',message="category added successfully")     
    except:
     return render_template('categoryadd.html',message= sys.exc_info()[0])
@app.route('/opendelcategory')
def opendelcategory():
  return render_template('categorydelete.html')

@app.route('/delcat',methods=['POST','GET'])
def delcat():  
    import ibm_db,sys;
    try:
     count=0
     categoryname = request.form.get("category_name")   
     conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
     global userid
     select_sql="SELECT * FROM CATEGORY "    
     details =ibm_db.exec_immediate(conn,select_sql) 
     while ibm_db.fetch_row(details) !=False:
       ans=ibm_db.result(details,0)
       ans=ans.strip()
       if ans==categoryname:
        count=count+1
     if count>=1:    
      delete_sql="DELETE FROM CATEGORY WHERE Name = ? "     
      prep_stmt=ibm_db.prepare(conn,delete_sql)    
      ibm_db.bind_param(prep_stmt,1,categoryname)
      ans=ibm_db.execute(prep_stmt) 
      return render_template('retailerhome.html',message="Deleted successfully")    
     else:
      return render_template('retailerhome.html',message="No such category exists") 
    
    except:
     return render_template('categorydelete.html',message= sys.exc_info()[0])
@app.route('/openupcategory')
def openupcategory():
  return render_template('categoryupdate.html')
@app.route('/upcat',methods=['POST','GET'])
def upcat():  
    import ibm_db,sys;
    try:
     count=0
     oldcategoryname = request.form.get("old_category_name")  
     newcategoryname = request.form.get("new_category_name")  
     conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
     global userid
     select_sql="SELECT * FROM CATEGORY "    
     details =ibm_db.exec_immediate(conn,select_sql) 
     while ibm_db.fetch_row(details) !=False:
       ans=ibm_db.result(details,0)
       ans=ans.strip()
       if ans==oldcategoryname:
        count=count+1
     if count>=1:    
      delete_sql="UPDATE CATEGORY SET (Name)=('"+newcategoryname+"') WHERE Name = '"+oldcategoryname+"' "
      ibm_db.exec_immediate(conn,delete_sql)  
      return render_template('retailerhome.html',message="Updated successfully")    
     else:
      return render_template('retailerhome.html',message="No such category exists") 
    
    except:
     return render_template('categorydelete.html',message= sys.exc_info()[0])
@app.route('/openviewcategory')
def openviewcategory():
  return render_template('categoryview.html')

@app.route('/openaddpro')
def openaddpro():
     import ibm_db;
     optionval=[]
     conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
     global userid
     select_sql="SELECT * FROM CATEGORY "    
     details =ibm_db.exec_immediate(conn,select_sql) 
     while ibm_db.fetch_row(details) !=False:
       optionval.append(ibm_db.result(details,0))
     return render_template('addproduct.html',options=optionval)
@app.route('/addpro',methods=['POST','GET'])
def addpro():
  import ibm_db,sys;
  try:  
    proname=request.form.get("pro_name")     
    category=request.form.get("category_name")  
    Quantity=request.form.get("quantity")  
    price=request.form.get("price")  
    criticalstock=request.form.get("critical_stock")  
    profit=request.form.get("profit")  
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
    global userid
    insert_sql="Insert into PRODUCT(ID,Name,Category,Quantity,Price,CriticalStock,profit) values(DEFAULT,?,?,?,?,?,?)"
    prep_stmt=ibm_db.prepare(conn,insert_sql)
    ibm_db.bind_param(prep_stmt,1,proname)
    ibm_db.bind_param(prep_stmt,2,category)
    ibm_db.bind_param(prep_stmt,3,Quantity)
    ibm_db.bind_param(prep_stmt,4,price)
    ibm_db.bind_param(prep_stmt,5,criticalstock)
    ibm_db.bind_param(prep_stmt,6,profit)    
    ibm_db.execute(prep_stmt)    
    return render_template('retailerhome.html',message="Product added successfully..")
  except:
    return render_template('retailerhome.html',message="Product Not added ..")
@app.route('/opendelpro')
def opendelpro():
     import ibm_db;
     optionval=[]
     conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
     global userid
     select_sql="SELECT * FROM PRODUCT "    
     details =ibm_db.exec_immediate(conn,select_sql) 
     while ibm_db.fetch_row(details) !=False:
       optionval.append(ibm_db.result(details,1))
     return render_template('deleteproduct.html',options=optionval)
@app.route('/delpro',methods=['POST','GET'])
def delpro():  
    import ibm_db,sys;
    try:     
     proname = request.form.get("product_name")   
     conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
     global userid         
     delete_sql="DELETE FROM PRODUCT WHERE Name = ? "     
     prep_stmt=ibm_db.prepare(conn,delete_sql)    
     ibm_db.bind_param(prep_stmt,1,proname)
     ans=ibm_db.execute(prep_stmt) 
     return render_template('retailerhome.html',message="Deleted successfully")      
    
    except:
     return render_template('retailerhome.html',message= "Not deleted")
@app.route('/openuppro')
def openuppro():
  import ibm_db;
  optionval=[]
  catval=[]
  conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
  global userid
  select_sql="SELECT * FROM PRODUCT "    
  details =ibm_db.exec_immediate(conn,select_sql) 
  while ibm_db.fetch_row(details) !=False:
   optionval.append(ibm_db.result(details,1))
  select_sql2="SELECT * FROM CATEGORY "    
  details2 =ibm_db.exec_immediate(conn,select_sql2) 
  while ibm_db.fetch_row(details2) !=False:
       catval.append(ibm_db.result(details2,0))
  return render_template('updateproduct.html',options=optionval,message=catval)
@app.route('/uppro',methods=['POST','GET'])
def uppro():  
    import ibm_db,sys;
    try:     
      oldproname = request.form.get("protoup")
      proname=request.form.get("pro_name")     
      category=request.form.get("category_name")  
      Quantity=request.form.get("quantity")  
      price=request.form.get("price")  
      criticalstock=request.form.get("critical_stock")  
      profit=request.form.get("profit")
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
      return render_template('retailerhome.html',message="Product updated successfully..")
    except:
      return render_template('retailerhome.html',message="Product Not updated ")

@app.route('/openviewcat')
def openviewcat():
  return render_template('viewcategory.html')
@app.route('/opendelorder')
def opendelorder():
     import ibm_db;
     optionval=[]
     conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
     global userid
     select_sql="SELECT * FROM PRODUCT "    
     details =ibm_db.exec_immediate(conn,select_sql) 
     while ibm_db.fetch_row(details) !=False:
       optionval.append(ibm_db.result(details,1))
     return render_template('deliveryorder.html',options=optionval)
@app.route('/mkdelorder',methods=['GET','POST'])
def mkdelorder():
  from datetime import date
  import ibm_db;
  tentdeldate=request.form.get('delivery_date')
  custname=request.form.get('customername')
  phno=request.form.get('phoneno')
  product=request.form.get('product_name')
  quantity=request.form.get('quantity')
  status='booked'
  amount=0.0
  today=date.today()
  curr_quant=0
  dbquant=0
  criticalstock=0
  try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
    
    global userid 
    select_sql="SELECT Price,Quantity FROM PRODUCT WHERE NAME = '"+product+"'"     
    details=ibm_db.exec_immediate(conn,select_sql)     
    while ibm_db.fetch_row(details) !=False:
      amount=ibm_db.result(details,0)*int(quantity)
      curr_quant=ibm_db.result(details,1)-int(quantity)
    if curr_quant<=criticalstock or dbquant<=criticalstock:
      import os
      import ssl
      import smtplib
      from email.message import EmailMessage
      email_sender = 'dhksretailinv@gmail.com'
      email_password = 'eqicnsxxfqamzbky'
      email_receiver = 'dharshu.9101@gmail.com'

      subject = 'Critical stock Notification'
      body = """
       There is a risk of Low stock Product name:
      """+product

      en = EmailMessage()
      en['From'] = email_sender
      en['To'] = email_receiver
      en['Subject'] = subject
      en.set_content(body)

      context = ssl.create_default_context()

      with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smpt:
        smpt.login(email_sender,email_password)
        smpt.sendmail(email_sender,email_receiver,en.as_string()) 
        
    if curr_quant>=0:  
      update_sql="UPDATE PRODUCT SET (Quantity)=(?) WHERE Name = ?"
      prep_stmt=ibm_db.prepare(conn,update_sql)
      ibm_db.bind_param(prep_stmt,1,curr_quant)
      ibm_db.bind_param(prep_stmt,2,product)
      ibm_db.execute(prep_stmt)
      insert_sql="insert into deliveryorders values(?,?,?,?,?,?,?,?)" 
      prep_stmt2=ibm_db.prepare(conn,insert_sql)
      ibm_db.bind_param(prep_stmt2,1,custname)
      ibm_db.bind_param(prep_stmt2,2,phno)
      ibm_db.bind_param(prep_stmt2,3,product)
      ibm_db.bind_param(prep_stmt2,4,quantity)
      ibm_db.bind_param(prep_stmt2,5,amount)
      ibm_db.bind_param(prep_stmt2,6,today)
      ibm_db.bind_param(prep_stmt2,7,tentdeldate)
      ibm_db.bind_param(prep_stmt2,8,status)
      ibm_db.execute(prep_stmt2)
      insert_sql2="insert into order values(?,?,?,?,?,?)" 
      prep_stmt3=ibm_db.prepare(conn,insert_sql2)
      ibm_db.bind_param(prep_stmt3,1,custname)
      ibm_db.bind_param(prep_stmt3,2,phno)
      ibm_db.bind_param(prep_stmt3,3,product)
      ibm_db.bind_param(prep_stmt3,4,quantity)
      ibm_db.bind_param(prep_stmt3,5,amount)
      ibm_db.bind_param(prep_stmt3,6,today)
      ibm_db.execute(prep_stmt3)      
      return render_template('retailerhome.html',message="Order successfull!!" )
    else:
      return render_template('retailerhome.html',message="no stock")
  except:
    return render_template('retailerhome.html',message="not successfull")
@app.route('/openviewpro')
def openviewpro():
  return render_template('viewproduct.html')
@app.route('/openviewpurchase')
def openviewpurchase():
  return render_template('viewpurchase.html')
@app.route('/openviewsummary')
def openviewsummary():
  return render_template('viewsummary.html')
@app.route('/openaddemp')
def openaddemp():
  return render_template('addemployee.html')
@app.route('/addemp',methods=['POST','GET'])
def addemp():
  import ibm_db,sys;
  try:  
    name=request.form.get('emp_name')
    username='employee@'+name
    password=username+'123'
    mailid=request.form.get('mail_id')
    phno=request.form.get('ph_no')
    Gender=request.form.get('Gender')
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
    return render_template('retailerhome.html',message="Employee details addedd successfully...")     
  except:
    return render_template('retailerhome.html',message="Employee details Not addedd ")     
@app.route('/opendelemp')
def opendelemp():
     import ibm_db;
     optionval=[]
     conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
     global userid
     select_sql="SELECT * FROM REGISTER WHERE Role='Employee'"    
     details =ibm_db.exec_immediate(conn,select_sql) 
     while ibm_db.fetch_row(details) !=False:
       optionval.append(ibm_db.result(details,0))
     return render_template('deleteemployee.html',options=optionval)
@app.route('/delemp',methods=['POST','GET'])
def delemp():  
    import ibm_db;
    try:     
     empname = request.form.get("emp_name")   
     conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
     global userid         
     delete_sql="DELETE FROM REGISTER WHERE Name = ? "     
     prep_stmt=ibm_db.prepare(conn,delete_sql)    
     ibm_db.bind_param(prep_stmt,1,empname)
     ans=ibm_db.execute(prep_stmt) 
     return render_template('retailerhome.html',message="Deleted successfully")      
    
    except:
     return render_template('retailerhome.html',message= "Not deleted")
@app.route('/openupemp')
def openupemp():
     import ibm_db;
     optionval=[]
     conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
     global userid
     select_sql="SELECT * FROM REGISTER WHERE Role='Employee'"    
     details =ibm_db.exec_immediate(conn,select_sql) 
     while ibm_db.fetch_row(details) !=False:
       optionval.append(ibm_db.result(details,0))
     return render_template('updateemployee.html',options=optionval)
@app.route('/upemp',methods=['POST','GET'])
def upemp():  
    import ibm_db;
    try:     
      oldempname = request.form.get("old_emp_name")
      name=request.form.get('emp_name')
      mailid=request.form.get('mail_id')
      phno=request.form.get('ph_no')
      Gender=request.form.get('Gender')
      conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
      global userid   
      update_sql="UPDATE REGISTER SET (Name,Mailid,phno,Gender)=(?,?,?,?) WHERE Name = ?"
      prep_stmt=ibm_db.prepare(conn,update_sql)
      ibm_db.bind_param(prep_stmt,1,name)
      ibm_db.bind_param(prep_stmt,2,mailid)
      ibm_db.bind_param(prep_stmt,3,phno)
      ibm_db.bind_param(prep_stmt,4,Gender)
      ibm_db.bind_param(prep_stmt,5,oldempname)   
      ibm_db.execute(prep_stmt) 
      return render_template('retailerhome.html',message="Details updated successfully..")
    except:
      return render_template('retailerhome.html',message="Details Not updated ")
@app.route('/openorder')
def openorder():
     import ibm_db;
     optionval=[]
     conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
     global userid
     select_sql="SELECT * FROM PRODUCT "    
     details =ibm_db.exec_immediate(conn,select_sql) 
     while ibm_db.fetch_row(details) !=False:
       optionval.append(ibm_db.result(details,1))
     return render_template('order.html',options=optionval)
@app.route('/mkorder',methods=['GET','POST'])
def mkorder():
  from datetime import date
  import ibm_db;
  custname=request.form.get('customername')
  phno=request.form.get('phoneno')
  product=request.form.get('product_name')
  quantity=request.form.get('quantity')
  amount=0.0
  today=date.today()
  curr_quant=0
  dbquant=0
  criticalstock=0
  try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hhp00822;PWD=KmXijbm6bjkzaEEp","", "")  
    
    global userid 
    select_sql="SELECT Price,Quantity,Criticalstock FROM PRODUCT WHERE NAME = '"+product+"'"     
    details=ibm_db.exec_immediate(conn,select_sql) 
    
    while ibm_db.fetch_row(details) !=False:
      amount=ibm_db.result(details,0)*int(quantity)
      dbquant=ibm_db.result(details,1)
      curr_quant=dbquant-int(quantity)
      criticalstock=ibm_db.result(details,2) 
    if curr_quant<=criticalstock or dbquant<=criticalstock:
      import os
      import ssl
      import smtplib
      from email.message import EmailMessage
      email_sender = 'dhksretailinv@gmail.com'
      email_password = 'eqicnsxxfqamzbky'
      email_receiver = 'dharshu.9101@gmail.com'

      subject = 'Critical stock Notification'
      body = """
       There is a risk of Low stock Product name:
      """+product

      en = EmailMessage()
      en['From'] = email_sender
      en['To'] = email_receiver
      en['Subject'] = subject
      en.set_content(body)

      context = ssl.create_default_context()

      with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smpt:
        smpt.login(email_sender,email_password)
        smpt.sendmail(email_sender,email_receiver,en.as_string()) 
    
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
      
      return render_template('retailerhome.html',message="Order successfull!!" )
    else:
      return render_template('retailerhome.html',message="no stock")
  except:
    return render_template('retailerhome.html',message="not successfull")
@app.route('/openviewprof')
def openviewprof():
  return render_template('viewemployee.html')
@app.route('/openhome')
def openhome():
  return render_template('retailerhome.html')




 

    









if __name__ == '__main__':
  app.run(debug=True)