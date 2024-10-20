[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/krishiv1545/) 
Krishiv K.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/imkapil/) 
Kapil Parmar


## Project Selene

Have been working on this Project for a while. Finally put some work in for Syntax Error '24 Hackathon :D

The web application accepts any Lunar image captured by Chandrayaan-2's OHRC (Orbital High Resolution Camera), extracts the pixel brightness to plot a 3D Lunar Map.
This idea can be polished and used in Space Programs for more efficient navigation and/or in EdTech domain, both of which we're passionate about!

For now though, this was a fabulous project to work upon in order to learn many technologies used here such as Flask, Jinja, Three.js, NumPy, Pillow (PIL) and more. And this is just the beginning 💪.
![image](https://github.com/user-attachments/assets/b6e2ec06-ab2e-4549-91bd-e3407e25af18)


## How to run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run app.py 

```bash
flask run
```
in IDE

### 3. Access the app at the following URL

```bash
http://localhost:5000/
```

### 4. Samples

To work with, I've provided certain sample images. You can access the complete dataset from https://pradan.issdc.gov.in/ch2/protected/browse.xhtml?id=ohrc

### 5. Controls

Pinch and zoom in/out while viewing the Model.

## Future Prospects

In the repository, you may have noticed the crater.py and crater.obj files. The program essentially creates a crater 1/3rd the depth of it's diameter. The math is roughly explained in crater.png. 

What we aspire is to detect craters in the input images and replace them with the craters formed through crater.py for more accurate 3D modelling. 
All it takes for input is the diameter and center coordinates to patch over the existing 3D terrain map we created in this project.

Will love to implement upon this idea in the near future.

Thank you for bearing with us, give up some love ;) "⭐"
