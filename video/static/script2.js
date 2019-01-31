jQuery("document").ready(function () {
    jQuery(".likecom").on('click', function ()
    {
        var comm_id = jQuery(this).attr('id');
        jQuery.ajax
        ({
            type:"GET",
            url:"/video/addlikecom/",
            data:{"coment_id": comm_id},
            datatype:"text",
            catch:false,
            success:function (data)
            {
                jQuery("#" + comm_id + "comlikes").html(data);
            }
        })
    });
},
);