document.addEventListener("DOMContentLoaded", function() {
            // Генерация уникального идентификатора пользователя
            let userId = localStorage.getItem("userId");
            if (!userId) {
                userId = 'user-' + Date.now(); // Создаем ID, если его нет
                localStorage.setItem("userId", userId);
            }

            // Отправка ID пользователя на бэкэнд
            fetch('/trackUser', {
                method: 'POST',
                body: JSON.stringify({ user_id: userId }),
                headers: {
                    'Content-Type': 'application/json',
                },
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Сеть ответила с ошибкой: ' + response.status);
                }
                return response.json();
            })
            .then(data => {
                console.log(data.message);
            })
            .catch(error => {
                console.error('Ошибка:', error);
            });
        });





function toggleAnswer(element) {
    const answer = element.nextElementSibling;
    const arrow = element.querySelector('.arrow1');

    if (answer.classList.contains('open')) {
        answer.classList.remove('open'); // Закрыть ответ
        arrow.style.transform = "rotate(0deg)"; // Вернуть стрелочку в исходное положение
    } else {
        answer.classList.add('open'); // Открыть ответ
        arrow.style.transform = "rotate(90deg)"; // Повернуть стрелочку
    }
}







$(document).ready(function() {
    let currentIndex = 0;

    // Код для первого слайдера
    const slides1 = $('.custom-slide');
    const dots1 = $('.custom-dot');
    const totalSlides1 = slides1.length;

    function updateCustomSlider1() {
        const newTransform = -currentIndex * 100;
        $('.custom-slider').css('transform', `translateX(${newTransform}%)`);
        updateDots1();
    }

    function updateDots1() {
        dots1.removeClass('active');
        dots1.eq(currentIndex).addClass('active');
    }

    $('.right-custom-arrow').click(function() {
        currentIndex += 1;
        if (currentIndex >= totalSlides1) {
            currentIndex = 0;
        }
        updateCustomSlider1();
    });

    $('.left-custom-arrow').click(function() {
        currentIndex -= 1;
        if (currentIndex < 0) {
            currentIndex = totalSlides1 - 1;
        }
        updateCustomSlider1();
    });

    dots1.click(function() {
        currentIndex = $(this).data('index');
        updateCustomSlider1();
    });

    updateDots1();

    // Код для второго слайдера
    currentIndex = 0; // Сброс индекса для второго слайдера
    const slides2 = $('.custom-slide2');
    const dots2 = $('.custom-dot2');
    const totalSlides2 = slides2.length;

    function updateCustomSlider2() {
        const newTransform = -currentIndex * 100;
        $('.custom-slider2').css('transform', `translateX(${newTransform}%)`);
        updateDots2();
    }

    function updateDots2() {
        dots2.removeClass('active2');
        dots2.eq(currentIndex).addClass('active2');
    }

    $('.right-custom-arrow2').click(function() {
        currentIndex += 1;
        if (currentIndex >= totalSlides2) {
            currentIndex = 0;
        }
        updateCustomSlider2();
    });

    $('.left-custom-arrow2').click(function() {
        currentIndex -= 1;
        if (currentIndex < 0) {
            currentIndex = totalSlides2 - 1;
        }
        updateCustomSlider2();
    });

    dots2.click(function() {
        currentIndex = $(this).data('index');
        updateCustomSlider2();
    });

    updateDots2();
});


const slider = document.querySelector('.slider1');
const slides = document.querySelectorAll('.slide1');

// Клонируем первые слайды, чтобы создать эффект бесконечной прокрутки
slides.forEach(slide => {
    const clone = slide.cloneNode(true);
    slider.appendChild(clone);
});

// Устанавливаем ширину контейнера в два раза больше, чтобы учесть клонированные слайды
slider.style.width = `${slides.length * 240 * 2}px`;

// Функция для запуска анимации
function startSlider() {
    slider.style.animation = 'scroll 100s linear infinite';
}

startSlider();

