document.addEventListener("DOMContentLoaded", function() {
    fetch('/admin_portfolio_roof_gallery')
        .then(response => response.json())
        .then(data => {
            const portfolioList = document.getElementById('portfolio-list');
            data.forEach(portfolio => {
                const item = document.createElement('div');
                item.className = 'portfolio-item';
                item.innerHTML = `
                    <h2>${portfolio.title}</h2>
                    <img src="image/portfolio/${portfolio.main}" alt="Главное изображение" class="main-image">
                    <p>${portfolio.description}</p>
                    <button class="btn btn-info" onclick="showGallery(${portfolio.id})">Показать галерею</button>
                    <button class="btn btn-warning" onclick="openPortfolioForm(${portfolio.id})">Изменить</button>
                    <button class="btn btn-danger" onclick="deletePortfolio(${portfolio.id})">Удалить</button>
                    <button class="btn btn-success" onclick="uploadPhotos(${portfolio.id})">Добавить фото</button>
                    <div id="gallery-${portfolio.id}" class="gallery" style="display:none;"></div>
                `;
                portfolioList.appendChild(item);
            });
        })
        .catch(error => console.error("Ошибка при получении данных:", error));
});


document.getElementById('createPortfolioButton').addEventListener('click', function() {
    $('#createPortfolioModal').modal('show'); // Показать модальное окно с помощью Bootstrap
});
    function openPortfolioForm(portfolioId = null) {
    const portfolioIdInput = document.getElementById('portfolioId');
    portfolioIdInput.value = portfolioId; // Убедитесь, что значение устанавливается

    if (portfolioId) {
        // Логика для заполнения формы данными портфолио
        fetch(`/admin_portfolio_roof/${portfolioId}`)
            .then(response => response.json())
            .then(data => {
                const titleInput = document.getElementById('title');
                const descriptionInput = document.getElementById('description');
                titleInput.value = data.title;
                descriptionInput.value = data.description;
            });
    } else {
        // Логика для создания нового портфолио
    }
    $('#portfolioModal').modal('show');
}


document.getElementById('portfolioForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const portfolioId = document.getElementById('portfolioId').value;

    const formData = new FormData();
    formData.append('title', title);
    formData.append('description', description);

    fetch(`/admin_portfolio_roof/${portfolioId}`, {
        method: 'PUT',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Сервер вернул ошибку: " + response.status);
        }
        return response.json();
    })
    .then(data => {
        $('#portfolioModal').modal('hide');
        location.reload(); // Обновляем страницу, чтобы увидеть изменения
    })
    .catch(error => console.error("Ошибка при сохранении портфолио:", error));
});



// Обработчик для изменения главного изображения
document.getElementById('changeMainImageButton').addEventListener('click', function() {
    const mainImage = document.getElementById('mainImage').files[0];
    const portfolioId = document.getElementById('portfolioId').value;

    if (!mainImage) {
        alert("Пожалуйста, выберите главное изображение.");
        return;
    }

    const formData = new FormData();
    formData.append('main', mainImage);

    fetch(`/admin_portfolio_roof/${portfolioId}/main-image`, {
        method: 'PUT',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Сервер вернул ошибку: " + response.status);
        }
        return response.json();
    })
    .then(data => {
        $('#portfolioModal').modal('hide');
        location.reload(); // Обновляем страницу, чтобы увидеть изменения
    })
    .catch(error => console.error("Ошибка при изменении главного изображения:", error));
});

    function openPhoto(filename) {
    const imgElement = document.getElementById('modalImage');
    imgElement.src = `image/portfolio/${filename}`; // Устанавливаем источник изображения
    $('#photoModal').modal('show'); // Показываем модальное окно
}

function uploadPhotos(portfolioId) {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.multiple = true; // Позволяем выбирать несколько файлов
    input.onchange = () => {
        const files = input.files;
        if (files.length === 0) {
            alert("Пожалуйста, выберите хотя бы одно изображение.");
            return;
        }

        const formData = new FormData();
        for (let i = 0; i < files.length; i++) {
            formData.append('photos', files[i]); // Убираем '[]'
        }

        fetch(`/admin_portfolio_roof/${portfolioId}/photos`, {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Ошибка при загрузке фотографий: " + response.status);
            }
            return response.json();
        })
        .then(data => {
            console.log("Фотографии загружены:", data);
            location.reload(); // Перезагрузка страницы для обновления данных
        })
        .catch(error => {
            console.error("Ошибка:", error);
        });
    };
    input.click();
}


    function showGallery(portfolioId) {
    const gallery = document.getElementById(`gallery-${portfolioId}`);
    gallery.style.display = gallery.style.display === 'none' ? 'block' : 'none';
    if (gallery.style.display === 'block') {
        fetch(`/admin_portfolio_roof/${portfolioId}/photos`)
            .then(response => response.json())
            .then(photos => {
                gallery.innerHTML = photos.map(photo => {
                    return `
                        <div data-photo-filename="${photo.filename}">
                            <img src="image/portfolio/${photo.filename}" alt="Фото" style="width: 100px; margin: 5px; cursor: pointer;" onclick="openPhoto('${photo.filename}')">
                            <button class="btn btn-danger" onclick="deletePhoto('${portfolioId}', '${photo.filename}', this)">Удалить</button>
                        </div>
                    `;
                }).join('');
            })
            .catch(error => console.error("Ошибка при получении фотографий:", error));
    }
}


    function deletePhoto(portfolioId, filename, button) {
        console.log(`Попытка удалить фото с именем: ${filename} из портфолио с ID: ${portfolioId}`);
        fetch(`/admin_portfolio_roof/${portfolioId}/photos/${filename}`, {
            method: 'DELETE'
        })
        .then(response => {
            console.log("Статус ответа:", response.status);
            if (!response.ok) {
                throw new Error("Ошибка при удалении фото");
            }
            return response.json();
        })
        .then(data => {
            console.log("Ответ от сервера:", data);
            // Удаление элемента фотографии из DOM
            const photoElement = button.parentElement; // Получаем родительский элемент кнопки
            photoElement.remove(); // Удаляем элемент фотографии
        })
        .catch(error => console.error("Ошибка:", error));
    }

    document.getElementById('createPortfolioButton').addEventListener('click', function() {
    document.getElementById('createPortfolioModal').style.display = 'block'; // Показать модальное окно
});

document.getElementById('createPortfolioForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвратить стандартное поведение формы

    const title = document.getElementById('newTitle').value;
    const description = document.getElementById('newDescription').value;
    const mainImage = document.getElementById('newMainImage').files[0];

    const formData = new FormData();
    formData.append('title', title);
    formData.append('description', description);
    formData.append('main', mainImage);

    fetch(`/admin_create_portfolio_roof`, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Сервер вернул ошибку: " + response.status);
        }
        return response.json();
    })
    .then(data => {
        console.log("Портфолио создано:", data);
        $('#createPortfolioModal').modal('hide');
        location.reload(); // Обновляем страницу, чтобы увидеть изменения
    })
    .catch(error => console.error("Ошибка при создании портфолио:", error));
});

function closeModal() {
    document.getElementById('createPortfolioModal').style.display = 'none'; // Скрыть модальное окно
}

    function deletePortfolio(portfolioId) {
    if (confirm("Вы уверены, что хотите удалить это портфолио?")) {
        fetch(`/admin_delete_portfolio_roof/${portfolioId}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Ошибка при удалении портфолио: " + response.status);
            }
            return response.json();
        })
        .then(data => {
            console.log("Портфолио успешно удалено:", data);
            location.reload(); // Обновляем страницу, чтобы увидеть изменения
        })
        .catch(error => console.error("Ошибка при удалении портфолио:", error));
    }
}
