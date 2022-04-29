# Scrapper

##Struktura opinii w serwisie Ceneo [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|user-post|obj|
|indentyfikator opinii|div.js_product-review["data-entry-id"\]|data_entry_id|str|
|autor opinii|span.user-post__author-name|str|
|rekomendacja|span.user-post__author-recomendation > em|str|
|liczba gwiazdek|span.user-post__score-count|user-post__score_count|string|
|treść opinii|div.user-post__text|user-post__text|string|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item|review-feature__col|list|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item|list|
|dla ilu osób przydatna|button.vote-yes > span|votes-yes-id|str|
|dla ilu osób nieprzydatna|button.vote-no > span|votes-no-id|str|
|data wystawienie opinii|span.user-post__published > time:nth-child(1)["datetime"]|user-post__published|str|
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|bought|str| 