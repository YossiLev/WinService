# 🔦 Windows service installation App

A Python-based app for installing new services into Windows

## 🚀 Features


## 📦 Installation

```bash
# clone the repo
git clone https://github.com/YossiLev/winservice

# navigate into the project folder
cd winservice

# (Optional) Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install pywin32
```

## ▶️ Activation
Make the following changes in main.py to fit the name and location of your uvicorn program

    _svc_name_ = "MyUvicornService"
    _svc_display_name_ = "Uvicorn FastAPI Service"
    _svc_description_ = "Runs a Uvicorn server as a Windows service"
    base_dir = r"C:\path\to\your\project"

Also change information about the inforation about how you want to run uvicorn (port, host, etc...)
    uvicorn_cmd = [
        sys.executable, "-m", "uvicorn",
        "app:app",
        "--host", "0.0.0.0",
        "--port", "8000"
    ]


```bash
python main.py install
#or (in order to install as automatic start)
python main.py --startup auto install

python main.py start

```

## 📁 Project Structure
```
winservice/
├── main.py                             # Uvicorn entry point
└── README.md
```

## 📄 License
Copyright (c) 2024-2025, Bar Ilan University, Prof. Avi Pe'er Lab

This project is licensed under the [MIT License](https://opensource.org/license/mit).

## 🙋‍♂️ Contact
For questions or feedback, feel free to contact me at **yossi.lev.home@gmail.com**.