# 🎉 CycleSenseAI


---

## 🚀 Project Overview
**CycleSenseAI** is a smart period tracker featuring a sleek, user-friendly GUI built with **CustomTkinter**. It uses an **LSTM** model to predict the next cycle date accurately and offers multiple features including different modes and an embedded chatbot for personalized assistance. The backend is securely powered by **Supabase**, supporting user authentication and data management.

---

## ✨ Features
- 🖥️ CustomTkinter-based intuitive GUI  
- 🔮 LSTM model for next cycle date prediction  
- 🤖 Embedded chatbot for cycle-related assistance  
- 🔒 Secure login and data storage via Supabase  
- ⚙️ Multiple user modes for personalized tracking  

---

## 🛠️ Tech Stack

| 🔧 Category       | 🛠️ Technologies Used                                  |
|-------------------|------------------------------------------------------|
| 🐍 Programming    | Python 3.10+                                         |
| 🎨 GUI            | CustomTkinter                                        |
| 🤖 Machine Learning| LSTM (PyTorch / TensorFlow)                          |
| 💬 NLP / Chatbot  | Custom chatbot embedding                             |
| ☁️ Backend         | Supabase (PostgreSQL, Authentication)                |
| 📊 Data Handling  | Dataset from Kaggle ([Menstrual Cycle Data](https://www.kaggle.com/datasets/nikitabisht/menstrual-cycle-data)) |
| 📁 Files          | Trained model weights (`.pth`), datasets in `/dataset` folder |

---

## 🗂️ Project Structure

```plaintext
## 🗂️ Project Structure

```plaintext
CycleSenseAI/
│
├── images_used/             # All UI images and assets used in the app
├── dataset/                 # Kaggle dataset and preprocessed files
├── models/                  # Trained LSTM `.pth` model files
├── main.py                  # Main application entry point (runs the full app)
├── gui.py                   # GUI components (CustomTkinter main interface)
├── chatbot.py               # Chatbot embedding and logic
├── database.py              # Supabase backend integration and authentication
├── first_page.py            # Initial GUI page (welcome/get started)
├── forgotpassword.py        # GUI and logic for 'Forgot Password' feature
├── getstarted.py            # First entry page for new users
├── login.py                 # Login GUI and credential handling
├── phase_calculation.py     # Logic for menstrual phase calculation
├── signup.py                # Signup GUI and logic for new accounts
├── bot2.py                  # Chatbot GUI and interaction logic
├── insights.py              # Main dashboard: date prediction, mood selection, articles
├── tracker.py               # Calendar GUI, LSTM input setup for predictions
├── modellstm.py             # LSTM model definition and loading
├── requirements.txt         # Python dependencies
└── README.md                # This file



```
## 📩 Contact

**👩‍💻 Dure Adan Noor**  
📧 Email: [dureadannoor88@gmail.com](mailto:dureadannoor88@gmail.com)  
🔗 LinkedIn: [www.linkedin.com/in/dure-adan-noor-29b01b2b5](https:linkedin.com/in/dure-adan-noor-29b01b2b5)

---
