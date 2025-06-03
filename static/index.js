// using the fetch function to get the data necessary
fetch("/api/message")
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));

