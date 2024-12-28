function fillFilmList() {
    fetch('/lab7/rest-api/films/')
        .then(data => data.json())
        .then(films => {
            const tbody = document.getElementById('film-list');
            tbody.innerHTML = '';

            films.forEach((film, index) => {
                const tr = document.createElement('tr');

                const tdTitleRus = document.createElement('td');
                tdTitleRus.innerText = film.title_ru;

                const tdTitle = document.createElement('td');
                tdTitle.innerHTML = film.title ? `<i>(${film.title})</i>` : '';

                const tdYear = document.createElement('td');
                tdYear.innerText = film.year;

                const tdActions = document.createElement('td');
                const editButton = document.createElement('button');
                editButton.innerText = 'редактировать';
                editButton.onclick = () => editFilm(index);

                const delButton = document.createElement('button');
                delButton.innerText = 'удалить';
                delButton.onclick = () => deleteFilm(index, film.title_ru);

                tdActions.append(editButton, delButton);
                tr.append(tdTitleRus, tdTitle, tdYear, tdActions);
                tbody.append(tr);
            });
        });
}

function deleteFilm(id, title) {
    if (!confirm(`Вы точно хотите удалить фильм "${title}"?`)) return;

    fetch(`/lab7/rest-api/films/${id}`, { method: 'DELETE' })
        .then(() => fillFilmList());
}

function showModal() {
    document.querySelector('div.modal').style.display = 'block';
}

function hideModal() {
    document.querySelector('div.modal').style.display = 'none';
}

function cancel() {
    hideModal();
}

function addFilm() {
    document.getElementById('id').value = '';
    document.getElementById('title').value = '';
    document.getElementById('title-ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    showModal();
}

function sendFilm() {
    const id = document.getElementById('id').value;
    const film = {
        title: document.getElementById('title').value.trim(),
        title_ru: document.getElementById('title-ru').value.trim(),
        year: document.getElementById('year').value.trim(),
        description: document.getElementById('description').value.trim(),
    };

    const url = `/lab7/rest-api/films/${id}`;
    const method = id === '' ? 'POST' : 'PUT';

    fetch(url, {
        method: method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(film),
    })
        .then(resp => {
            if (resp.ok) {
                fillFilmList();
                hideModal();
                return {};
            }
            return resp.json();
        })
        .then(errors => {
            if (errors.description) {
                document.getElementById('description-error').innerText = errors.description;
            }
        });
}

function editFilm(id) {
    fetch(`/lab7/rest-api/films/${id}`)
        .then(data => data.json())
        .then(film => {
            document.getElementById('id').value = id;
            document.getElementById('title').value = film.title;
            document.getElementById('title-ru').value = film.title_ru;
            document.getElementById('year').value = film.year;
            document.getElementById('description').value = film.description;
            showModal();
        });
}

