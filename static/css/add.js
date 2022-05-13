let calendar = document.getElementById('calendar'),
    year = calendar.querySelector('.year input'),
    color = calendar.querySelector('.color input')

color.addEventListener('change', function() {
    console.log(this.value);
  });

year.addEventListener('change', function() {
    console.log(this.value);
});