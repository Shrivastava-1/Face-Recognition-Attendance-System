<h1>📸 Face Recognition Attendance System</h1>

<p>This project is a <strong>Face Recognition-based Attendance System</strong> developed using Python, OpenCV, and the <code>face_recognition</code> library. It uses your webcam to recognize pre-registered students and automatically marks their attendance in a dated CSV file.</p>

<h2>🚀 Features</h2>
<ul>
  <li>Live webcam feed for real-time face detection.</li>
  <li>Face encoding and matching using the <code>face_recognition</code> library.</li>
  <li>Stores student attendance in a daily <code>.csv</code> file.</li>
  <li>Automatically skips duplicates — one entry per person per day.</li>
  <li>Encodes faces from a folder named <code>Images/</code>.</li>
</ul>

<h2>🛠️ Technologies Used</h2>
<ul>
  <li>Python</li>
  <li>OpenCV</li>
  <li>face_recognition (dlib-based)</li>
  <li>NumPy</li>
  <li>CSV module</li>
  <li>Pickle</li>
</ul>

<h2>📂 Folder Structure</h2>
<pre>
project/
│
├── Images/                  # Folder containing images of enrolled students
│   ├── John.jpg             # Image file name = Student Name
│   └── Alice.jpg
│
├── encodings.pickle         # Saved face encodings
├── Attendance_dd-mm-yyyy.csv # Automatically generated daily attendance file
├── main.py                  # Your main script (face recognition code)
└── README.html
</pre>

<h2>🧑‍🏫 How To Use</h2>

<h3>1. 🔧 Install Dependencies</h3>
<pre><code>pip install opencv-python face_recognition numpy</code></pre>
<p><strong>Note:</strong> <code>face_recognition</code> requires <code>dlib</code>. If you face installation issues, refer to <a href="https://pypi.org/project/dlib/" target="_blank">dlib installation guide</a>.</p>

<h3>2. 🖼 Add Student Images</h3>
<p>Place clear front-facing images of each student in the <code>Images/</code> folder.<br>
File name should be the <strong>student’s name or enrollment number</strong>, e.g., <code>20123456.jpg</code>.</p>

<h3>3. ▶️ Run the Script</h3>
<pre><code>python main.py</code></pre>

<h3>4. 📊 View Attendance</h3>
<p>A new <code>.csv</code> file is created automatically with the name:<br>
<code>Attendance_dd-mm-yyyy.csv</code></p>

<h2>📝 Example CSV Output</h2>
<table border="1" cellpadding="6" cellspacing="0">
  <tr>
    <th>Enrollment Number</th>
    <th>Time</th>
    <th>Date</th>
  </tr>
  <tr>
    <td>20123456</td>
    <td>10:15:32</td>
    <td>06-04-2025</td>
  </tr>
  <tr>
    <td>20123478</td>
    <td>10:17:05</td>
    <td>06-04-2025</td>
  </tr>
</table>

<h2>🧠 How It Works (Brief)</h2>
<ol>
  <li>Load and encode all images in <code>Images/</code>.</li>
  <li>Capture video stream from webcam.</li>
  <li>Detect faces in real-time, and compare with known encodings.</li>
  <li>If a match is found, mark attendance in the CSV file with a timestamp.</li>
  <li>Skip if already marked.</li>
</ol>

<h2>💡 Future Improvements</h2>
<ul>
  <li>Add a GUI (Tkinter or PyQT) for easier usage.</li>
  <li>Store data in a database instead of CSV.</li>
  <li>Add login authentication for teachers/admins.</li>
  <li>Email daily attendance reports.</li>
</ul>

<h2>📷 Sample Screenshot</h2>
<p><em>(Add a screenshot of the webcam window with rectangle & name showing.)</em></p>

<h2>👨‍💻 Author</h2>
<p>Made with ❤️ by <a href="https://github.com/yourusername" target="_blank">Your Name</a></p>
