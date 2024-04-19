function deleteNote(employeeID) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ employeeID: employeeID }),
        }).then((_res) => {
            window.location.href = "/";
        });
    }