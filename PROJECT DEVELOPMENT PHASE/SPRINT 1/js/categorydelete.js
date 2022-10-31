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
  var dbRef1 = firebase.database().ref("categoryList");
  // reference your database
  
  document.getElementById("deletebut").addEventListener("click", deletecat);
  function deletecat(e) {
    var categorytodelete = getElementVal("categoryname");
    var dbRef1 = firebase.database().ref("categoryList");
  
    dbRef1.child(categorytodelete).once("value", function (snapshot) {
      var exists = snapshot.val() !== null;
  
      if (exists) {
        dbRef1.remove();
        alert("Deleted Successfully");
        window.open("retailerhome.html", "_self");
      } else if (exists == false) {
        alert("Category does not exist");
      }
      window.open("categorydelete.html", "_self");
      
    });
  }
  
    
  const getElementVal = (id) => {
    return document.getElementById(id).value;
  };
  