jQuery("document").ready(function () {

    jQuery(".videolike").on('click', function ()
    {
        var video_id = jQuery(this).attr('id');
        console.log(video_id);
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



