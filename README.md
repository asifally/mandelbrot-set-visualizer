# Mandelbrot Set Visualizer

This project displays the [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set). It contains a backend python fastapi application server that returns a list of data points corresponding to the amount of iterations it took for the complex number to escape the Mandelbrot set. A gradient is produced on the frontend that shows whether or not a complex number escapes the Mandelbrot set in the max amount of interations set.

Mandelbrot Set equation:
```
f(z) = z^2 + c
```
where c is a complex number

## Usage/Development

Navigate to the project folder and install python packages
```
pipenv install
```
Install node packages
```
npm install
```
Run backend server
```
uvicorn backend.main:app --reload
```

Open a browser and navigate to 
```
http://127.0.0.1:8000/static/index.html
```

## Documentation
Do the above steps then go to
```
http://127.0.0.1:8000/docs
```

