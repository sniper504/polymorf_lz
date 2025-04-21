from cleaner import DeleteDuplicates, SplitByOperation

def main():
    df_path = "var2.csv"
    
    # Удаляем дубликаты через `~`
    cleaner = DeleteDuplicates(df_path)
    cleaner = ~cleaner  # Используем `__invert__`
    
    cleaned_data = cleaner.data
    cleaned_data.to_csv("cleaned_var2.csv", index=False)
    print("Удалены дубликаты, сохранено как cleaned_var2.csv")
    print(f"Удалено {cleaner.removed_rows} повторяющихся строк")
    
    # Разделяем датасет по типу операции через `~`
    splitter = SplitByOperation("cleaned_var2.csv")
    separated_files = ~splitter  # Вызываем `__invert__`

    for operation, filename in separated_files.items():
        print(f"Сохранен файл: {filename} (Тип операции: {operation})")

if __name__ == "__main__":
    main()






