# Shape-and-Tree-Recognizer

This project aims to develop a program capable of recognizing specific shapes and distinguishing between various types of trees using boundary descriptors. These descriptors include parameters such as length of the boundary, diameter, eccentricity, and others.

<h2>Objective:</h2>
The primary goal is to determine whether the image depicts a single shape or a tree. If it's a tree, we further categorize it into Class 1 (comprising a circle and a rectangle) or Class 2 (comprising a triangle and a rectangle). For single shapes, we aim to classify them based on boundary characteristics such as length, area, circularity, and compactness.

<br/>
<br/>

<h2>Shape Recognition Process:</h2>

<h3>1- Identification:</h3> We detect intersecting shapes to determine if the image represents a tree or a single shape.
<h3>2- Tree Classification:</h3> Classify trees into Class 1 or Class 2 based on their constituent shapes (circle, rectangle, triangle).
<h3>3- Single Shape Recognition:</h3>

* Calculate boundary length and area.
* Determine circularity to identify circles (circularity > 0.85).
* For non-circular shapes, compute extreme position points and contour moments to find the center and distinguish between rectangle and triangle.
* Recognize triangles based on the position of extreme points.
<h3>4- Output Generation:</h3> Utilize the center and topmost point of each contour to print the name of single shapes and tree types.

<br/>
<br/>

<h2>Samples:</h2>

<h3>Sample 1:</h3>
<br/>

* **Input:**
<br/>

![image](https://github.com/AbdelrahmanJaber/Shape-and-Tree-Recognizer/assets/113253216/2dd4d670-ff0e-44da-9c4b-f1afb36a248a)

<br/>

* **Output:**
<br/>

![image](https://github.com/AbdelrahmanJaber/Shape-and-Tree-Recognizer/assets/113253216/d18116bf-f0d1-4ec8-b880-bfd34449debc)

<br/>
<br/>

<h3>Sample 2:</h3>
<br/>

* **Input:**
<br/>

![image](https://github.com/AbdelrahmanJaber/Shape-and-Tree-Recognizer/assets/113253216/e8d70f2f-2b27-4403-8afe-d34aaafbabd0)

<br/>

* **Output:**
<br/>

![image](https://github.com/AbdelrahmanJaber/Shape-and-Tree-Recognizer/assets/113253216/da9fb7c6-d1d8-4501-b2d0-774d796a189a)
