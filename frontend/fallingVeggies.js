const container = document.getElementById('falling-veggies');

const veggieEmojis = [
  '🥕', '🍅', '🌽', '🍆', '🥒', '🍄', '🌶️', '🥦', '🧄', '🧅',
  '🍋', '🍏', '🍎', '🍐', '🍇', '🍉', '🍌', '🥭', '🍓', '🥝'
];

const veggieCount = 30;

function random(min, max) {
  return Math.random() * (max - min) + min;
}

function createVeggie() {
  const span = document.createElement('span');
  span.classList.add('veggie');
  span.textContent = veggieEmojis[Math.floor(Math.random() * veggieEmojis.length)];
  span.style.left = random(0, 100) + 'vw';
  span.style.fontSize = random(16, 36) + 'px';
  span.style.animationDuration = random(8, 15) + 's';
  span.style.animationDelay = random(0, 15) + 's';
  span.style.opacity = 0.4 + Math.random() * 0.3;
  container.appendChild(span);
}

for (let i = 0; i < veggieCount; i++) {
  createVeggie();
}
