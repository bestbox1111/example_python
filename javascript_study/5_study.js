


// 1 클래스
'use strict';

class Person{
// constructor 생성자.
constructor(name, age){
    this.name=name;
    this.age=age;
}
// 함수
speak(){
    console.log(`${this.name}: hellow`)
}
}
// 객체 생성.
const park = new Person('park',42);
console.log(park.name, park.age)
park.speak()



// 2 게터 앤 세터
class User{
    constructor(firstName, lastName, age){
        this.firstName=firstName;
        this.lastName=lastName;
        this.age=age;
    }
    get age(){
        return this._age;
    }
    set age(vlaue){
        this._age=vlaue; 
    }
}
// 만약 나이에 -1이라는 데이터는 말이 안되기 때문에.이를 수정하기 위해 게터앤 세터.사용
const user1 = new User('park','hyung',42);
console.log(user1.age)



// 3 static
class Article{
    static publiser='dream';
    constructor(number){
        this.number=number;
    }

    static printpublisher(){
        console.log(Article.publiser);
    }
}

const article1=new Article(1);
// 객체를 이용하여 변수에 접근이원칙이지만 static이 붙은 변수는
console.log(article1.publiser) 
// 아래와 갵이 클래스자체를 통한 접근을 해야함.
console.log(Article.publiser)
// 클래스를 통한 함수사용도 동일.
Article.printpublisher();



// 4 상속. 도형을 예시로.
class Shape{
    constructor(width,height,color){
        this.width=width;
        this.height=height;
        this.color=color;
    }

    draw(){
        console.log(`drawing ${this.color} color of`);
    }

    getArea(){
        return this.width * this.height;
    }

}

// extends를 통한 상속.... 사각형일경우
class Rectangle extends Shape{}
const rectang = new Rectangle(20,20,"blue");
console.log(rectang.getArea());
rectang.draw();

// extends를 통한 상속.... 삼각형일 경우 너비는 위변*높이/2가 되어야함.
class Triangle extends Shape{

    draw(){
    // super는 상속을 통한매소드.
    super.draw();   
    console.log("트라이앵글의 오버라이딩된 메소드실행부분.")
    }

    getArea(){
        return (this.width * this.height)/2;
        // 위와 같이 해당 메소드를 따로 적용시킬수있음.. 오버라이딩이라고하는데... 같은 메소드인대 실행을 다르게 함...
    }
}
const tri = new Triangle(10,20,"black");
console.log(tri.getArea());
tri.draw();