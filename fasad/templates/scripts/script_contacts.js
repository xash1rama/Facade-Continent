function showNotification(notificationId) {
    const notification = document.getElementById(notificationId);
    notification.classList.add('show'); // Добавляем класс для показа

    // Убираем уведомление через 7 секунд
    setTimeout(() => {
        notification.classList.remove('show'); // Убираем класс показа
        notification.classList.add('hide'); // Добавляем класс скрытия

        // Удаляем уведомление из DOM через 0.5 секунды (время анимации)
        setTimeout(() => {
            notification.style.display = 'none'; // Скрываем уведомление
            notification.classList.remove('hide'); // Убираем класс скрытия
        }, 500);
    }, 7000); // Убираем уведомление через 7 секунд
}


// Функция обратного отсчета
function updateCountdown(lastSubmitTime) {
    const currentTime = new Date().getTime();
    const timeRemaining = 3600000 - (currentTime - lastSubmitTime); // Оставшееся время в миллисекундах

    if (timeRemaining > 0) {
        const minutes = Math.floor((timeRemaining / 1000) / 60);
        const seconds = Math.floor((timeRemaining / 1000) % 60);
        document.getElementById('countdown').innerText = `Осталось времени до следующей отправки: ${minutes} мин ${seconds} сек`;
        document.getElementById('countdown').style.display = 'block'; // Показываем счетчик
        setTimeout(() => updateCountdown(lastSubmitTime), 1000); // Обновляем каждую секунду
    } else {
        document.getElementById('countdown').style.display = 'none'; // Скрываем счетчик, когда время истекло
    }
}


    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Отменяем стандартное поведение отправки формы

        const currentTime = new Date().getTime(); // Текущее время
        const lastSubmitTime = localStorage.getItem('lastSubmitTime'); // Получаем время последней отправки из localStorage

        // Проверяем, прошло ли 1 час (3600000 миллисекунд) с последней отправки
        if (lastSubmitTime && (currentTime - lastSubmitTime < 3600000)) {
            document.getElementById('errorNotification').style.display = 'block'; // Показываем сообщение об ошибке
            document.getElementById('notification').style.display = 'none'; // Скрываем успешное сообщение
            updateCountdown(parseInt(lastSubmitTime)); // Запускаем обратный отсчет
            return; // Выходим из функции
        }

        const formData = new FormData(this); // Собираем данные формы

        // Отправляем данные на сервер
        fetch('/contact_form', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при отправке данных');
            }
            return response.json(); // Предполагаем, что сервер возвращает JSON
        })
        .then(data => {
               console.log('Успешно отправлено:', data);
            document.getElementById('notification').style.display = 'block'; // Показываем успешное сообщение
            document.getElementById('errorNotification').style.display = 'none'; // Скрываем сообщение об ошибке
            localStorage.setItem('lastSubmitTime', currentTime); // Сохраняем время последней отправки
            updateCountdown(currentTime); // Запускаем обратный отсчет
        })
        .catch(error => {
            console.error('Ошибка:', error);
            document.getElementById('errorNotification').style.display = 'block'; // Показываем сообщение об ошибке
            document.getElementById('notification').style.display = 'none'; // Скрываем успешное сообщение
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


