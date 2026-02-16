document.getElementById("vqa-form").addEventListener("submit", async function(e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append("image", document.getElementById("image").files[0]);
    formData.append("question", document.getElementById("question").value);
    formData.append("mode", document.getElementById("mode").value);

    const response = await fetch("http://localhost:5000/analyze", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    document.getElementById("output").innerText = data.response;
});
