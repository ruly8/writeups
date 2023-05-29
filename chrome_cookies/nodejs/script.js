localStorage.setItem("cp", "%ud800");
document.cookie = `${unescape(localStorage.getItem("cp"))} = asd`;
