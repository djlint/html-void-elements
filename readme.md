# HtmlTagNames

Python port of npm package [html-void-elements](https://www.npmjs.com/package/html-void-elements).

List of known HTML tag names.

## What is this?

This is a list of HTML tag names.
It includes ancient (for example, `nextid` and `basefont`) and modern (for
example, `shadow` and `template`) names from the HTML living standard.
The repo includes scripts to regenerate the data from the specs.

## When should I use this?

You can use this package when you need to know what tag names are allowed in
any version of HTML.

## Install

```sh
pip install html-tag-names
```

## Use

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
## License

[GPL][license] © Riverside Healthcare
Ported from `html-void-elements` [MIT][license] © [Titus Wormer][author]

[license]: LICENSE