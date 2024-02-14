let updateCart = document.querySelectorAll('.item-quantity')
$('.update-item-value').on('click',function(){
    if (user==='AnonymousUser'){
        console.log('istifadeci yoxdur')
      
    }
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
