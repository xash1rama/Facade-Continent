async function deleteItem(id) {
    const confirmation = confirm("Вы уверены, что хотите удалить этот элемент?");
    if (confirmation) {
        try {
            const response = await fetch(`/admin_delete_order/${id}`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    // Добавьте авторизацию, если это необходимо
                    // 'Authorization': 'Basic ' + btoa('username:password')
                }
            });

            if (response.ok) {
                // Удаляем строку из таблицы
                document.getElementById(`row-${id}`).remove();
                alert("Элемент успешно удален!");
            } else {
                alert("Ошибка при удалении элемента.");
            }
        } catch (error) {
            console.error('Ошибка:', error);
            alert("Произошла ошибка при удалении элемента.");
        }
    }
}


