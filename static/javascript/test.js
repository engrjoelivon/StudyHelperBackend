$(document).ready(function(){
    $("#doc_title").click(function(){
        $("#titledef").show();



    });
    });

$(document).ready(function(){
    $("#Constructors").click(function(){
        $("#titledef").hide();
        $("#bodylist").show();

        var out = '<ul><li>get_whole_record(self):- \n from its base class and implements the body Using the Title class and the username set in the constructor to get whole record from the titles table  </li>\n\
<li>Item Two</li><li>Item Three</li></ul>';
    $('#bodylist').html(out);


    });
    });



 $(document).ready(function(){
    $("#fields").click(function(){
        $("#titledef").hide();
        $("#bodylist").show();
        var out = '<ul><li>Item four</li><li>Item Two</li><li>Item Three</li></ul>';
    $('#bodylist').html(out);

    });
    });



 $(document).ready(function(){

    $("#Methods").click(function(){
        $("#titledef").hide();
        $("#bodylist").show();
        var out = '<ul><li>Item 9ine</li><li>Item Two</li><li>Item Three</li></ul>';
    $('#bodylist').html(out);

    });
    });






