var updateBtns = document.getElementsByClassName('update-cart')
var list = [].slice.call(document.getElementsByClassName("update-cart"))

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var page = 'index'
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
function updateUserOrder(productId,action,page){
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

