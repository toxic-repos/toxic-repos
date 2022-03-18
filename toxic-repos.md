# В этом файле в человекочитаемом виде представлен список проектов с закладками
[Данные из этого файла в машиночитаемом виде](./projects.json)

## es5-ext
Уровень опасности: LOW  
Критерий атаки: TZ_RU  
Источник: SRC   
Закладка в коде проекта в файле [_postinstall.js](https://github.com/medikoo/es5-ext/blob/main/_postinstall.js)   
Вывод агиток и незначительный сабботаж собственной работы  
Срабатывает в следующих часовых поясах  
"Europe/Moscow", "Asia/Yakutsk", "Asia/Krasnoyarsk", "Europe/Samara", "Asia/Yekaterinburg", "Asia/Irkutsk", "Asia/Anadyr", "Asia/Kamchatka", "Europe/Kaliningrad", "Asia/Vladivostok", "Asia/Magadan", "Asia/Novosibirsk", "Asia/Omsk"  
Ответвенный контрибьютор [medikoo](https://github.com/medikoo)  

## AWS Terraform modules
Уровень опасности: HIGH  
Критерий атаки: UNKNOWN  
Источник: SRC   
Все модули AWS для Terraform поддерживаемые сообществом, также сдублировалось в официальный Registry  
Шифровальщик системы  
Закладка внедрена лично мейнтейнером [antonbabenko](https://github.com/antonbabenko)  
Также в условия лицензии добавлен пункт о том что используя данный код вы соглашаетесь с полит позицией атвора.  

## rete
Уровень опасности: LOW  
Критерий атаки: NONE   
Источник: SRC   
Печать агитки после установки  
Внедрено [Ni55aN](https://github.com/Ni55aN) в коммите [d3ff828a41f96e34f04](https://github.com/retejs/rete/commit/d3ff828a41f96e34f04619eb44c688c913ee8def)  

## PHP composer 
Уровень опасности: LOW  
Критерий атаки: NONE  
Источник: SRC   
Пакетный менеджер PHP добавляет бейдж StandWithUkraine  
Внедрено [Seldaek](https://github.com/Seldaek) в коммите [86244a3695fcaaac9c](https://github.com/composer/packagist/commit/86244a3695fcaaac9c5ba4257a4314eae1c6d981)  

## PHPUnit
Уровень опасности: LOW  
Критерий атаки: NONE  
Источник: SRC   
Показывает бейдж StandWithUkraine  
Внедрено [sebastianbergmann](https://github.com/sebastianbergmann) в коммите [4634e702b5f05f5e](https://github.com/sebastianbergmann/phpunit/commit/4634e702b5f05f5e948e531eb8b4fc19be40610c)  

## Tasmota
Уровень опасности: HIGH   
Критерий атаки: KM_RU POS_RU POS_BY
Источник: SRC   
Закладка в прошивке для ESP8266 и ESP32  
Должна показывать сообщение StandWithUkraine но с некоторым шансом окирпичивает устройтсво, по видимому из а бага в закладке  
Внедрено [arendst](https://github.com/arendst) в коммите [98cbf2587a1a91](https://github.com/arendst/Tasmota/commit/98cbf2587a1a914bbd16996ebb48dd451d3da448)  



