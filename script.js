let score = 0;
let current = 0;
const questions = Array.from({ length: 30 }, (_, i) => `คำถามข้อที่ ${i + 1}`);

function loginWithFacebook() {
  document.getElementById('loginBox').style.display = 'none';
  document.getElementById('quizBox').style.display = 'block';
}

function loginWithLine() {
  document.getElementById('loginBox').style.display = 'none';
  document.getElementById('quizBox').style.display = 'block';
}

function setCloudName(name) {
  document.getElementById('cloudName').textContent = name;
}

function showQuestion() {
  if (current >= questions.length) return showResult();
  document.getElementById('questionBox').innerHTML = `
    <p>${questions[current]}</p>
    <button onclick="answer(1)">ตอบแบบที่ 1</button>
    <button onclick="answer(2)">ตอบแบบที่ 2</button>
  `;
}

function answer(val) {
  score += val;
  current++;
  paintCloud();
  showQuestion();
}

function paintCloud() {
  const cloud = document.getElementById('cloudImage');
  cloud.style.filter = `grayscale(${Math.min(score, 30) / 30})`;
}

function showResult() {
  let color = 'gray';
  if (score <= 5) color = 'gray';
  else if (score <= 10) color = 'orange';
  else if (score <= 15) color = 'yellow';
  else if (score <= 20) color = 'green';
  else if (score <= 25) color = 'blue';
  else color = 'white';

  document.getElementById('cloudImage').src = `public/cloud-${color}.png`;
  document.getElementById('questionBox').innerHTML = `<h4>เมฆของคุณคือสี ${color}</h4>`;
}

showQuestion();
