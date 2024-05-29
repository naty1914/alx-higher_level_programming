const $ = window.$;
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
      var movies = data.results;
      var listElement = $('#list_movies');
      
      $.each(movies, function(index, movie) {
        $('<li>').text(movie.title).appendTo(listElement);
      });
    });