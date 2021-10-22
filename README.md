# zbase32

A human-oriented base-32 encoding.

## 🛠 Installing

## poetry

```
poetry add python-zbase32
```

## pip

```
pip install python-zbase32
```

## 🎓 Usage

```pycon
>>> import zbase32
>>> zbase32.encode(b"asdasd")
'cf3seamuco'
>>> zbase32.decode("cf3seamu")
b"asdas"
```

## 🔧  Development

| Command           | Description                           |
| ----------------- | ------------------------------------- |
| `make bootstrap`  | install project dependencies          |
| `make ci`         | run continuous integration tasks      |
| `make console`    | open a repl console                   |
| `make format`     | format all source files               |
| `make setup`      | setup the project after a `git clone` |
| `make test`       | run the applications test suite       |
| `make update`     | update the project after a `git pull` |

## ⚖️ Licence

This project is licensed under the [MIT licence](http://dan.mit-license.org/).

All documentation and images are licenced under the 
[Creative Commons Attribution-ShareAlike 4.0 International License][cc_by_sa].

[cc_by_sa]: https://creativecommons.org/licenses/by-sa/4.0/

## 📝 Meta

This project uses [Semantic Versioning](http://semver.org/).