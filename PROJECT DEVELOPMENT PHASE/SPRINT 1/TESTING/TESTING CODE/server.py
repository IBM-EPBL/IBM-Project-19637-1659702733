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
@app.route('/openviewcat')
def openviewcat():
  return render_template('viewcategory.html')


if __name__ == '__main__':
  app.run(debug=True)