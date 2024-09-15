document.getElementById('image-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const input = document.getElementById('imageInput');
    const file = input.files[0];

    if (file) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            const outputImage = document.getElementById('outputImage');
            outputImage.src = e.target.result;  // Set uploaded image as preview
        };
        
        reader.readAsDataURL(file);
    }
});
