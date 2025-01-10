import os

# Define the directory where the images are stored
image_dir = './images'

# Get the list of image files in the directory (assuming all files are images)
image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

# Start the HTML content
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            text-align: center;
        }
        .gallery {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }
        .gallery div {
            text-align: center;
        }
        img {
            max-width: 300px;
            height: auto;
            display: block;
            margin: 0 auto;
        }
        .filename {
            margin-top: 5px;
            font-size: 14px;
            word-wrap: break-word;
            max-width: 300px;
            white-space: normal;
        }
    </style>
</head>
<body>

    <h1>Image Gallery</h1>
    <div class="gallery">
'''

# Loop through each image file and add it to the HTML content
for image in image_files:
    image_path = os.path.join(image_dir, image)
    html_content += f'''
        <div>
            <img src="{image_path}" alt="{image}">
            <div class="filename">{image}</div>
        </div>
    '''

# Close the gallery div and the HTML structure
html_content += '''
    </div>

</body>
</html>
'''

# Write the generated HTML to a file
output_file = 'gallery.html'
with open(output_file, 'w') as file:
    file.write(html_content)

print(f"HTML gallery generated successfully. Open '{output_file}' in your browser to view it.")

