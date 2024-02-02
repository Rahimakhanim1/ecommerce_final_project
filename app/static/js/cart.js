var updateBtns = document.getElementsByClassName('update-cart')
var info = document.getElementById('info')

// for(var i = 0; i < updateBtns.length; i++){
//     updateBtns[i].addEventListener('click',function(){
//         var productId = this.dataset.product
//         var action = this.dataset.action
//         var page = 'shop'
//         if (user==='AnonymousUser'){
//             console.log('User NOT logged in')
//         }else{
//             updateUserOrder(productId,action,page)
//         }
//     })
// }
// function updateUserOrder(productId,action,page){
//     // Obtain the CSRF token from the hidden input field
//     var csrfToken = $('[name="csrfmiddlewaretoken"]').val();

//     // Get the data from the form
//     var formData = {
//         'productId': productId,
//         'action': action
//     };

//     // Send AJAX request
//     $.ajax({
//         type: 'POST',
//         url: '/update_item/',  // Adjust the URL as per your project structure
//         data: formData,
//         headers: {
//             'X-CSRFToken': csrfToken
//         },
//         success: function (response) {
//             if (response.status === 'success') {
//                 // Clear the form
//                 // $('#name').val('');
//                 // $('#age').val('');

//                 // Update the table
              
//             } else {
//                 alert('Error adding patient');
//             }
//         },
//         error: function () {
//             alert('Error adding patient');
//         }
//     });

// }

// function updateUserOrder(productId, action,page){

//     var url = '/update_item/'

//     fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type':'application/json',
//             'X-CSRFToken':csrftoken,
//         },
//         body: JSON.stringify({
//             'productId': productId,'action':action,'page':page})
//                             }
//         )
//     .then((response)=>{
//         return response.json()
//     })

//     .then((data) =>{
       
//        console.log(data)
//        return data
   
     
     
       
//     })
// }

