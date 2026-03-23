document.getElementById('add_item').addEventListener('click', () => {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  document.querySelector('ul.my_list').append(newLi);
  console.log('ok');
});
