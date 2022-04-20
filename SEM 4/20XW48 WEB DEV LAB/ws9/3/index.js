function isEmail(str) {

    //valid email regexp
    regexp = /^\w+([\.!#$%&'*+/=?^_`{|}~-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/

    if (regexp.test(str)) {
        return true;
    }
    else {
        return false;
    }
}
let mail1 = `kartol@gmail.com`
let mail2 = `.jickserrrrrrr@hmail.com`
//testcases
document.querySelector(".result").innerHTML = mail1 + " => " + isEmail(mail1)
document.querySelector(".result").innerHTML += "<br>"
document.querySelector(".result").innerHTML += mail2 + " => " + isEmail(mail2)