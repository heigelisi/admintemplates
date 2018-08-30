$("a[lay-event='del']").on('click',function () {
    var mythis = this;
   layer.confirm('真的删除吗？', function(index){
        $(mythis).parent().parent().parent().remove();
        layer.close(index);
        //向服务端发送删除指令
      });

 
})

$('td>i.layui-icon').on('click',function(){
 var class_ = $(this).attr('class');
 if(class_.indexOf('layui-icon-ok') != -1){
    $(this).removeClass('layui-icon-ok').addClass('layui-icon-close').css('color','#f00');
 }else{
  $(this).removeClass('layui-icon-close').addClass('layui-icon-ok').css('color','#009688');
 }
 
})