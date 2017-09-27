
var request=require("request");
var cheerio =require("cheerio");
var url ="http://www.watthakhanun.com/webboard/showthread.php?t=5235&page=2";
// var url ="http://www.thaiseoboard.com/index.php?action=register"
request(url,function(err,resp,body){
	var $=cheerio.load(body,{decodeEntities:false});
	// var com=$('.windowbg').text();
	// com = com.replace(/\s+/g, '') //Delete spacebar
	// var a = com.localeCompare("ขออภัยปิดรับการลงทะเบียนชั่วคราว");
	// if(!a)
	// 	console.log("Find");
	// else
	// 	console.log("Not Find");

	// var com=$('.alt2','#post_thanks_box_174877').text();
	// console.log(com.decode);
	console.log($('.alt1','#td_post_174868').html())
	// console.log(body);

})
// td_post_174868  alt1
