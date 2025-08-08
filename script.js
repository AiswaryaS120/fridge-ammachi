async function uploadImage() {
  const fileInput = document.getElementById("fileInput");
  if (fileInput.files.length === 0) {
    alert("Please select a file!");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  const response = await fetch("http://127.0.0.1:8000/detect", {
    method: "POST",
    body: formData
  });

  const blob = await response.blob();
  const imageUrl = URL.createObjectURL(blob);
  document.getElementById("outputImage").src = imageUrl;
}
