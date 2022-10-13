function validate(){
    alerts=[]
    var em = document.forms["login"]["email"].value;
    var pass = document.forms["login"]["password"].value;
    var role = document.forms["login"]["role"].value;
    if(em==""){
        alerts.push('Please enter your username.');
    }
    if(pass==""){
        alerts.push('Please enter your Password.');
    }
    if(role==""){
        alerts.push('Please select your role.');
    }
    if(alerts.length!=0){
        alert(alerts.join("\r\n"));
        event.preventDefault();
    }
}

