


// 펑션 ==  함수....

function print(){
    console.log("hellow")
}
print()
// 위 함수는 매개변수 없어서..같은 문구만 출력해서  의미없음.

function print2(message){
    console.log(message)
}
print2("kakakakpoarkr")
// 위 함수는 ㅈㅅ 같은 자바스트립트이고...타입필요없는 언어다보니...

// function print2(message:string){
//     console.log(message)
// }
// print2("kakakakpoarkr")
// 위 처럼 들어가는 매개변수 타입을 옆에 적어줘야 하는 타입스크립트도있고.


// function print2(message:string):number{
//     console.log(message)
//     return message;
// }
// print2("1234")
// 매개변수가 스트링이지만 리턴타입이 넘버를 원한다고 지정해야한다...타입스크립트




// 메개변수가 몇개를 넣을지 모를때 ...args를 사용하면 무제한 인자제공.
function printall(...args){
    // for (let i = 0; i < args.length; i++) {
    //     console.log(args[i])
    // }
// 위의 for문처럼 사용해도되지만 조금더 간단하게하려면 아래와같이.
    for(const arg of args){
        console.log(args)
    }
}
printall("akrka",1244,"gmaklmkla","gmklamklopa.a")




//  지역 변수 및 전역 변수 개념.
let globalm="globalm"
function msg(){
    let message ="hellow";
    console.log(message);
    console.log(globalm);
}
msg()
// 함수안에 있는 지역 변수인 message를 읽어내려 하면 오류가남.... 남의집 여자를 불러내면 싸움남.ㅡ
// console.log(message)



//  익명함수 및 함수를 변수에 저장
const name = function(){
    console.log("name")
}
name()
const namename= name;
namename();




// 에로우 함수 =  화살표로 함수정의
const simple =()=>console.log("simgple")    
const add =(a,b)=>a+b;
// add 함수를 원래 함수로 만들게된다면 아래와 같지만.
//  const add = function(a,b){
//     return a+b;
//  }





// 함수를 선언함과 동시에 실행하는법
(function quick(){
    console.log("fast");
})();