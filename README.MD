# 💸 Expense Management System

This project is an **Expense Management System** that consists of a user-friendly **Streamlit** frontend application and a powerful **FastAPI** backend server. This application helps users track and manage expenses efficiently, with a monthly and yearly breakdown for easy analysis. 📊

---

## 📂 Project Structure

- **`frontend/`**: Contains the Streamlit application code for the frontend interface.
- **`backend/`**: Contains the FastAPI backend server code for handling API requests.
- **`tests/`**: Contains the test cases for both frontend and backend to ensure stability.
- **`requirements.txt`**: Lists the required Python packages.
- **`README.md`**: Provides an overview and setup instructions for the project.

---

## 🚀 Key Features

- **Expense Tracking**: Record and categorize your expenses.
- **Monthly and Yearly Analytics**: Analyze expenses by month and year with easy visualizations.
- **User-friendly Interface**: Simple, intuitive design powered by Streamlit.
- **Robust Backend**: Efficient data handling and processing with FastAPI.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Nayan-2303/expense-management-system.git
cd expense-management-system
```

### 2. Install Dependencies

Ensure you have all necessary packages by running:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

#### Start the FastAPI Server
To start the backend server:
```bash
uvicorn backend.server:app --reload
```

#### Start the Streamlit App
To launch the frontend interface:
```bash
streamlit run frontend/app.py
```

---

## 🧩 Requirements

The following packages are required to run the Expense Management System. Make sure they are specified in your `requirements.txt` file:

```plaintext
streamlit==1.35.0
fastapi==0.112.2
pydantic==1.10.9
uvicorn==0.30.6
mysql-connector-python==8.0.33
pandas==2.0.2
requests==2.31.0
pytest==8.3.2
```

---

## 📞 Contact

For any questions or issues, please reach out to the [project owner](https://github.com/Nayan-2303) on GitHub.

---

### 🎉 Happy Expense Tracking!
