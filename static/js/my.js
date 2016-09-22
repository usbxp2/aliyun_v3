$(function() {
    //点击按钮，弹出模态框
    //如果用$('#comment')是不能获取到所有id为comment的元素，所以得这样写，或者用class也行
    $('[id="comment"]').each(function(){
        $(this).click(function(){
            //获取子元素span的值
            var text = $(this).children('span').text();
            //如果值不等于"添加",将值写入textarea
            if(text != "添加") {
                $("textarea").html(text);
            }else{
                //如果值等于“添加”，显示提示信息，如果获取鼠标焦点，则清空提示信息
                $("textarea").html("10个字简单描述一下").focus(function(){
                    $(this).html("");
                });
            }
            //获取该条业务的在数据库中的ID值，由month页面获取
            var bus_id = $(this).attr('bus_id');
            //当前url， 发给django后台用于页面跳转
            var url = window.location.href
            console.log('url:'+url);
            //设置模态框两个隐藏input的value值
            $('#motai_bus_id').val(bus_id);
            $("#motai_url").val(url);
            //获取模态框
            var mt_html = $(".motai");
            //layer模态框弹出
            layer.open({
                      type: 1,
                      title: '添加备注',
                      skin: 'layui-layer-rim', //加上边框
                      area: ['350px', '300px'], //宽高
                      content: mt_html,
                  });
        });
    }); //弹出模态框结束
    
    
});