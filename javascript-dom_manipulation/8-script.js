document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => {
      return response.json();
    })
    .then(response => {
      document
        .getElementById('hello')
        .append(response.hello);
    });
});
