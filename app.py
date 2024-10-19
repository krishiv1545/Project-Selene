from flask import Flask, render_template, request
from PIL import Image
import os
import numpy as np
import trimesh

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def process_image(filepath, pixel_size):
    input_img = Image.open(filepath).convert(mode="L").resize((pixel_size, pixel_size))
    img = input_img.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    pixel_data = np.array(img)
    unflipped_pixel_data = np.array(input_img)

    grounded_matrix = (pixel_data - np.min(pixel_data)) / 20.0
    print(np.min(grounded_matrix))
    print(np.max(grounded_matrix))

    output_img = Image.fromarray(unflipped_pixel_data)
    output_img.save("static/enhanced_images/output.png")
    return grounded_matrix

def generate_mesh(grounded_matrix, input_filename, save_path):
    X = np.linspace(-200, 200, grounded_matrix.shape[0])
    Z = np.linspace(-200, 200, grounded_matrix.shape[1]) 
    X, Z = np.meshgrid(X, Z)
    Y = grounded_matrix
    vertices = np.stack([X.ravel(), Z.ravel(), Y.ravel()], axis=-1) 
    idx = np.arange(grounded_matrix.size).reshape(grounded_matrix.shape)
    faces = np.stack([idx[:-1, :-1].ravel(), idx[:-1, 1:].ravel(), idx[1:, :-1].ravel()], axis=-1)
    faces = np.vstack([faces, np.stack([idx[:-1, 1:].ravel(), idx[1:, 1:].ravel(), idx[1:, :-1].ravel()], axis=-1)])
    mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
    base_name = os.path.splitext(input_filename)[0] 
    output_path = os.path.join(save_path, f"{base_name}.obj")
    mesh.export(output_path)
    return output_path

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        pixel_size = 1000
        filepath = f"static/uploads/{f.filename}"
        f.save(filepath)
        save_path = "static/plots"
        grounded_matrix = process_image(filepath, pixel_size)
        mesh_path = generate_mesh(grounded_matrix, f.filename, save_path)
        inputimgpath = f"../{filepath}"
        outputimgpath = "enhanced_images/output.png"
        outputimgpath = f"../static/{outputimgpath}"
        downloadattributename = f"enhanced_{f.filename}.png"
        print(downloadattributename)
        mesh_path_relative = os.path.relpath(mesh_path, start='static')
        return render_template("processing.html", name=f.filename, matrix=grounded_matrix.tolist(), mesh_path=mesh_path_relative, inputimgpath = inputimgpath, outputimgpath = outputimgpath, downloadattributename = downloadattributename)

@app.route('/model', methods=['POST'])
def model():
    if request.method == 'POST':
        f = request.files['file']
        pixel_size = 1000
        filepath = f"static/uploads/{f.filename}"
        f.save(filepath)
        save_path = r"static\plots"
        grounded_matrix = process_image(filepath, pixel_size)
        mesh_path = generate_mesh(grounded_matrix, f.filename, save_path)
        string_path = mesh_path
        return render_template("output.html", file_path=string_path)

if __name__ == '__main__':
    app.run(debug=True)