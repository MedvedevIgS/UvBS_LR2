## Программа по нахождению кратчайшего пути
#### Библиотеки: PyQt6, graphviz

### Пользователь задает размер матрицы смежности (Матица показывающая из какой в какую вершину идет дуга)
>Он может сделать это как вручную, указав количество вершин и заполнить её сам

>![This is an image](https://github.com/MedvedevIgS/UvBS_LR2/blob/master/README%20img/1.png)

>Так и загрузив ее из заранее подготовленного `.txt` файла

>![This is an image](https://github.com/MedvedevIgS/UvBS_LR2/blob/master/README%20img/2.png)

>![This is an image](https://github.com/MedvedevIgS/UvBS_LR2/blob/master/README%20img/3.png)

### Существует возможность добавлять и удалять вершины
>Для этого нужно нажать в таблице на соответсвующую вершину и затем нажать кнопку "Удалить вершину"

>![This is an image](https://github.com/MedvedevIgS/UvBS_LR2/blob/master/README%20img/4.png)

>Для добавления вершины необходимо нажать кнопку "Добавить вершину", чего в таблицу будет добавлена вершина

>![This is an image](https://github.com/MedvedevIgS/UvBS_LR2/blob/master/README%20img/5.png)

### После того как матрица была задана пользователь получить графическое представления графа

>При нажатии на кнопку "Расчет графа" Программа по заданной матрице смежности орграфа (ориентированного графа) строит
>его графическое представления:

>![This is an image](https://github.com/MedvedevIgS/UvBS_LR2/blob/master/README%20img/6.png)

>- Неупорядоченный граф

>![This is an image](https://github.com/MedvedevIgS/UvBS_LR2/blob/master/README%20img/7.png)

>- Упорядоченный граф, где вершины распределены по уровням

>![This is an image](https://github.com/MedvedevIgS/UvBS_LR2/blob/master/README%20img/8.png)

### Пользователь может указать из какой в какую вершину он хочет получить кратчайший путь и при нажати на кнопку "Найти" на графе красным цветом помечаются все кратчайшие и в виде текста внизу отображается какждый путь и его длина

>![This is an image](https://github.com/MedvedevIgS/UvBS_LR2/blob/master/README%20img/9.png)
