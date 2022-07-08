const axios = require('axios');

axios.get("http://localhost:5000/techtalk").then(response => {
    console.log(response.data);
}).catch(error => {
    console.error(error);
});

const payload = { "message": "Hello there!" };

axios.post("http://localhost:5000/ilikecs", JSON.stringify(payload), {
    headers: {
        'Content-Type': 'application/json'
    }
}).then(response => {
    console.log(response.data);
}).catch(error => {
    console.error(error);
});
