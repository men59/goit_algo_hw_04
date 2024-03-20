def get_cats_info(path):
    try:
    #path = "cats_file.txt"
        with open(path, "r", encoding= 'UTF-8') as fh:
            cats_info = []
            lines = [el.strip() for el in fh.readlines()]
            for line in lines:
             part = line.split(',')
            cats_info.append({ "id": part[0], "name": part[1], "age": part[2]})
            return cats_info
    except FileNotFoundError:
        print("Файл не знайдено")
cats_info = get_cats_info("cats_file.txt")
print(cats_info)
