#### 👉 파싱(parsing)
 파싱이란 프로그래밍 언어의 문법에 맞게 작성된 문서를 읽어와 실행하기 위해 토큰으로 분해하고 토큰의 문법적 의미와 구조를 반영해 트리구조의 자료구조(파스트리)를 생성하는 과정을 말한다. 

 <br>

 #### 👉 렌더링 (rendering)
 렌더링은 html,css,js로 작성된 문서를 파싱하여 브라우저에 시각적으로 출력하는 것을 말한다.    
 ```렌더링 엔진```    
 렌더링 엔진은 요청받은 내용을 브라우저 화면에 표시해주는 역할을 한다. 이때 각 브라우저마다 가지고 있는 렌더링 엔진이 달라 모든 브라우저 화면에 동일하게 그려지지 않고 엔진마다 읽을 수 있는 코드의 버전도 다르기 때문에 __크로스브라우징__ 이슈가 발생하기도 한다.  

 ```대표적 브라우저```   
 - 크롬 : 웹킷사용하다 fork하여 블링크 엔진 자체적으로 구현해 사용   
 - 사파리 : 웹킷   
 - 파이어폭스 : 게코   



 <br>  

 #### 👉 브라우저
 ```브라우저 역할```   
 - 서버에 리소스를 요청한다(request)   
 - 요청 받은 리소스를 가지고 화면을 보여준다(reponse)      

```브라우저 구성요소```   


<br>

 #### 👉 렌더링 과정
 
 - 클라이언트가 주소창에 주소를 입력   
 - DNS의 역할로 인해 해당 ip주소를 알아낸뒤 이와 연결된 서버로 이동   
 - 서버에서 HTML파일을 클라이언트로 랜선을 통해 전송    
 - 브라우저가 이해할 수 있게 HTML 파일을 파싱하여 DOM Tree를 생성   
 - 

<br>

#### 👉 DOM
  
렌더링 엔진은 HTML 문서를 파싱하여 브라우저가 이해할 수 이는 자료구조인 DOM을 생성한다. DOM은 프로퍼티와 메서드를 제공하는 트리 자료구조이다    

```HTML 요소```   
HTML요소는 HTML문서를 구성하는 개별적인 요소를 의미한다. 
class="greeting": 어트리뷰트, class:어트리뷰트 이름, "greeting":어트리뷰트 값
```html
<div class="greeting">HELLO</div>
```

```요소노드객체```   
HTML요소가 파싱되어 DOM을 구성하는 요소노드 객체로 변환된다   

```HTML문서를 렌더링엔진이 파싱하여 DOM생성```   

```html
<html>
    <head>
    </head>
    <body>
        <ul>
            <li>Apple</li>
            <li>Banana</li>
            <li>Orange</li>
        </ul>
    </body>
</html>
```
```DOM생성```   

<br>

#### 👉 노드탐색


```자식 노드 탐색```   

- Node.prototype.childNodes : 자식 노드 모두 탐색하여 요소노드뿐만 아니라 텍스트 노드도 포함된다   

- Element.prototype.children : 자식 노드 중에서 요소 노드만 탐색하여 반환한다   

- Node.prototype.firstChild : 첫번째 자식 노드를 반환한디. 반환한 노드는 텍스트 노드이거나 요소노드이다(lastChild 마지막 자식 노드 반환)       

- Node.prototype.firstElementChild : 첫번째 자식 노드를 반환한다. 요소 노드만을 반환한다(lastElementChild 마지막 자식 노드 반환)            

```html
<body>
    <ul id="fruits">
        <li class="apple">Apple</li>
        <li class="banana">Banana</li>
        <li class="orange">Orange</li>
      </ul>    
</body>
<script>
    const fruits = document.getElementById('fruits');
    const apple = document.querySelector('.apple');
    console.log(fruits.childNodes); //NodeList(7) [text, li.apple, text, li.banana, text, li.orange, text]
    console.log(fruits.children); //[li.apple, li.banana, li.orange]
    console.log(fruits.firstChild); //#text
    console.log(fruits.firstElementChild); //<li class="apple">..</li>
    console.log(fruits.lastChild); //#text
    console.log(fruits.lastElementChild); //<li class="orange">..</li>
</script>
```

```부모 노드 탐색``` 

```html
<script>
    console.log(apple.parentNode); //<ul id="fruits">.</ul>
</script>
```

```형제 노드 탐색``` 

```html

<script>
    console.log(apple.nextSibling); //#text
    console.log(apple.nextElementSibling); //<ul class="banana">..</ul>
</script>
```

<br>

#### 👉 요소 노드의 텍스트 조작

```nodeValue``` 

nodeValue는 텍스트노드가 아닌 노드 , 즉 문서 노드나 요소 노드의 nodeValue 프로퍼티를 참조하면 null을 반환한다   
```html
<body>
    <ul id="fruits">
        <li class="apple">Apple</li>
        <li class="banana">Banana</li>
        <li class="orange">Orange</li>
      </ul>    
    <div id="foo">Hello</div>
</body>

<script>
    const apple = document.querySelector('.apple');
    const appleTextNode = apple.firstChild; 
    console.log(apple.nodeVallue); // 요소노드의 nodeValue 프로퍼티를 참조 null
    console.log(appleTextNode.nodeValue); //텍스트노드의 nodeValue프로퍼티를 참조 apple
    appleTextNode.nodeValue='i dont like apple';
    console.log(appleTextNode.nodeValue); // i dont like apple로 변경
</script>
```

```textContent```    

요소 노드의 textContent 프로퍼티를 참조하면 요소 노드의 콘텐츠 영역내의 텍스트를 모두 반환한다. 요소 노드의 childNode 프로퍼티가 반환한 모든 노드들의 텍스트를 반환한다 
```html
<body>
    <ul id="fruits">
        <li class="apple">Apple</li>
        <li class="banana">Banana</li>
        <li class="orange">Orange</li>
      </ul>    
</body>

<script>
    const fruits = document.querySelector('#fruits');
    const apple = document.querySelector('.apple');
    const appleTextNode = apple.firstChild; 
    console.log(appleTextNode.nodeValue); //Apple
    console.log(apple.nodeValue); //null
    console.log(apple.textContent); //Apple
    console.log(fruits.nodeValue); //null
    console.log(fruits.textContent); //Apple Banana Orange
</script>
```

<br>

#### 👉 DOM 조작

```innerHTML```   
요소 노드의 innerHTML 프로퍼티를 참조하면 요소 노드의 콘텐츠영역 내에 포함된 모든 마크업을 문자열로 반환한다. textCont 프로퍼티는 html 마크업을 제외한 텍스트만 반환하지만 innerHTML 프로퍼티는 html마크업이 포함된 문자열을 그대로 반환한다

```html
<body>
    <ul id="fruits">
        <li class="apple">Apple</li>
        <li class="banana">Banana</li>
        <li class="orange">Orange</li>
      </ul>    
</body>
<script>
    console.log(document.querySelector('#fruits').innerHTML)
    document.querySelector('#fruits').innerHTML='<li class="grape">Grape</li>'; //fruits안의 html 마크업이 파싱되어 자식 노드로 dom에 반영된다
</script>
```
하지만 사용자로부터 입력 받은 데이터를 그대로 innerHTML 프로퍼티에 할당하는 것은 __크로스 스크립팅 공격__ 에 취약하므로 위험하다. HTML 마크업내에 JS 악성 코드가 포함되어 있다면 파싱 과정에서 그대로 실행될 가능성이 있기 때문이다     

innerHTML 프로퍼티의 또다른 단점으로는 기존에 있는 모든 마크업을 지우고 할당한 HTML 마크업만을 파싱하여 DOM을 변경한다는 것이다     

아래와 같이 +=로 grape를 fruits의 자식요소로 추가하면 Grape가 추가되어 화면에는 모든 과일이 그대로 출력되지만 실제로는 fruits 요소의 모든 자식 노드를 제거하고 다시 새롭게 하나하나 추가하여 실행된 것이다
```HTML
document.querySelector('#fruits').innerHTML+='<li class="grape">Grape</li>'; 
```

innerHTML 프로퍼티는 요소 삽입 위치를 지정할 수 없다는 단점도 있다   

```복수의 노드 생성과 추가```    
여러개의 요소노드를 생성하여 DOM에 추가할 수 있다    

ul안에 js에서 받아온 데이터를 li안에 넣어 화면에 출력한다(forEach, createElement, createTextNode, appendChild이용)
```HTML
<body>
    <ul id="fruits">
    </ul>    
</body>
<script>
const todos = [
  { id: 3, content: 'HTML', completed: false },
  { id: 2, content: 'CSS', completed: true },
  { id: 1, content: 'Javascript', completed: false }
];

const fruits = document.querySelector('#fruits');
['Apple','Banana','Orange'].forEach(text => {
    const li = document.createElement('li');
    const textNode = document.createTextNode(text);
    li.appendChild(textNode);
    fruits.appendChild(li);
});
</script>
```

<br>

#### 👉 스타일
style프로퍼티를 이용해 마크업한 html의 스타일을 변경할 수 있다. 
css프로퍼티는 케밥케이스(background-color)를 따르고 js에서는 카멜케이스를 따르기 때문에 backgroundColor식으로 작성해주어야 한다 
```text
hi.style.backgroundColor = 'yellow'; 
hi.style['background-color'] = 'yellow'; // 위의 카멜케이스 방식이 더 효율적이다 
```

```html
<body> 

<div class="hi">hi</div>
</body>
<script>
    const hi = document.querySelector('.hi');
    hi.style.color = 'red'; // 폰트color Red로 변경
    hi.style.backgroundColor='yellow'; //배경 color yellow 변경
    
</script>
```
단위 지정이 필요한 css값을 js에서 제어하기 위해서는 반드시 단위를 지정해야 한다. px,em.%등의 크기단위가 필요하다
```text
hi.style.width = '100px';
```

<br>

#### 👉 클래스 조작

```className```   
className은 해당 class의 네임을 가져올 수 있다. 해당 Class의 네임도 replace를 통해 변경이 가능하다. 하지만 해당 프로퍼티는 문자열을 반환하기 때문에 공백으로 구분된 여러개의 클래스를 반환하는 경우 다루기 불편한 단점을 가지고 있다

```classList```   
classList 프로퍼티는 class네임을 가져올수 있는데 여러 메서드를 사용해 제어가 가능하다

- add : class를 추가한다.   
```javascript
div.classList.add('foo')  // class = "box foo"
div.classList.add('bar, barrr')  // class = "box foo, bar, barrr"
```
- remove : class를 삭제한다
```javascript
div.classList.remove('foo')  // class = "box"
div.classList.add('barrr')  // class = "box bar"
```

- toggle : class가 존재하면 제거하고 존재하지 않으면 추가한다
```javascript
div.classList.toggle('foo')  // class = "box foo"
div.classList.toggle('barrr')  // class = "box"
```

<br>

#### 👉 이벤트 핸들러
브라우저는 클릭,키보드 입력, 마우스 이동등이 일어나면 이를 감지하여 이벤트를 발생시킨다. 해당 이벤트가 발생했을때 호출된 함수를 브라우저에게 알려 호출을 해준다. 이때 호출될 함수를 ```이벤트 핸들러```라 한다. 
```html
<body> 
<button class="clickBtn">click me</button>
</body>
<script>
    const clickBtn = document.querySelector('.clickBtn');

    //사용자가 버튼을 클릭하면 함수를 호출하도록 요청
    clickBtn.onclick = () => {
        alert('button click');
    }
</script>
```

```addEventListener```   
해당 메서드가 도입되면서 이를 사용하여 이벤트 핸들러를 등록할 수 있다. addEventListener 메서드의 첫번째 매개변수에는 이벤트의 종류를 나타내는 문자열인 이벤트 타입을 전달한다. 이때 이벤트 핸들러 프로퍼티 방식과는 달리 on접두사를 붙이지 않는다.   

이벤트 핸들러 프로퍼티 방식은 이벤트 핸들러 프로퍼티에 이벤트 핸들러를 바인딩하지만 addEventListener메서드는 이벤트 핸들러를 인수로 전달한다. 
```html
<body> 
<button class="clickBtn">click me</button>
</body>
<script>
    const clickBtn = document.querySelector('.clickBtn');

    clickBtn.addEventListener('click', function(){
        alert('button click');
    });

// 동일한 동작을 한다
    // const handleClick = () => console.log('btn click');
    // handleClick.addEventListener('click',handleClick);
</script>
```

<br>

#### 👉 DOMContentLoaded [실습]
html과 script가 로드되면 발생하는 이벤트로 브라우저가 작동하면 실행된다.
```javascript
// getTodos 함수가 실행된다 
document.addEventListener('DOMContentLoaded', getTodos);
```