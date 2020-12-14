$(document).ready(function() {
    var $randomQuote = $('#randomQuote');
    var root = "https://cors-anywhere.herokuapp.com/quotes.stormconsultancy.co.uk/quotes.json/";
  
    function loadQuote(json) {
      var quote = '<li data-id = "' + json.id + '"><p> <i class= "fa fa-quote-left fa-2x"></i>' + json.quote + '' + '</p><p>' + json.author + '</p>';
  
      var quoteButtons = '<button class = "btn btn-info tweetQuote"><i class = "fa fa-twitter">Tweet This!</i></button>' + '<button class = "btn btn-primary nextQuote">Next Quote</button></li>'
  
      $randomQuote.append(quote + quoteButtons);
    };
  
    $.getJSON(root, function(json) {
      var x = Math.floor(Math.random() * json.length);
      loadQuote(json[x]);
    });
  
    function newRandomQuote() {
      $.getJSON(root, function(json) {
        var x = Math.floor(Math.random() * json.length);
        loadQuote(json[x]);
      });
    };
  
    $randomQuote.delegate('.nextQuote', 'click', function() {
      var $li = $(this).closest('li');
      $li.fadeOut(1000, function() {
        $(this).remove();
        newRandomQuote();
      });
    });
  
    $randomQuote.delegate('.tweetQuote', 'click', function() {
      var twitter = "https://twitter.com/intent/tweet?text=";
      var $li = $(this).closest('li');
      var id = $li.attr('data-id');
      var link = "https://crossorigin.me/quotes.stormconsultancy.co.uk/quotes/";
      var itsJSON = ".json";
      var quoteLink = link + id + itsJSON;
      $.getJSON(quoteLink, function(json) {
        window.open(twitter + encodeURIComponent(json.quote + '\n' + json.author));
      });
    });
  });