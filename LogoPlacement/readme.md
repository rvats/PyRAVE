## Build
docker build --no-cache -t image_logo_overlay .
## Run
docker run --rm -v "C:\Edited\Vertical:/app/input_images" -v "C:\Edited\Vertical\Edited:/app/output_images" -v "C:\Edited\logos:/app/logos" image_logo_overlay /app/input_images /app/output_images /app/logos/MPAD.jpg "Bottom Right"