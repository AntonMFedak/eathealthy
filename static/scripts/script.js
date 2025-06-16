document.addEventListener("DOMContentLoaded", () => {
  const recipeBtn = document.getElementById('recipe-btn');
  const calorieBtn = document.getElementById('calorie-btn');

  // Get the last active button from localStorage
  const activeButton = localStorage.getItem('activeSearchButton');

  // Set the active button on page load
  if (activeButton == 'recipe') {
    calorieBtn.classList.remove('active');
    recipeBtn.classList.add('active');
  } else {
    // Default to calorie if no preference is set
    recipeBtn.classList.remove('active');
    calorieBtn.classList.add('active');
  }
});

function setActive(button) {
  const recipeBtn = document.getElementById('recipe-btn');
  const calorieBtn = document.getElementById('calorie-btn');

  // Remove active class from both
  recipeBtn.classList.remove('active');
  calorieBtn.classList.remove('active');

  // Add active class and save to localStorage
  if (button == 'recipe') {
    recipeBtn.classList.add('active');
    localStorage.setItem('activeSearchButton', 'recipe');
    //window.location.href = '/recipes';
  } else if (button == 'calorie') {
    calorieBtn.classList.add('active');
    localStorage.setItem('activeSearchButton', 'calorie');
    //window.location.href = '/calories';
  }
}