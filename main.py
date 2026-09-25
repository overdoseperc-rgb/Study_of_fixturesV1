from strings import string_length, save_string

if __name__ == "__main__":
    text = "Привет!\nИзучаем фикстуры pytest."
    print("Длина:", string_length(text))
    print("Сохранено:", save_string(text, "string.txt").resolve())
