function generateArt() {

    fetch('/mandlebrot_set')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            drawArt(data);   
        })
        .catch(error => {
            console.error("Error:", error)
        })
}

function drawArt(data) {
    max_iter = data.max_iter
    data = data.data
    const canvas = document.getElementById('art-canvas');
    const ctx = canvas.getContext('2d');

    // Set the canvas size
    canvas.width = data[0].length;
    canvas.height = data.length;

    // Iterate over the data and draw pixels
    for (let y = 0; y < data.length; y++) {
        for (let x = 0; x < data[y].length; x++) {
            const value = data[y][x]; // Get the integer value from the 2D list
            const color = getColor(value, max_iter); // Convert the integer value to a color
            ctx.fillStyle = color;
            ctx.fillRect(x, y, 1, 1); // Draw a 1x1 pixel at position (x, y) with the selected color
        }
    }
}

function getColor(value, max_iter) {
    // Define the start and end colors of the gradient
    const endColor = [0, 0, 0]; // White
    const startColor = [255, 255, 255]; // Black

    // Calculate the color components for the given value
    const color = startColor.map((startComponent, index) => {
        const endComponent = endColor[index];
        return Math.round(startComponent + (endComponent - startComponent) * (value / max_iter));
    });

    // Return the color as a CSS string
    return `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
}
