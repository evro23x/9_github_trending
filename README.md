# Тренды проекта Github

Cкрипт находит все репозитории на GitHub, созданные за последнюю неделю, выбирает 20 с наибольшим количеством звёзд и для каждого считает количество открытых issues. Затем выповодит их вместе со ссылками в консоль.

# Быстрый старт

Пример запуска скрипта в среде Linux, под Python 3.5:

```#!bash
$ python github_trending.py
```

# Пример запуска

```#!bash

$ python github_trending.py
Name: preact-cli
Stars: 1032
Issues: 30
Link: https://api.github.com/repos/developit/preact-cli

Name: wannakey
Stars: 888
Issues: 1
Link: https://api.github.com/repos/aguinet/wannakey

Name: whats-new-in-swift-4
Stars: 810
Issues: 1
Link: https://api.github.com/repos/ole/whats-new-in-swift-4

Name: ssh-mitm
Stars: 738
Issues: 1
Link: https://api.github.com/repos/jtesta/ssh-mitm

Name: from-java-to-kotlin
Stars: 596
Issues: 1
Link: https://api.github.com/repos/MindorksOpenSource/from-java-to-kotlin

Name: wanakiwi
Stars: 560
Issues: 4
Link: https://api.github.com/repos/gentilkiwi/wanakiwi

Name: chaos
Stars: 548
Issues: 30
Link: https://api.github.com/repos/chaosbot/chaos

Name: insights
Stars: 428
Issues: 4
Link: https://api.github.com/repos/mariusandra/insights

Name: android-architecture-counter-sample
Stars: 427
Issues: 4
Link: https://api.github.com/repos/dlew/android-architecture-counter-sample

Name: delaunator
Stars: 285
Issues: 2
Link: https://api.github.com/repos/mapbox/delaunator
```

# Цель проекта 

Код написан в целях обучения в рамках курса для веб-разработчиков - [DEVMAN.org](https://devman.org)
