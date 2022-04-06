document.querySelector('.add-book').onclick = function(){
    document.querySelector('#bg-popup').style.display =  'flex';
    document.querySelector('.add').style.display =  'block';
    document.querySelector('.update').style.display =  'none';
    document.querySelector('form').setAttribute("action", "addBook");
}

document.querySelector('.cancel').onclick = function(){
	document.querySelector('#bg-popup').style.display =  'none';
}

document.querySelectorAll('.edit').forEach(btnEdit=>{
    btnEdit.onclick = function(){
        document.querySelector('#bg-popup').style.display =  'flex';
        document.querySelector('.update').style.display =  'block';
        document.querySelector('.add').style.display =  'none';
        document.querySelector('form').setAttribute("action", `updateBook/${this.attributes[1].value}`);
        fetch(`/getRecord/${this.attributes[1].value}`)
        .then(response => {
            var promise = response.json();
            promise.then(res => {
                let book = res[0].fields;
                for(p in book)
                {
                    if(p != "image" && p != "description")
                        document.querySelector(`input[name='${p}']`).value = book[p];
                    else if(p == "description")
                        document.querySelector(`textarea[name='${p}']`).value = book[p];
                    else
                        continue;
                }
            })
        })
    }
})

function validate()
{
    if(document.querySelector("input[type='file']").value == '')
    {
        alert('chưa chọn ảnh');
    }
    else
        document.querySelector('form').submit();
}
