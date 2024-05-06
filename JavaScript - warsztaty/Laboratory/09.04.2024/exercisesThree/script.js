


$(document).ready(function () {
table = $('#peopleTable').DataTable({
    columns: [
        { data: 'name' }
    ]
});
});

let random_const = Math.floor(Math.random() * 100 + 1);

function randomNumber() {
    console.log("func", random_const);

let getNum = document.getElementById('Number').value;

    if (getNum < random_const) {
        alert(getNum + "licba jest mniej");
    } else if (getNum > random_const) {
        alert(getNum + " > licba jest wieksza");
    } else {
        alert('Wygrales: liczba jest' + getNum)
        add(document.getElementById("name").value);
    }
}

function add(name) {
    let newPerson = { name: name };
    table.row.add(newPerson).draw();
}
