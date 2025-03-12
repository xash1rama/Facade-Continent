
    function showStartForm(action, id, name = '', measure = '', price = '', material = '') {
    document.getElementById('startFacadeId').value = id || '';
    document.getElementById('startFacadeName').value = name || '';
    document.getElementById('startFacadePrice').value = price || '';


    // Установка выбранного значения для единицы измерения
    document.querySelectorAll('input[name="startMeasure"]').forEach((radio) => {
        radio.checked = false; // Сброс всех радиокнопок
    });

    if (measure === 'м²') {
        document.getElementById('startMeasureM2').checked = true;
    } else if (measure === 'м/п') {
        document.getElementById('startMeasureMP').checked = true;
    } else if (measure === 'Общая') {
        document.getElementById('startMeasureCommon').checked = true;
    }

    // Изменение заголовка модального окна
    document.getElementById('startModalTitle').innerText = action === 'edit' ? 'Изменить значение' : 'Добавить новое значение';

    // Открытие модального окна
    $('#startFacadeFormModal').modal('show');

    // Установка обработчика события для кнопки сохранения
    document.getElementById('submitStartFacadeBtn').onclick = function() {
        if (action === 'edit') {
            updateStartFacade(id);
        } else {
            createStartFacade();
        }
    };
}


    function createStartFacade() {
    const name = document.getElementById('startFacadeName').value;
    const measure = document.querySelector('input[name="startMeasure"]:checked').value;
    const price = document.getElementById('startFacadePrice').value;


    fetch('/admin/create_start_facade', {
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


    function updateStartFacade(id) {
        const name = document.getElementById('startFacadeName').value;
        const measure = document.querySelector('input[name="startMeasure"]:checked').value;
        const price = document.getElementById('startFacadePrice').value;

        fetch(`/admin/start_facade_update`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id, name, measure, price }),
        })
        .then(response => {
            if (response.ok) {
                location.reload(); // Обновление страницы после успешного обновления
            } else {
                alert('Ошибка при обновлении значения');
            }
        })
        .catch(error => console.error('Ошибка:', error));
    }

    function deleteStartItem(id) {
        if (confirm('Вы уверены, что хотите удалить этот элемент?')) {
            fetch(`/admin/start_facade/${id}`, {
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


function showBaseForm(action, id, name = '', measure = '', price = '') {
        document.getElementById('baseFacadeId').value = id || '';
        document.getElementById('baseFacadeName').value = name || '';
        document.getElementById('baseFacadePrice').value = price || '';


        // Установка выбранного значения для единицы измерения
        document.querySelectorAll('input[name="baseMeasure"]').forEach((radio) => {
            radio.checked = false; // Сброс всех радиокнопок
        });

        if (measure === 'м²') {
            document.getElementById('baseMeasureM2').checked = true;
        } else if (measure === 'м/п') {
            document.getElementById('baseMeasureMP').checked = true;
        } else if (measure === 'Общая') {
            document.getElementById('baseMeasureCommon').checked = true;
        }

        // Изменение заголовка модального окна
        document.getElementById('baseModalTitle').innerText = action === 'edit' ? 'Изменить значение' : 'Добавить новое значение';

        // Открытие модального окна
        $('#baseFacadeFormModal').modal('show');

        // Установка обработчика события для кнопки сохранения
        document.getElementById('submitBaseFacadeBtn').onclick = function() {
            if (action === 'edit') {
                updateBaseFacade(id);
            } else {
                createBaseFacade();
            }
        };
    }

    function createBaseFacade() {
    const name = document.getElementById('baseFacadeName').value;
    const measure = document.querySelector('input[name="baseMeasure"]:checked').value;
    const price = document.getElementById('baseFacadePrice').value;


    fetch('/admin/create_base_facade', {
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


    function updateBaseFacade(id) {
        const name = document.getElementById('baseFacadeName').value;
        const measure = document.querySelector('input[name="baseMeasure"]:checked').value;
        const price = document.getElementById('baseFacadePrice').value;


        fetch(`/admin/base_facade_update`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id, name, measure, price }),
        })
        .then(response => {
            if (response.ok) {
                location.reload(); // Обновление страницы после успешного обновления
            } else {
                alert('Ошибка при обновлении значения');
            }
        })
        .catch(error => console.error('Ошибка:', error));
    }

    function deleteBaseItem(id) {
        if (confirm('Вы уверены, что хотите удалить этот элемент?')) {
            fetch(`/admin/base_facade/${id}`, {
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




    function showFinishForm(action, id, name = '', measure = '', price = '') {
        document.getElementById('finishFacadeId').value = id || '';
        document.getElementById('finishFacadeName').value = name || '';
        document.getElementById('finishFacadePrice').value = price || '';

        // Установка выбранного значения для единицы измерения
        document.querySelectorAll('input[name="finishMeasure"]').forEach((radio) => {
            radio.checked = false; // Сброс всех радиокнопок
        });

        if (measure === 'м²') {
            document.getElementById('finishMeasureM2').checked = true;
        } else if (measure === 'м/п') {
            document.getElementById('finishMeasureMP').checked = true;
        } else if (measure === 'Общая') {
            document.getElementById('finishMeasureCommon').checked = true;
        }

        // Изменение заголовка модального окна
        document.getElementById('finishModalTitle').innerText = action === 'edit' ? 'Изменить значение' : 'Добавить новое значение';

        // Открытие модального окна
        $('#finishFacadeFormModal').modal('show');

        // Установка обработчика события для кнопки сохранения
        document.getElementById('submitFinishFacadeBtn').onclick = function() {
            if (action === 'edit') {
                updateFinishFacade(id);
            } else {
                createFinishFacade();
            }
        };
    }

    function createFinishFacade() {
        const name = document.getElementById('finishFacadeName').value;
        const measure = document.querySelector('input[name="finishMeasure"]:checked').value;
        const price = document.getElementById('finishFacadePrice').value;

        fetch('/admin/create_finish_facade', {
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

    function updateFinishFacade(id) {
        const name = document.getElementById('finishFacadeName').value;
        const measure = document.querySelector('input[name="finishMeasure"]:checked').value;
        const price = document.getElementById('finishFacadePrice').value;

        fetch(`/admin/finish_facade_update`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id, name, measure, price }),
        })
        .then(response => {
            if (response.ok) {
                location.reload(); // Обновление страницы после успешного обновления
            } else {
                alert('Ошибка при обновлении значения');
            }
        })
        .catch(error => console.error('Ошибка:', error));
    }

    function deleteFinishItem(id) {
        if (confirm('Вы уверены, что хотите удалить этот элемент?')) {
            fetch(`/admin/finish_facade/${id}`, {
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


