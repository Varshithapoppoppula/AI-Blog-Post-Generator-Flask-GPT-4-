function generateBlog() {
    const topic = document.getElementById("topic").value;
    if (!topic) {
        alert("Please enter a topic!");
        return;
    }

    fetch("/generate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ topic })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText = data.blog_post;
    })
    .catch(error => console.error("Error:", error));
}
