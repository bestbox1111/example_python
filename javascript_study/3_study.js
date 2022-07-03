


// 연산 부분.


const value1= true;
const value2=4<2;

console.log(value1 || value2 || check())
//  or 연산에서 중요한 부분.... 세개의 조건중에서 맨앞에서 이미 트루이면 뒤에껀 아예코드안읽음.

function check(){
    for (let i = 0; i <10; i++) {
        console.log(i) 
    }
    return true;
}

//  레퍼런스를 담고있으므로.
const park1={name:'park1'};
const park2={name:'park2'};
const park3 = park1;

console.log(park1==park2)
console.log(park1===park2)
console.log(park1===park3)
// false,flase,true출력임.


// 0~10까지 짝수만 출력
for (let i = 0; i < 10; i++) {
    if (i%2===0)
        console.log(i)
}

// 0~10까지중 8 만나면 브렉
for (let i = 0; i < 10; i++) {
    if (i==8)
        break;
        console.log(i)
}