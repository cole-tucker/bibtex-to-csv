function setYear(val) {
    for (let i = val; i < 2021; i++) {
        var sel = document.getElementById('select2');
        var opt = document.createElement('option');
        opt.text = i;
        sel.add(opt);
    }
}