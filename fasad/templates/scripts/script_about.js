
const slides = document.querySelectorAll('.slide');
let currentSlide = 0;

function showSlide(index) {
    slides.forEach((slide, idx) => {
        slide.classList.remove('active'); // Убираем активный класс у всех слайдов
        if (idx === index) {
            slide.classList.add('active'); // Добавляем активный класс к текущему слайду
        }
    });
}
function nextSlide() {
    console.log("Next slide triggered");
    currentSlide = (currentSlide + 1) % slides.length; // Переход к следующему слайду
    showSlide(currentSlide);
}

function prevSlide() {
    console.log("Previous slide triggered");
    currentSlide = (currentSlide - 1 + slides.length) % slides.length; // Переход к предыдущему слайду
    showSlide(currentSlide);
}
// Инициализация первого слайда
showSlide(currentSlide);
// Автоматическая смена слайдов каждые 9 секунд
setInterval(nextSlide, 9000);




const slider1 = document.querySelector('.slider1');
const slides1 = document.querySelectorAll('.slide1');

// Клонируем первые слайды, чтобы создать эффект бесконечной прокрутки
slides1.forEach(slide => {
    const clone1 = slide.cloneNode(true);
    slider1.appendChild(clone1);
});

// Устанавливаем ширину контейнера в два раза больше, чтобы учесть клонированные слайды
slider1.style.width = `${slides1.length * 240 * 2}px`;

// Функция для запуска анимации
function startSlider1() {
    slider1.style.animation = 'scroll 40s linear infinite';
}

startSlider1();

