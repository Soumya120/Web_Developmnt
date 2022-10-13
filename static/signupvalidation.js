function validates(){
    alerts=[]
    var fname = document.forms["signup"]["first_name"].value;
    var lname = document.forms["signup"]["last_name"].value;
    var em = document.forms["signup"]["email"].value;
    var pass = document.forms["signup"]["password"].value;
    var confirm_pass = document.forms["signup"]["confirm_password"].value;
    var gender = document.forms["signup"]["gender"].value;
    var phone = document.forms["signup"]["phone"].value;
    var role = document.forms["signup"]["role"].value;
    
    if(fname==""){
        alerts.push('Please enter First Name.');
    }
    if(lname==""){
        alerts.push('Please enter Last Name.');
    }
    if(em==""){
        alerts.push('Please enter your username.');
    }
    if(pass==""){
        alerts.push('Please enter your Password.');
    }
    if(confirm_pass==""){
        alerts.push('Please confirm your password.')
    }
    if(pass!==confirm_pass){
        alerts.push('Your passwords do not match')
    }
    if(gender==""){
        alerts.push('Please enter Gender.');
    }
    if(phone==""){
        alerts.push('Please enter phone number.');
    }
    
    if(alerts.length!=0){
        alert(alerts.join("\r\n"));
        event.preventDefault();
    }
}