# Multi-Language Code Runner / Çok Dilli Kod Çalıştırıcı

A web-based code editor and runner that supports **Python, C, and JavaScript**.  
Users can write code in the browser, select the language, and run it safely on the backend.  
Errors are displayed in red, while standard output is green.

---

## Features / Özellikler

- Supports **Python, C, JavaScript**  
- Syntax highlighting in the editor using Prism.js  
- Safe execution environment for Python code  
- Color-coded output: green for success, red for errors  
- Clear button to reset editor and output  

---

## Folder Structure / Klasör Yapısı

first-project/
│
├─ backend/
│ ├─ app.py # Flask backend
│ ├─ runner.py # Python runner
│ ├─ main.py # Optional helper
│
├─ frontend/
│ ├─ src/
│ │ ├─ App.js # React frontend
│ │ └─ index.js
│ ├─ package.json
│ └─ ...

yaml
Kodu kopyala

---

## Requirements / Gereksinimler

- **Python 3.x**  
- **Node.js + npm**  
- **GCC** (for compiling C code on Windows)  

---

## Installation / Kurulum

1. Clone the repository / Depoyu klonlayın:

```bash
git clone https://github.com/yourusername/first-project.git
cd first-project
Install frontend dependencies / Frontend bağımlılıklarını yükleyin:

bash
Kodu kopyala
cd frontend
npm install
Install backend dependencies / Backend bağımlılıklarını yükleyin:

bash
Kodu kopyala
cd ../backend
pip install flask flask-cors
Make sure GCC is installed and in PATH for C compilation / C derlemesi için GCC’nin PATH’e ekli olduğundan emin olun.

Running the Project / Projeyi Çalıştırma
Start backend / Backend’i başlatın:

bash
Kodu kopyala
cd backend
python app.py
Start frontend / Frontend’i başlatın:

bash
Kodu kopyala
cd ../frontend
npm start
Open your browser at http://localhost:3000 and run code / Tarayıcıda açın ve kodu çalıştırın.

Notes / Notlar
Python code is executed safely using a restricted environment.

C code requires GCC and JavaScript code runs using Node.js backend execution.

Output colors: green = normal output, red = errors.

Clear button resets both editor and output area.
