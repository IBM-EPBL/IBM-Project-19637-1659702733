const firebaseConfig = {
    apiKey: "AIzaSyBdvQAyqn9lo3YR76sGl5axihH04JoI5pk",
    authDomain: "loginform-382a7.firebaseapp.com",
    databaseURL: "https://loginform-382a7-default-rtdb.firebaseio.com",
    projectId: "loginform-382a7",
    storageBucket: "loginform-382a7.appspot.com",
    messagingSenderId: "532215484219",
    appId: "1:532215484219:web:e91cbc668a8f492f6db11e"
  };
  firebase.initializeApp(firebaseConfig);

// reference your database
var dbRef = firebase.database().ref('loginform');

dbRef.once("value").then(function(snapshot){
  var loginInfo=snapshot.val();
  document.getElementById("butt").addEventListener("click",function(){
    var username = document.getElementById("username");
    var password = document.getElementById("password");
    var role = document.getElementById("role");
    var val=0;
    snapshot.forEach(function(childSnapshot) {
      var childData = childSnapshot.val();
      var newArrayDataOfOjbect = Object.values(childData);  
      if (username.value==newArrayDataOfOjbect[2] && password.value==newArrayDataOfOjbect[0] && role.value==newArrayDataOfOjbect[1] && role.value=="retailer"){
      val=1;
           window.open("retailerhome.html","_self");     
      
      
      }
      else if(username.value==newArrayDataOfOjbect[2] && password.value==newArrayDataOfOjbect[0] && role.value==newArrayDataOfOjbect[1] && role.value=="employee"){
        val=1;
        window.open("employeehome.html","_self");        
      }
        }); 
         if(val == 0){
          alert(" Username/password incorrect");
        }      
  });
});



 
 


const getElementVal = (id) => {
  return document.getElementById(id).value;
};
