$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus, jqXHR) {
    for (const element of data.results) {
      $('#list_movies').append(`<li>${element.title}</li>`);
    }
  }
  );
});
