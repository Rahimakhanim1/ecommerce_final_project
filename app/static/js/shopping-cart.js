let updateCart = document.querySelectorAll('.item-quantity')
$('.update-item-value').on('click',function(){
    if (user==='AnonymousUser'){
        list.map(function(item){
        item.onclick = function() {
          var toastElList = [].slice.call(document.querySelectorAll('.toast'))
          var toastList = toastElList.map(function(toastEl) {
            return new bootstrap.Toast(toastEl)
          })
          toastList.forEach(toast => toast.show()) 
        }})}
    else{
    let data = {
        'items': [     
        ]
    }   
    updateCart.forEach(function(item){  
        data.items.push(
            {
                "itemId":item.name,
                "itemValue":item.value,
            })
        })
    updateItemValue(data)
    }  
})


function updateItemValue(changedValue){
    var url = '/update_cart/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken2,
        },
        body: JSON.stringify({
            'data':changedValue}),     
        })
    .then((response)=>{
        return response.json()
    })

    .then((data) =>{
       
       return data
   
    })
}
