function validates(){
    alerts=[]
    var fname = document.forms["addEmp"]["first_name"].value;
    var lname = document.forms["addEmp"]["last_name"].value;
    var em = document.forms["addEmp"]["email"].value;
    var pass = document.forms["addEmp"]["password"].value;
    var gender = document.forms["addEmp"]["gender"].value;
    var phone = document.forms["addEmp"]["phone"].value;
    var team_lead = document.forms["addEmp"]["team_lead"].value;
    var role = document.forms["addEmp"]["role"].value;
    var skills =  document.forms["addEmp"]["skill[]"];
    var Dskills = document.forms["addEmp"]["Dskill[]"];
    var hobbies = document.forms["addEmp"]["hobbies"].options;
    var selected = [];
    for(option of hobbies){
        if(option.selected){
            selected.push(option.value);
        }
    }
    var checkedskills = 0
    for (var i = 0; i < skills.length; i++) {
        if (skills[i].checked) {
            checkedskills++;
        }
    }
    var checkedDskills = 0
    for (var i = 0; i < Dskills.length; i++) {
        if (Dskills[i].checked) {
            checkedDskills++;
        }
    }
    
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
    if(gender==""){
        alerts.push('Please enter Gender.');
    }
    if(phone==""){
        alerts.push('Please enter phone number.');
    }
    if(team_lead==""){
        alerts.push('Please enter name of team lead.');
    }
    if(role==""){
        alerts.push('Please enter your role.');
    }
    if (checkedskills < 1) {
        alerts.push('Please select your technical skills.')
    }
    if (checkedDskills < 1) {
        alerts.push('Please select your databse skills.')
    }
    if(selected.length===0){
        alerts.push('Please enter hobbies.');
    }
    if(alerts.length!=0){
        alert(alerts.join("\r\n"));
        event.preventDefault();
    }
}