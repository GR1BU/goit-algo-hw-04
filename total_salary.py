def total_salary(path):
    try:
        with open(path, encoding="utf-8") as file:
            lines = file.readlines()
        
        salaries = []

        for line in lines:
            name_num = line.strip().split(",")
            salary = int(name_num[1])
            salaries.append(salary)

        total = sum(salaries)
        average = total / len(salaries)

        return total, average

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0

    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0
