# 🧠 Sentiment Analysis Web App

This is a simple web application built using **Flask** and **TextBlob** to analyze the sentiment of user-inputted text. The app classifies the input as **Positive**, **Negative**, or **Neutral**, and shows the corresponding sentiment probability.

## 🚀 Features

- Web-based interface to enter and analyze text
- Uses `TextBlob` for sentiment analysis
- Displays:
  - Sentiment type (😊 Positive / 😠 Negative / 😐 Neutral)
  - Sentiment polarity probability
  - Subjectivity score (optional)

## 🛠️ Technologies Used

- Python 🐍
- Flask 🌐
- TextBlob 📦
- HTML5 & CSS3 🧾

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nkale882/Sentiment_Analysis.git
   cd sentiment-analysis-flask
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or manually:
   ```bash
   pip install flask textblob
   python -m textblob.download_corpora
   ```

## ▶️ Running the App

```bash
python app.py
```

Then open your browser and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 📁 Project Structure

```
sentiment-analysis-flask/
│
├── templates/
│   └── index.html       # Frontend form and result display
│
├── static/
│   └── css/
│       └── style.css    # (Optional) Styling
│
├── app.py               # Flask application
└── README.md            # Project documentation
```

## 📊 Example

Input:
```
I love the way this app works!
```

Output:
```
Sentiment: 😊 Positive
Sentiment Probability: 0.625
```
<img width="500" height="600" alt="image" src="https://github.com/user-attachments/assets/39c85160-5254-4277-9143-9275827b2fc9" />
<img width="500" height="600" alt="image" src="https://github.com/user-attachments/assets/d35babce-49c5-4aca-8634-3436ee200254" />
<img width="500" height="600" alt="image" position=center src="https://github.com/user-attachments/assets/7d132280-93be-4488-bc7b-d1710d2d3a2c" />

## 🧪 Troubleshooting

- Always check if `TextBlob` corpora are downloaded:
  ```bash
  python -m textblob.download_corpora
  ```
- Adjust sentiment thresholds if your model is too strict or lenient.

## 📃 License

MIT License

---

Made with ❤️ using Flask and TextBlob.

