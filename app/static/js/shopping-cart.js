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
        }})
    else{
    let data = {
        'items': [
           
        ]
    }   
    updateCart.forEach( function(item){  
        data.items.push(
            {
                "itemId":item.name,
                "itemValue":item.value,
            }
        )
       
     })
    }
   
})


