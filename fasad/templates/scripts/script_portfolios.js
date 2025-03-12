

function toggleGallery(portfolioId) {
        const gallery = document.getElementById(`gallery-${portfolioId}`);
        const toggleText = document.getElementById(`toggle-text-${portfolioId}`);
        const toggleBtn = document.getElementById(`toggle-btn-${portfolioId}`);

        gallery.classList.toggle("open"); // Переключаем класс для открытия/закрытия

        if (gallery.classList.contains("open")) {
            toggleText.textContent = "Закрыть галерею"; // Меняем текст на "Закрыть галерею"
            toggleBtn.classList.add("animate"); // Добавляем анимацию к стрелке
        } else {
            toggleText.textContent = "Открыть галерею"; // Меняем текст на "Открыть галерею"
            toggleBtn.classList.remove("animate"); // Убираем анимацию
        }
    }

    function openFullscreen(src) {
        const fullscreen = document.getElementById('fullscreen');
        const fullscreenImage = document.getElementById('fullscreenImage');
        fullscreenImage.src = src;
        fullscreen.style.display = "flex"; // Показываем увеличенное изображение
    }

    function closeFullscreen() {
        const fullscreen = document.getElementById('fullscreen');
        fullscreen.style.display = "none"; // Скрываем увеличенное изображение
        const fullscreenImage = document.getElementById('fullscreenImage');
        fullscreenImage.src = ''; // Очищаем src, чтобы предотвратить загрузку изображения при закрытии
    }


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




