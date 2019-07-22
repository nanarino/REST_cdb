//请在layout中紧跟jq引入

//获取GET请求参数
function getGET(key){
    var reg = new RegExp("(^|&)" + key + "=([^&]*)(&|$)","i")
    return location.search.substr(1).match(reg)
}//null or Array[2]

//弹窗
function rewardsLog(h3,h4){
    $(".rewards-popover h3").text(h3)
    $(".rewards-popover h4").html(h4)
}
function rewardsON(){
    rewardsLog("操作失败","可能是网络原因")
    $(".rewards-popover-mask").css("display","block").on('click', function(){
        $(this).css("display","none");
    })
    $(".rewards-popover").css("display","block")
}
//重定向
function countDown(secs, surl) {
	var $jumpTo = $(".rewards-popover h4 span");
	$jumpTo.html(secs)
	if(--secs > 0) {
		setTimeout("countDown(" + secs + ",'" + surl + "')", 1000);
	} else {
		location.href = surl;
	}
}//countDown(3, '/index');



