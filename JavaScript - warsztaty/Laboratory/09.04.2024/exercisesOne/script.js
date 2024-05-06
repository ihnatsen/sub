let peopleList = [];
let table = $('#peopleTable').DataTable({
    columns: [
        { data: 'name' },
        { data: 'surname' },
        { data: 'email' },
        { data: 'date' },
        { data: 'action' }
    ]
});

function addNewPerson(name, surname, email, date) {
    let newPerson = {
        name: name,
        surname: surname,
        email: email,
        date: date,
        action: '<button class="removeButton">Usuń</button>'
    };
    table.row.add(newPerson).draw();
    peopleList.push(newPerson);
    updatePeopleList();
}

function checkingByKey(value, key, list) {
    if (list.length === 0){
        return false;
    }
    for(let i = 0; i < list.length; ++i){
        if(list[i][key] === value){
            return true;
        }
    }
    return false;
}

function updatePeopleList() {

    document.getElementById("peopleList").innerHTML = "";


    peopleList.forEach(function (person) {
        let listItem = document.createElement("li");
        listItem.textContent = "Imię: " + person.name + ", Nazwisko: " + person.surname + ", Email: " + person.email + ", Data zatr.: " + person.date;
        document.getElementById("peopleList").appendChild(listItem);
    });
}

$('#peopleTable tbody').on('click', '.removeButton', function () {
    let rowData = table.row($(this).parents('tr')).data();
    let email = rowData.email;

    peopleList = peopleList.filter(person => person.email !== email);

    table.row($(this).parents('tr')).remove().draw();

    updatePeopleList();
});

function main() {
    document.getElementById("myForm").addEventListener("submit", function (event) {
        event.preventDefault();

        let name = document.getElementById("name").value;
        let surname = document.getElementById("surname").value;
        let email = document.getElementById("email").value;
        let date = document.getElementById("date").value;

        if (checkingByKey(email, 'email',peopleList)) {
            alert("email jest kożystany!!!");
            return ;
        }
        addNewPerson(name, surname, email, date);

        document.getElementById("myForm").reset();
    });
}

main()