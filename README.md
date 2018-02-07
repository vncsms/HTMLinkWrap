# Link wrap
Find words in html file and wrap with links

## Requisit:
First needs `BeautifulSoup` installed: You can install via pip:

`pip install beautifulsoup4==4.6.0`

Or just 

`pip install beautifulsoup4`


## Files:
You need a input file `mypage.hmtl`:

```hmtl
<body>
The apple tree (Malus pumila, commonly and erroneously called Malus domestica) is a deciduous
tree in the rose family best known for its sweet, pomaceous fruit, the apple. It is cultivated
worldwide as a fruit tree, and is the most widely grown species in the genus Malus. The tree
originated in Central Asia, where its wild ancestor, Malus sieversii, is still found today.
Apples have been grown for thousands of years in Asia and Europe, and were brought to North
America by European colonists. Apples have religious and mythological significance in many
cultures, including Norse, Greek and European Christian traditions.
</body>
```
> This file don't need be a html or contains html elements file but the output will be.

> The text is the first paragraph of https://en.wikipedia.org/wiki/Apple

Now you needs a file `links.txt` that contains the links ans the words:


```
https://en.wikipedia.org/wiki/Apple Apple
https://en.wikipedia.org/wiki/Tree Tree
https://en.wikipedia.org/wiki/Asia Asia
https://en.wikipedia.org/wiki/North_America North America
```
> The file must have this format: url word.

> The both files can have whatever name you want.

## Executing:
Activate you virtualenv enviroment and execute:


`python wraplinker.py mypage.hmtl output.hmtl links.txt`

> 1º Argument: your input file, 2º Argument: your output file, 3º Argument: words and links file

OutPut:

```hmtl
<body>
The <a data-cke-saved-href="https://en.wikipedia.org/wiki/Apple" href="https://en.wikipedia.org/wiki/Apple" target=""> apple</a> <a data-cke-saved-href="https://en.wikipedia.org/wiki/Tree" href="https://en.wikipedia.org/wiki/Tree" target=""> tree</a> (Malus pumila, commonly and erroneously called Malus domestica) is a deciduous tree in the rose family best known for its sweet, pomaceous fruit, the apple. It is cultivated worldwide as a fruit tree, and is the most widely grown species in the genus Malus. The tree originated in Central <a data-cke-saved-href="https://en.wikipedia.org/wiki/Asia" href="https://en.wikipedia.org/wiki/Asia" target=""> Asia</a>, where its wild ancestor, Malus sieversii, is still found today. Apples have been grown for thousands of years in Asia and Europe, and were brought to <a data-cke-saved-href="https://en.wikipedia.org/wiki/North_America" href="https://en.wikipedia.org/wiki/North_America" target=""> North America</a> by European colonists. Apples have religious and mythological significance in many cultures, including Norse, Greek and European Christian traditions.
</body>
```

Or:

<body>
The <a data-cke-saved-href="https://en.wikipedia.org/wiki/Apple" href="https://en.wikipedia.org/wiki/Apple" target=""> apple</a> <a data-cke-saved-href="https://en.wikipedia.org/wiki/Tree" href="https://en.wikipedia.org/wiki/Tree" target=""> tree</a> (Malus pumila, commonly and erroneously called Malus domestica) is a deciduous tree in the rose family best known for its sweet, pomaceous fruit, the apple. It is cultivated worldwide as a fruit tree, and is the most widely grown species in the genus Malus. The tree originated in Central <a data-cke-saved-href="https://en.wikipedia.org/wiki/Asia" href="https://en.wikipedia.org/wiki/Asia" target=""> Asia</a>, where its wild ancestor, Malus sieversii, is still found today. Apples have been grown for thousands of years in Asia and Europe, and were brought to <a data-cke-saved-href="https://en.wikipedia.org/wiki/North_America" href="https://en.wikipedia.org/wiki/North_America" target=""> North America</a> by European colonists. Apples have religious and mythological significance in many cultures, including Norse, Greek and European Christian traditions.
</body>

> Only the first word will be wraped

