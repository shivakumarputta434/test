function msg(){
alert("i am alert function")
}


function read(){

$.ajax({
    type:'GET',
    url:"http://localhost:8000/testapp/display-student/",
    success:function(data){

$.each(data.Studata, function(key,val) {

  var dummy="<tr><td>"+val.name+"</td><td>"+val.id+"</td><td>"+val.marks+"</td></tr>";

    $("#tbody").append(dummy);
    });

    },
    error:function(data){
alert("error");
    }

});

}

read();

