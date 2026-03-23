fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    return response.json();
  })
  .then(data => {
    console.log(data);
    document.getElementById('character').append(data.name);
  });
