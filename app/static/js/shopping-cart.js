var updateBtns = document.getElementsByClassName('update-cart')
console.log('rahima')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        if (user==='AnonymousUser'){
            console.log('User NOT logged in')
        }else{
            updateUserOrder(productId,action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is logged 36')

    var url = 'http://127.0.0.1:8003/item_delete/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken2,
        },
        body: JSON.stringify({
            'productId': productId,'action':action})
    })
    .then((response)=>{
        return response.json()
    })

    .then((data) =>{
       
       console.log(data)
       return data
    //    location.reload()
     
     
       
    })
}

