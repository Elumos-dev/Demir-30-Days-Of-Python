1. Open the page in your browser, right-click the data, choose **Inspect**, and note the tag (`table`, `tr`, `td`) and any `class`.
2. `soup.find('table', class_='wikitable')` targets one table by class. `class_` has an underscore because `class` is a Python keyword.
3. Print small pieces first (`print(table.find('tr'))`) before writing the loop.
4. The old UCI `datasets.php` page is gone. The list now lives at `https://archive.ics.uci.edu/datasets`.
