jQuery("document").ready(function () {

    jQuery(".videolike").on('click', function ()
    {
        var video_id = jQuery(this).attr('id');
        jQuery.ajax
        ({
            type:"GET",
            url:"/video/addlike/",
            data:{"video_id": video_id},
            datatype:"text",
            catch:false,
            success:function (data)
            {
                jQuery("#" + video_id + "videolikes").html(data);
            }
        })
    });
},
);



