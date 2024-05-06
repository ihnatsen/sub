
$(document).ready(function () {
let table = $('#carsdatabases').DataTable({
    columns: [
    { data: 'regNr' },
    { data: 'dateGet' },
    { data: 'name' },
    { data: 'surname' },
    { data: 'dateBack' },
    { data: 'action' }
    ]
});

$('#myForm').submit(function (event) {
event.preventDefault();
    let regNr = $('#regNr').val();
    let dateGet = $('#dateGet').val();
    let name = $('#name').val();
    let surname = $('#surname').val();
    let dateBack = $('#dateBack').val();
    addNewPerson(regNr, dateGet, name, surname, dateBack);
    $('#myForm')[0].reset();
});

function addNewPerson(regNr, dateGet, name, surname, dateBack) {
    let newPerson = {
        regNr: regNr,
        dateGet: dateGet,
        name: name,
        surname: surname,
        dateBack: dateBack,
        action: '<button class="edit">Usun</button>'
    };
    table.row.add(newPerson).draw();
    updatePeopleList();
}

$('#carsdatabases tbody').on('click', '.edit', function () {
    let rowData = table.row($(this).parents('tr')).data();
    edit.call(this, rowData);
});

function edit(rowData) {
    let newDateBack = prompt("Nowa data zwrotu:");
    if (newDateBack !== null) {
        rowData.dateBack = newDateBack;
        table.row($(this).parents('tr')).data(rowData).draw();
        updatePeopleList();
    }
}


function updatePeopleList() {
    $('#peopleList').empty();
    table.rows().every(function () {
        let data = this.data();
        let listItem = document.createElement("li");
        listItem.textContent = "Nr Rejestracyjny: " + data.regNr + ", Data Wypozyczenia: " + data.dateGet +
        ", Imie: " + data.name + ", Nazwisko: " + data.surname + ", Data Zwrotu: " + data.dateBack;
        document.getElementById("peopleList").appendChild(listItem);
    });
}
});

