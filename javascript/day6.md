#### 👉 고차함수
자바스크립트의 함수는 함수를 값처럼 인수로 전달할 수 있고 반환할 수도 있다.    

```Array.prototype.map```    
map 메서드는 입력으로 들어온 배열을 인자로 받는 콜백함수를 호출함으로써 새로운 배열을 만들어낸다. 따라서 원본 배열은 변경되지 않는다. map메서드로 전해진 콜백함수는 item, index, array의 3가지 인수를 받는다.   

num이라는 배열객체를 map을 이용하여 콜백함수를 호출해 새로운 배열을 만드는데 이때 콜백함수에서 각 배열의 요소에 제곱을 한 값이 리턴되므로 num의 배열 요소 각각에 제곱된 새로운 배열이 mapNum에 저장된다 (고차함수:map, 콜백함수 item=>item**2)
```javascript
const num = [1,2,3,4,5];
const mapNum = num.map(item=>item**2);

console.log(num); //[ 1, 2, 3, 4, 5 ]
console.log(mapNum); //[ 1, 4, 9, 16, 25 ]
```

map메서드의 콜백함수는 map메서드를 호출한 배열의 요소값,인덱스값, 배열자체, 즉 this를 순차적으로 전달받을 수 있다.
```javascript
const num = [1,2,3];
num.map((item,index,arr)=>{
    console.log(`item ${item} index ${index} arr ${arr}`);
});

// 결과값
// item 1 index 0 arr 1,2,3
// item 2 index 1 arr 1,2,3
// item 3 index 2 arr 1,2,3
```

#### map에 대한 예시

__1. map과 화살표 함수를 사용하여 배열의 제곱값을 구한다__   
```javascript
const numbers = [1,2,3];
console.log(numbers.map(v=>v**2)); //[1,4,9]
```

__2. polyfill을 이용하여 map기능 구현하기__    

Q. polyfill(폴리필)이란 ?   
A. polyfill은 브라우저에서 지원하지 않는 코드를 사용가능한 코드로 바꾸어 작성한 기능을 의미한다.    


numbers라는 배열 객체를 myMap을 이용하여 콜백함수를 호출해 새로운 배열을 만드는데 이때 콜백함수를 인자로 받는 callback 타입이 function이 아니면 에러를 출력해준다. 만약 타입이 function인 경우 새로 만든 배열 res에 callback함수는 인수로 받을수 있는 3가지를 받아 push해준다. 이때 callback함수는 결국 첫번째 요소의값 만을 사용하여 제곱해주므로 리턴은 첫번째 요소의값이 제곱된 값이 리턴되고 해당 값들이 배열로 출력된다
```javascript
const numbers = [1,2,3];

Array.prototype.myMap = function(callback){
    if(typeof callback != 'function'){
        throw new TypeError(`${callback} is not a function`);
    }
    const res = [];
    
    for(let i =0; i<this.length; i++){
        res.push(callback(this[i],i,this));
    }
    return res;
};
console.log(numbers.myMap(v => v**2)); //[1,4,9]
```
