function setYear(val) {
    var sel = document.getElementById('select2');
    var length = sel.options.length;
    for (i = length-1; i >= 0; i--) {
        sel.options[i] = null;
    }
    for (let i = val; i < 2021; i++) {
        var opt = document.createElement('option');
        opt.text = i;
        sel.add(opt);
    }
}