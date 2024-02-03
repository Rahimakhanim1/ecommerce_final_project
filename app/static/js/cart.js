var updateBtns = document.getElementsByClassName('update-cart')
var info = document.getElementById('info')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var page = 'shop'
        if (user==='AnonymousUser'){
            console.log('User NOT logged in')
        }else{
            updateUserOrder(productId,action,page)
        }
    })
}


function updateUserOrder(productId, action,page){
    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftokenShop,
        },
        body: JSON.stringify({
            'productId': productId,'action':action,'page':page})
                            }
        )
    .then((response)=>{
        return response.json()
    })

    .then((data) =>{
       
       console.log(data)
       return data     
       
    })
}

