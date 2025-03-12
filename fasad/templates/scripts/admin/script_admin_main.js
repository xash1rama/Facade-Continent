function showForm3(action, type, id = '', name = '', data = '') {
        document.getElementById('dataId').value = id || '';
        document.getElementById('dataName').value = name || ''; // Сохраняем значение для "Название" в скрытом поле
        document.getElementById('dataValue').value = data || '';

        // Изменение заголовка модального окна
        document.getElementById('modalTitle').innerText = action === 'edit' ? 'Изменить значение' : 'Добавить новое значение';

        // Открытие модального окна
        $('#dataFormModal').modal('show');

        // Установка обработчика события для кнопки сохранения
        document.getElementById('submitDataBtn').onclick = function() {
            if (action === 'edit') {
                updateData(id);
            } else {
                createData();
            }
        };
    }

    function createData() {
        const name = document.getElementById('dataName').value;
        const value = document.getElementById('dataValue').value;

        fetch('/admin/create_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, data: value })
        })
        .then(response => {
            if (!response.ok) throw new Error('Ошибка при добавлении данных');
            return response.json();
        })
        .then(data => {
            alert('Данные добавлены!');
            location.reload(); // Обновление страницы
        })
        .catch(error => {
            alert(error.message);
        })
        .finally(() => {
            $('#dataFormModal').modal('hide'); // Закрытие модального окна
        });
    }
        function updateData(id) {
        const name = document.getElementById('dataName').value;
        const value = document.getElementById('dataValue').value;

        fetch(`/admin/data_update`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id, name, data: value })
        })
        .then(response => {
            if (!response.ok) throw new Error('Ошибка при обновлении данных');
            return response.json();
        })
        .then(data => {
            alert('Данные обновлены!');
            location.reload(); // Обновление страницы
        })
        .catch(error => {
            alert(error.message);
        })
        .finally(() => {
            $('#dataFormModal').modal('hide'); // Закрытие модального окна
        });
    }

    function deleteItem3(type, id) {
        if (confirm('Вы уверены, что хотите удалить этот элемент?')) {
            fetch(`/admin/data`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ id })
            })
            .then(response => {
                if (!response.ok) throw new Error('Ошибка при удалении данных');
                alert('Данные удалены!');
                location.reload(); // Обновление страницы
            })
            .catch(error => {
                alert(error.message);
            });
        }
    }

