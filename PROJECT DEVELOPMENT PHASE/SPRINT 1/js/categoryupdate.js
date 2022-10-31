
        var cattoupdate="Groceries";
        const firebaseConfig = {
    apiKey: "AIzaSyBppWHnNYXSpDPyDLPU4n71ET3RtQlnYq0",
    authDomain: "categorylist-7bd45.firebaseapp.com",
    databaseURL: "https://categorylist-7bd45-default-rtdb.firebaseio.com",
    projectId: "categorylist-7bd45",
    storageBucket: "categorylist-7bd45.appspot.com",
    messagingSenderId: "910020944578",
    appId: "1:910020944578:web:6383eb167c973a8c5c115b"
  };
  firebase.initializeApp(firebaseConfig);

  // reference your database
  var categoryListDb = firebase.database().ref("categoryList");

  
  document.getElementById("updatebtn").addEventListener("click", submitForm);
  function submitForm(e){
    e.preventDefault();
  var oldcategoryname =document.getElementById("oldcategoryname");
 
  var dbRef1 = firebase.database().ref("categoryList/"+oldcategoryname.value);
  dbRef1.remove();     
    var categoryname = getElementVal("newcategoryname");
    saveMessages(categoryname); 
    alert("Category updated successfully..");
    window.open("retailerhome.html","_self");   
    
   
  }
  
  const saveMessages = (categoryname) => {
    var categoryListDbnew = firebase.database().ref("categoryList/"+categoryname);
    var newCategoryForm = categoryListDbnew.push();
  
    newCategoryForm.set({
     categoryname:categoryname,
    });
  };
  
  const getElementVal = (id) => {
    return document.getElementById(id).value;
  };

  
  
 
  