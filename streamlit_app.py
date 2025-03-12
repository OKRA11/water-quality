import streamlit as st
import joblib
import numpy as np

# Загрузка модели
model = joblib.load('model.pkl')

# Настройка фона и стилей с помощью CSS
st.markdown(
    """
    <style>
    /* Основной фон */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        font-family: 'Arial', sans-serif;
    }

    /* Стиль заголовка */
    h1 {
        color: #2c3e50;
        text-align: center;
        font-size: 3em;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }

    /* Стиль кнопки */
    .stButton>button {
        background-color: #2980b9;
        color: white;
        border-radius: 8px;
        font-size: 1.2em;
        padding: 10px 20px;
        transition: transform 0.2s ease-in-out;
    }

    /* Анимация кнопки при наведении */
    .stButton>button:hover {
        background-color: #3498db;
        transform: scale(1.05);
    }

    /* Улучшение полей ввода */
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 1px solid #ccc;
        padding: 10px;
        font-size: 1em;
    }

    /* Успешное сообщение */
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
        border-radius: 8px;
        padding: 15px;
        font-size: 1.2em;
        text-align: center;
        margin-top: 20px;
    }

    /* Сообщение об ошибке */
    .stError {
        background-color: #f8d7da;
        color: #721c24;
        border-radius: 8px;
        padding: 15px;
        font-size: 1.2em;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Заголовок приложения
st.title("Качество воды")

# Ввод параметров
ph = st.number_input("pH: значение рН воды (от 0 до 14)", min_value=0.0, max_value=14.0, step=0.1)
hardness = st.number_input("Жесткость (мг/л)", min_value=0.0)
solids = st.number_input("Содержание твердых веществ (млн/долей)", min_value=0.0)
chloramines = st.number_input("Хлорамины (млн/долей)", min_value=0.0)
sulfate = st.number_input("Сульфат (мг/л)", min_value=0.0)
conductivity = st.number_input("Электропроводность", min_value=0.0)
organic_carbon = st.number_input("Органический углерод (млн/долей)", min_value=0.0)
trihalomethanes = st.number_input("Тригалометаны", min_value=0.0)
turbidity = st.number_input("Turbidity", min_value=0.0)

# Кнопка для предсказания
if st.button("Проверить пригодность воды"):
    # Подготовка входных данных для модели
    input_data = np.array(
        [[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])

    # Получение предсказания
    prediction = model.predict(input_data)

    # Вывод результата
    if prediction[0] == 1:
        st.success("Вода пригодна!")
    else:
        st.error("Вода не пригодна!")
