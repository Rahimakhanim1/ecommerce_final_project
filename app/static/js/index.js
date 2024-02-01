var updateBtns = document.getElementsByClassName('update-cart')
var infoModal = document.getElementById('info-modal')
var closeInfoModal = document.getElementById('close-info-modal')
var info = document.getElementById('info')
console.log('rnjgkn')
console.log(infoModal)



closeInfoModal.addEventListener('click',function(){
    infoModal.style.display = 'none'
});

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var page = 'index'
        if (user==='AnonymousUser'){
            infoModal.style.display = 'flex';
            console.log('yoxsaann')
        }else{
            updateUserOrder(productId,action,page)
        }
    })
}

function updateUserOrder(productId,action,page){
    console.log('User is logged 16')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftokenIndex,
        },
        body: JSON.stringify({
            'productId': productId,'action':action,'page':page}),
            
        success: function(dataa){
                info.innerHTML(dataa)
            }
        
        })
    .then((response)=>{
        return response.json()
    })

    .then((data) =>{
       
       console.log(data)
       return data
   
     
     
       
    })
}


