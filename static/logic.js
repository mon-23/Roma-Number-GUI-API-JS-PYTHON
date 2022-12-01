






let btn_roma = document.querySelector('#btn_r');
let btn_number = document.querySelector('#btn_n');

// Roma to Number //
btn_roma.addEventListener('click', () => {
    let roma = document.querySelector('#roma');
    let dict = {'item': roma.value};
    let trans = JSON.stringify(dict);

    $.ajax({
        url: '/converter_1',
        type: 'POST',
        data: JSON.stringify(trans),
        contentType: 'application/json',
        success: function(data){
            data = JSON.parse(data);
            console.log(data);
            number.value = data['item'];
        },
        error: function(){
            number.value = 'Error';
        },
    });
});

// Number to Roma //
btn_number.addEventListener('click', () => {
    let number = document.querySelector('#number');
    let dict = {'item': number.value};
    let trans = JSON.stringify(dict);

    $.ajax({
        url: '/converter_2',
        type: 'POST',
        data: JSON.stringify(trans),
        contentType: 'application/json',
        success: function(data){
            data = JSON.parse(data);
            console.log(data);
            roma.value = data['item'];
        },
        error: function(){
            roma.value = 'Error';
        },
    });
});

// clear inputs //
let del_btn = document.querySelector('#del');
del_btn.addEventListener('click', () => {
    number.value =  '';
    roma.value = '';
});





