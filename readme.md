<h1 align="center">HTML Void Elements</h1>

<h4 align="center">List of known HTML void tag names.</h4>

<h5 align="center">Python port of npm package <a href="https://www.npmjs.com/package/html-void-elements" target="_blank">html-void-elements</a>.</h5>

<p align="center">
  <a href="https://pypi.org/project/html-void-elements/">
    <img src="https://badgen.net/pypi/v/html-void-elements" alt="Pypi Version">
  </a>
  <a href="https://pepy.tech/project/html-void-elements">
    <img src="https://static.pepy.tech/badge/html-void-elements" alt="Downloads">
  </a>
</p>

## 🤔 What is this?

This is a list of HTML void tag names.

## ⌚ When should I use this?

You can use this package when you need to know what void tag names are allowed in
any version of HTML.

## 💾 Install

```sh
pip install html-void-elements

# or

poetry add html-void-elements
```

## ✨ How to Use

```py
from HtmlVoidElements import html_void_elements

print(html_void_elements)
```

Yields:

```py
[
  'area',
  'base',
  'basefont',
  'bgsound',
  'br',
  'col',
  'command',
  'embed',
  'frame',
  'hr',
  'image',
  'img',
  'input',
  'isindex',
  'keygen',
  'link',
  'menuitem',
  'meta',
  'nextid',
  'param',
  'source',
  'track',
  'wbr'
]
```
## 🪪 License

- [GPL][license] © Riverside Healthcare
- Ported from `html-void-elements` [MIT][license] © [Titus Wormer](https://github.com/wooorm)

[license]: LICENSE
