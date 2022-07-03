


//  객체 = 오브젝트
// 1 오브 젝트는 {키:"밸류"}의 집합체이다.

const name="park";
const age =4;
print(name,age);

function print(name,age){
    console.log(name);
    console.log(age);
}

// 위 의 방법 대로 하면 넘 길고 복잡해져서 아래와 같이 오브젝트 형식으로작성
const park ={name:"park", age:5};
function print2(person){
    console.log(person.name);
    console.log(person.age);
}
print2(park);

// 이래와 같이 오브젝트 선언후에 개인적으로 추가해도돼며
park.hobby="program";       
console.log(park.hobby);

// 아래와 같이 개인적으로 삭제도 가능함.
delete park.hobby;
console.log(park.hobby);


// 2 컴퓨티 속성.
console.log(park.name);
// 과 같이 속성 확인도 가능하지만 아래와 같이 키값[스트링 타입]으로 밸루 확인가능함.
console.log(park['name']);



// 3. 속성 값 숏핸드.
const person1={name:"bob",age:3};
const person2={name:"bosteveb",age:13};
const person3={name:"dave",age:32};
// const person4=MakePerson("park",43);


// person4를 만들때 동일하게 만들수 있지만 동일 코드가 많아지므로.아래와깉이 함수정의
// function makePerson(name, age){
//     return{
//         name,
//         age,
//     };
// }
// 위와 같이 클래스가 없을 경우에는 함수를 클래스처럼 사용했지만 지금은
// 시작대문자로 만들며 리턴시 this 적용.

function MakePerson(name, age){
    this.name=name;
    this.age=age;
}

// 아래와 같이 클래스 객체 생성하는듯이 만들어줘서 사용가능.
const person4 = new MakePerson("pakrka", 73);
console.log(person4)


// 5 속성 존재 치크 유무. key in  obj
// 아래와 같은경우 t,t,f,undefided.
console.log('name' in park);
console.log('age' in park);
console.log('random' in park);
console.log(park.random);



// 6 for..in, for...of
// 파이썬과 비슷한 for문으로
// park에 있는 데이터가 반복을 돌며 key에 차곡차곡쌇임.
for(key in park){
    console.log(key);
}

// 원래 for문으로 작성하면 다음과 같은대.
const array=[1,2,3,4];
for (let i = 0; i < array.length; i++) {
    console.log(i);    
}

// 위의 for문을 조금더 효울적으로 해당배열을 처음부터끝까지 해당변수에 넣어주는구문.
for(value of array){
    console.log(value);    
}


//  7. cloning
const user= {name:"park", age:"12"};
const user2=user;
// use를 user2의 주소를 면향하게 하
user2.name="jjang";
// user2의 이름을 바꾸면 user의 이름도 동일하게 변경됨.
console.log(user.name);   
// jjang 출력
console.log(user2.name);   
// jjang 출력


// 예전방법 아래와 같이 for 문을 돌며, 해당 변수에 값을 넣어주는식.
const user3={};
for(key in user){
    user3[key]= user[key];
}
console.log(user3);   

// 현제방법
const user4={};
Object.assign(user4,user);
console.log(user4);