//alert("HAHA");
$(document).ready(function(){
    //alert("INIT");
    $("input").focus(function(){
	    //alert("TESTE")
        console.log($(this).closest("label").text());
    });
});
