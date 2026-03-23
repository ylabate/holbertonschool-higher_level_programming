fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    return response.json();
  })
  .then(response => {
    const films = response.results;
    for (let i = 0; i < films.length; i++) {
      const li = document.createElement('li');
      li.textContent = films[i].title;
      document
        .querySelector('ul#list_movies')
        .append(li);
    }
  });
