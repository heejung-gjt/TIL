let todos = [];
const $todos = document.querySelector('.todos');

// 왜 id,content,completed에 ({})를 작성해주었는지 ?
const render = () => {
  $todos.innerHTML = todos.map(({id,content,completed}) => {
    return `<li id=${id}>
    <label><input type="checkbox"${completed ? 'checked' : ''}>${content}</label>
  </li>`
  }).join('');
}

const getTodos = () => {
  todos = [
    { id: 3, content: 'HTML', completed: false },
    { id: 2, content: 'CSS', completed: true },
    { id: 1, content: 'Javascript', completed: false }
  ];  
  render();
}

document.addEventListener('DOMContentLoaded', getTodos);
