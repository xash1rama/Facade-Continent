
    function showStartRoofForm(action, id, name = '', measure = '', price = '') {
        document.getElementById('startRoofId').value = id || '';
        document.getElementById('startRoofName').value = name || '';
        document.getElementById('startRoofPrice').value = price || '';

        // Установка выбранного значения для единицы измерения
        document.querySelectorAll('input[name="startRoofMeasure"]').forEach((radio) => {
            radio.checked = false; // Сброс всех радиокнопок
        });

        if (measure === 'м²') {
            document.getElementById('startRoofMeasureM2').checked = true;
        } else if (measure === 'м/п') {
            document.getElementById('startRoofMeasureMP').checked = true;
        } else if (measure === 'Общая') {
            document.getElementById('startRoofMeasureCommon').checked = true;
        }

        // Изменение заголовка модального окна
        document.getElementById('startRoofModalTitle').innerText = action === 'edit' ? 'Изменить значение' : 'Добавить новое значение';

        // Открытие модального окна
        $('#startRoofFormModal').modal('show');

        // Установка обработчика события для кнопки сохранения
        document.getElementById('submitStartRoofBtn').onclick = function() {
            if (action === 'edit') {
                updateStartRoof(id);
            } else {
                createStartRoof();
            }
        };
    }

    function createStartRoof() {
        const name = document.getElementById('startRoofName').value;
        const measure = document.querySelector('input[name="startRoofMeasure"]:checked').value;
        const price = document.getElementById('startRoofPrice').value;

        fetch('/admin/create_start_roof', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, measure, price }),
        })
        .then(response => {
            if (response.ok) {
                location.reload(); // Обновление страницы после успешного добавления
            } else {
                alert('Ошибка при добавлении значения');
            }
        })
        .catch(error => console.error('Ошибка:', error));
    }

    function updateStartRoof(id) {
        const name = document.getElementById('startRoofName').value;
        const price = document.getElementById('startRoofPrice').value;

        // Получение выбранного значения радиокнопки
        const measure = document.querySelector('input[name="startRoofMeasure"]:checked').value;

        fetch(`/admin/start_roof_update/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id, name, price, measure }),
        })
        .then(response => {
            if (response.ok) {
                location.reload(); // Обновление страницы после успешного обновления
            } else {
                alert('Ошибка при обновлении значения');
            }
        })
        .catch(error => console.error('Ошибка при обновлении:', error));
    }

    function deleteStartRoofItem(id) {
        if (confirm('Вы уверены, что хотите удалить этот элемент?')) {
            fetch(`/admin/start_roof/${id}`, {
                method: 'DELETE',
            })
            .then(response => {
                if (response.ok) {
                    location.reload(); // Обновление страницы после успешного удаления
                } else {
                    alert('Ошибка при удалении значения');
                }
            })
            .catch(error => console.error('Ошибка:', error));
        }
    }



    function showBaseRoofForm(action, id, name = '', measure = '', price = '') {
        document.getElementById('baseRoofId').value = id || '';
        document.getElementById('baseRoofName').value = name || '';
        document.getElementById('baseRoofPrice').value = price || '';

        // Установка выбранного значения для единицы измерения
        document.querySelectorAll('input[name="baseRoofMeasure"]').forEach((radio) => {
            radio.checked = false; // Сброс всех радиокнопок
        });

        if (measure === 'м²') {
            document.getElementById('baseRoofMeasureM2').checked = true;
        } else if (measure === 'м/п') {
            document.getElementById('baseRoofMeasureMP').checked = true;
        } else if (measure === 'Общая') {
            document.getElementById('baseRoofMeasureCommon').checked = true;
        }

        // Изменение заголовка модального окна
        document.getElementById('baseRoofModalTitle').innerText = action === 'edit' ? 'Изменить значение' : 'Добавить новое значение';

        // Открытие модального окна
        $('#baseRoofFormModal').modal('show');

        // Установка обработчика события для кнопки сохранения
        document.getElementById('submitBaseRoofBtn').onclick = function() {
            if (action === 'edit') {
                updateBaseRoof(id);
            } else {
                createBaseRoof();
            }
        };
    }

    function createBaseRoof() {
        const name = document.getElementById('baseRoofName').value;
        const measure = document.querySelector('input[name="baseRoofMeasure"]:checked').value;
        const price = document.getElementById('baseRoofPrice').value;

        fetch('/admin/create_base_roof', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, measure, price }),
        })
        .then(response => {
            if (response.ok) {
                location.reload(); // Обновление страницы после успешного добавления
            } else {
                alert('Ошибка при добавлении значения');
            }
        })
        .catch(error => console.error('Ошибка:', error));
    }

    function updateBaseRoof(id) {
        const name = document.getElementById('baseRoofName').value;
        const price = document.getElementById('baseRoofPrice').value;

        // Получение выбранного значения радиокнопки
        const measure = document.querySelector('input[name="baseRoofMeasure"]:checked').value;

        fetch(`/admin/base_roof_update/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id, name, price, measure }),
        })
        .then(response => {
            if (response.ok) {
                location.reload(); // Обновление страницы после успешного обновления
            } else {
                alert('Ошибка при обновлении значения');
            }
        })
        .catch(error => console.error('Ошибка при обновлении:', error));
    }

    function deleteBaseRoofItem(id) {
        if (confirm('Вы уверены, что хотите удалить этот элемент?')) {
            fetch(`/admin/base_roof/${id}`, {
                method: 'DELETE',
            })
            .then(response => {
                if (response.ok) {
                    location.reload(); // Обновление страницы после успешного удаления
                } else {
                    alert('Ошибка при удалении значения');
                }
            })
            .catch(error => console.error('Ошибка:', error));
        }
    }




    function showFinishRoofForm(action, id, name = '', measure = '', price = '') {
        document.getElementById('finishRoofId').value = id || '';
        document.getElementById('finishRoofName').value = name || '';
        document.getElementById('finishRoofPrice').value = price || '';

        // Установка выбранного значения для единицы измерения
        document.querySelectorAll('input[name="finishRoofMeasure"]').forEach((radio) => {
            radio.checked = false; // Сброс всех радиокнопок
        });

        if (measure === 'м²') {
            document.getElementById('finishRoofMeasureM2').checked = true;
        } else if (measure === 'м/п') {
            document.getElementById('finishRoofMeasureMP').checked = true;
        } else if (measure === 'Общая') {
            document.getElementById('finishRoofMeasureCommon').checked = true;
        }

        // Изменение заголовка модального окна
        document.getElementById('finishRoofModalTitle').innerText = action === 'edit' ? 'Изменить значение' : 'Добавить новое значение';

        // Открытие модального окна
        $('#finishRoofFormModal').modal('show');

        // Установка обработчика события для кнопки сохранения
        document.getElementById('submitFinishRoofBtn').onclick = function() {
            if (action === 'edit') {
                updateFinishRoof(id);
            } else {
                createFinishRoof();
            }
        };
    }

    function createFinishRoof() {
        const name = document.getElementById('finishRoofName').value;
        const measure = document.querySelector('input[name="finishRoofMeasure"]:checked').value;
        const price = document.getElementById('finishRoofPrice').value;

        fetch('/admin/create_finish_roof', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, measure, price }),
        })
        .then(response => {
            if (response.ok) {
                location.reload(); // Обновление страницы после успешного добавления
            } else {
                alert('Ошибка при добавлении значения');
            }
        })
        .catch(error => console.error('Ошибка:', error));
    }

    function updateFinishRoof(id) {
        const name = document.getElementById('finishRoofName').value;
        const price = document.getElementById('finishRoofPrice').value;

        // Получение выбранного значения радиокнопки
        const measure = document.querySelector('input[name="finishRoofMeasure"]:checked').value;

        fetch(`/admin/finish_roof_update/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id, name, price, measure }),
        })
        .then(response => {
            if (response.ok) {
                location.reload(); // Обновление страницы после успешного обновления
            } else {
                alert('Ошибка при обновлении значения');
            }
        })
        .catch(error => console.error('Ошибка при обновлении:', error));
    }

    function deleteFinishRoofItem(id) {
        if (confirm('Вы уверены, что хотите удалить этот элемент?')) {
            fetch(`/admin/finish_roof/${id}`, {
                method: 'DELETE',
            })
            .then(response => {
                if (response.ok) {
                    location.reload(); // Обновление страницы после успешного удаления
                } else {
                    alert('Ошибка при удалении значения');
                }
            })
            .catch(error => console.error('Ошибка:', error));
        }
    }




