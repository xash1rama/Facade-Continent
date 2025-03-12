
    // Обновляем отображение суммы
const totalSumElement = document.getElementById('totalSum');
const totalSumContainer = document.getElementById('totalSumContainer');

document.querySelectorAll('.add-volume').forEach(button => {
    button.addEventListener('click', function() {
        const volumeInput = this.nextElementSibling;
        const isVisible = volumeInput.style.display === 'inline-block';
        const input = volumeInput.querySelector('.volume');

        // Если поле ввода скрывается
        if (isVisible) {
            const volume = parseFloat(input.value) || 0;
            const price = parseFloat(this.dataset.price);
            const currentSum = parseFloat(totalSumElement.textContent) || 0;
            const newSum = currentSum - (volume * price); // Вычитаем значение
            totalSumElement.textContent = newSum.toFixed(2); // Обновляем общую сумму

            // Очищаем поле ввода
            input.value = '';
        } else {
            // Если поле ввода открывается, сбрасываем значение
            input.value = '';
            input.focus();
        }

        // Переключаем видимость поля ввода
        volumeInput.style.display = isVisible ? 'none' : 'inline-block';
        // Меняем текст кнопки
        this.textContent = isVisible ? '+' : '-';

        // Проверяем, нужно ли скрыть контейнер с общей суммой
        const totalSum = parseFloat(totalSumElement.textContent) || 0;
        totalSumContainer.classList.toggle('visible', totalSum > 0); // Показываем или скрываем контейнер
    });

    const input = button.nextElementSibling.querySelector('.volume');
    input.addEventListener('input', function() {
        // Вычисляем общую сумму
        const totalSum = Array.from(document.querySelectorAll('.volume-input')).reduce((sum, input) => {
            const volume = parseFloat(input.querySelector('.volume').value) || 0;
            const price = parseFloat(input.previousElementSibling.dataset.price);
            return sum + (volume * price);
        }, 0);

        totalSumElement.textContent = totalSum.toFixed(2); // Обновляем общую сумму

        // Показываем или скрываем окно в зависимости от суммы
        totalSumContainer.classList.toggle('visible', totalSum > 0); // Добавляем/убираем класс для анимации
    });
});



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

