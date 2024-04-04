$(document).ready(function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, textStatus, jqXHR) {
    const name = data.hello;
    $('#hello').text(name);
  }
  );
});
