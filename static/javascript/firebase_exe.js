console.log("about to create username:", "creating");
         var myFirebaseRef = new Firebase("https://amber-heat-4308.firebaseio.com/");
         var myemail="444444eeetony@firebase.com";
         var mypassword="correcthorsebatterystaple";
         myFirebaseRef.createUser({
         email    : myemail,
         password : mypassword
          }, function(error, userData) {
          console.log("back from creating username:", "creating");
         if (error) {
          console.error("Error creating user:", error);
         } else {
         console.error("Successfully created user account with uid:", userData.uid);
         login(myemail,mypassword)
    console.log("Successfully created user account with uid:", userData.uid);
  }
});

function login(myemail,mypassword){
console.error("inside login");
myFirebaseRef.authWithPassword({
  email    : myemail,
  password : mypassword
}, function(error, authData) {
  if (error) {
    console.log("Login Failed!", error);
  } else {
    console.error("I have logged in");
  }
});


}