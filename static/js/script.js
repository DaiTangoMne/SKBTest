function disableOtherButtons(el){
    buttons = document.getElementById("sorting").getElementsByTagName("input");
//    [...buttons].forEach(btn => {
//        (btn == el)? null : btn.disabled = true;
//          console.log(btn);
//    });
    for (const btn of buttons){
        (btn == el)? null : btn.disabled = true;
    }
}