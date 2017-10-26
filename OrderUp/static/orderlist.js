$(document).ready(function(){


     $('input[type="button"]').click(function() {
        console.log($(this))
        $(this).val('ready to pick up')
        $(this).css('background-color','#393499')
        // $(this).closest('div').remove();
     })

     $('#resturantid').hide();
     var id = $("#resturantid").val()

})

function getList(id) {
    id = $("#resturantid").val()

    $.ajax({
        url: "/OrderUp/getlist/"+id,
        dataType : "json",
        success: updateList
    });
}

function updateList(response) {
    
    var leaderboard_div = document.getElementById("orderlists");

    while (leaderboard_div.hasChildNodes()) {
        leaderboard_div.removeChild(leaderboard_div.firstChild);
    }

    for (var i = 0; i < response.length; i++) {
       var ordernumber = response[i]["fields"]["ordernumber"];
       console.log(typeof ordernumber)
       var quantity = response[i]["fields"]["quantity"];
       var date = response[i]["fields"]["timestamp"]
       $("#orderlists").append(`
       <ul class="collapsible" data-collapsible="accordion">

        <li>
          <div class="collapsible-header">
              <ul>
              <li><a href="{% url 'myOrder' ${ordernumber} %}"><span>order number ${ordernumber} </span></a></li>
              <li>Order Details:</li>
              <li>Quantity: ${quantity}</li>
              <li><span>Order date: ${date} </span></li>
              <li>
              <button id="check" class="btn btn-sm btn-primary">Check</button>
              </li>
              </ul>
          </div>
        </li>

      </ul> `)
    }
}

function list(id){
    console.log('hahaha')
}

// var href = window.location.href
// id = href.slice(-1);

// window.onload = function(){
//    getList(id); 
// }
      
// window.setInterval( function(){
//    getList(id)}
//     , 5000);

