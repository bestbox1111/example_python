

'user strick';

let name="park";
console.log(name)

name="jjang";
console.log(name)

// 블록안의 변수를 밖에서 불러낼려면 사용이 안됨.
{
    let name2="123";
    console.log(name2)
    
    name2="456";
    console.log(name2)
}

// 블록안에 변수 사용할라면 오류가남..
// console.log(name2)      

// 위와 같은 경우   아래와 같이 {} 밖에서 정의한 변수를 사용

let globalname ="gobal name";
{
    let name2="123";
    console.log(name2)
    
    name2="456";
    console.log(name2)
    console.log(globalname)
}
console.log(globalname)


// 자바 스크립트의 미친 짓거리 - 내가 싫어하는 이유...
// 변수 선언전에 값을 먼저 넣고 선언을 나중에 해도됨..ㅆㅂ것..
// var로는 그래서 선언하면 그지됨..
age =30;
var age;
console.log(age)


// let으로 선언하면 그나마 절차 지키는 듯.. 선언후 값안넣으면 오류메시지 띄움.
// n_age=50;
// let n_age;
// console.log(n_age)



// var 를 쓰면 안되는 이유....2
{
p_age=40;
var p_age;
}
console.log(p_age)
// 블럭 변수를 개 무시한다.... 나중에 오류나 여러가지 상황에 치명적일듯.



// const 는 변수를 선언하면 수정이 안되는 타입.
// const nn =7;
// console.log(nn)
// nn=9;
// console.log(nn)
// 다른 값으러 변경 하려하면 오류뜸.



// 변수 종류 Number, String, boolean등
// ` 어쩌구 저쩌구 ${변수}` 로 변수입력 대처가능함.
const hellow ="park";
console.log(`hi jjang ${hellow}`)   


// null 과  undefined의 차이 ???
// null  은 값이 비어졌다고 값을 주긴준거구.
let not =null;
console.log(not)

// 언디파인드는 선언만 되었고 값이 할당 안된거임....
let y ;
console.log(y)


// symbol   자료구조에서  고유식별자  구분시 필요
const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
console.log(symbol1=== symbol2)   
// false로 나옴....
// 아래와 같이 하면 확인안되고
console.log(symbol1)
// 아래와 같이 해당함수를 같이 사용해여함.des...
console.log(symbol1.description)




// 변수에 스트링 과 넘버를 합하거나 나누기의 예시
let text ="hellow";
console.log(text.charAt(0))
console.log(typeof(text))

text=9;
console.log(text)
text="9"+8;
console.log(text)


