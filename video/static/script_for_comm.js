jQuery("document").ready(function () {

    jQuery(".btn-success").on('click', function ()
    {
        console.log("hello")
        var text = jQuery('textarea').val();
        var idvidos = jQuery('textarea').attr('id');
        console.log(text);
        console.log(idvidos);
        jQuery.ajax({
            type:"GET",
            url:"/video/addcommajax/",
            data:{"text": text, "idvideo":idvidos},
            contentType: "application/json; charset=utf-8",
            datatype:"json",
            catch:false,
            success: function(data){
                console.log("hellll")
                console.log(data['user']);
                console.log(data['date']);
            },
        })
    });
},
);



