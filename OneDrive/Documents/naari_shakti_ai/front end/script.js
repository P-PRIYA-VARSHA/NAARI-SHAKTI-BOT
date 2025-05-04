function sendEmergencyAlert() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            let data = {
                latitude: position.coords.latitude,
                longitude: position.coords.longitude
            };

            fetch("http://127.0.0.1:5000/emergency", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("status").innerText = data.message;
            })
            .catch(error => {
                document.getElementById("status").innerText = "Error sending alert!";
                console.error("Error:", error);
            });
        });
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}
