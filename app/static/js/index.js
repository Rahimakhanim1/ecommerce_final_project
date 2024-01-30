var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var page = this.dataset.page
        if (user==='AnonymousUser'){
            console.log('User NOT logged in')
        }else{
            updateUserOrder(productId,action,page)
        }
    })
}

function updateUserOrder(productId,action,page){
    console.log('User is logged 16')

    var url = 'http://127.0.0.1:8003/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftokenIndex,
        },
        body: JSON.stringify({
            'productId': productId,'action':action,'page':page})
    })
    .then((response)=>{
        return response.json()
    })

    .then((data) =>{
       
       console.log(data)
       return data
       location.reload()
     
     
       
    })
}

