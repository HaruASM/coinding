var sv={}; //static page scope
sv.recieves = []; // for xhr post recieves

// mainprocess : onload -> getDatasFromDB -> setPage
;(function(window){
  'use strict';
  var document = window.document;


  window.onload = function(){
    //new Promise( function(res){ res();} ).then( getDatasFromDB).then( setUpPage );
    getDatasFromDB();

}

function getDatasFromDB(){  // ():arrary
  var lists = [];
  sv.lists= lists;

  sendData( parseRes );
  return lists;
}// getDatasFormDB


var inboxMessage = 0;
var inbox;
function checkInbox( elapse ){

  inboxMessage += elapse;

  if( inboxMessage != 0 ){
    inbox = document.getElementById('noti-inbox');
    inbox.className += "mdl-badge mdo-overlap";
    inbox.setAttribute("data-badge", inboxMessage);
  }

}

function setUpPage(lists){ // (array):

  checkInbox(0); // warm up

} // setUpPage


var apis = [];
apis[5] = function(){};

function parseRes(body){
  var body = JSON.parse(body);
  if(apis[body.code]) apis[body.code](body.data);

  setUpPage();
  checkInbox(parseInt(body.code));
}








function sendData(callback){
  var xhr = new XMLHttpRequest();

  //var url = "https://script.google.com/macros/s/AKfycbw3wfdeUGHsGMvQe8_eZBEdI2eigZNRK-XtFPmHSP14x-LrVpA/exec";
  //var url = "https://webhook.site/618994c0-4ad0-4409-b0fe-cfbddeb62930";
  var url = "http://220.81.12.20:5555/home";
//  var form_ = document.getintouchForm ;
  // var params =  "n="+ form_.field01.value +
  //               "&e="+ form_.field02.value +
  //               "&t="+ form_.field03.value +
  //               "&a=faq";

  // var tmp =  {n: form_.field01.value ,
  //               e: form_.field02.value ,
  //               //t : form_.git03.value ,
  //               t: CKEDITOR.instances.git03.getData(),
  //               a : "faq" };

  var tmp = {api:10, data:"hello"};

  var params = JSON.stringify(tmp) ;

  xhr.open("POST", url, true);
  xhr.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200)
         callback(this.responseText);
  };// onreadystatechange
  xhr.onerror = function(e){      console.log( 'error'); console.dir(e) ;  } // onerror
  if(!xhr){ console.log('nop'); return ; } //if
  //xhr.setRequestHeader('Content-Type', 'text/plain');
  //xhr.setRequestHeader('Access-Control-Allow-Origin' , '*');
  xhr.send(params);
}   // sendData


//function sendData(callback, param_ ){
// function sendData2( callback, param_ ){
//   var xhr = new XMLHttpRequest();
//   var url = "https://script.google.com/macros/s/AKfycbw3wfdeUGHsGMvQe8_eZBEdI2eigZNRK-XtFPmHSP14x-LrVpA/exec";
//   var tmp =  { id: param_, a : "not" };
//
//   var params = JSON.stringify(tmp) ;
//   xhr.open("POST", url, true);
//   xhr.onreadystatechange = function() {
//       if (this.readyState == 4 && this.status == 200) {
//          callback(this.responseText);
//       } // if
//
//   };// onreadystatechange
//   xhr.onerror = function(e){      console.dir( e);    } // onerror
//   if(!xhr){      console.log('nop');      return ;    } //if
//   xhr.setRequestHeader('Content-Type', 'text/plain');
//
//   xhr.send(params);
//}   // sendData

})(window); // index page end
