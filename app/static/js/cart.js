var updateBtns = document.getElementsByClassName('update-cart')
var infoModal = document.getElementById('info-modal')
var closeInfoModal = document.getElementById('close-info-modal')
var info = document.getElementById('info')
var list = [].slice.call(document.getElementsByClassName("update-cart"))


// closeInfoModal.addEventListener('click',function(){
//     infoModal.style.display = 'none'
// });

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var page = 'shop'
        if (user==='AnonymousUser'){
            list.map(function(item){
                item.onclick = function() {
              var toastElList = [].slice.call(document.querySelectorAll('.toast'))
              var toastList = toastElList.map(function(toastEl) {
                return new bootstrap.Toast(toastEl)
              })
              toastList.forEach(toast => toast.show()) 
            }})
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

