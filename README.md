# DecoText

**DecoText** is a lightweight Python library to generate decorative text using Unicode.  
Turn plain text into stylish fonts with just a single function call!

---

## Features

- Multiple text styles: mono, serif, italic, bold, script, fraktur, circled, fullwidth, double-struck, and more.
- Simple and fast: one import and one method call.
- Full Python 3 support.

---

## Installation

Clone the repository and install the package in editable mode:

```bash
git pull https://github.com/Caportabow/decotext
pip install -e decotext/
```

Or, if it becomes available on PyPI:

```bash
pip install decotext
```

---

## Usage

```python
from decotext import DecoText as dt

text = "Hello World!"

print(dt.mono(text))
# 𝙷𝚎𝚕𝚕𝚘 𝚆𝚘𝚛𝚕𝚍!

print(dt.serif_bold(text))
# 𝐇𝐞𝐥𝐥𝐨 𝐖𝐨𝐫𝐥𝐝!

print(dt.italic(text))
# 𝐻𝑒𝑙𝑙𝑜 𝑊𝑜𝑟𝑙𝑑!

print(dt.bold_italic(text))
# 𝑯𝒆𝒍𝒍𝒐 𝑾𝒐𝒓𝒍𝒅!

print(dt.sans(text))
# 𝖧𝖾𝗅𝗅𝗈 𝖶𝗈𝗋𝗅𝖽!

print(dt.sans_bold(text))
# 𝗛𝗲𝗹𝗹𝗼 𝗪𝗼𝗿𝗹𝗱!

print(dt.sans_italic(text))
# 𝘏𝘦𝘭𝘭𝘰 𝘞𝘰𝘳𝘭𝘥!

print(dt.sans_bold_italic(text))
# 𝙃𝙚𝙡𝙡𝙤 𝙒𝙤𝙧𝙡𝙙!

print(dt.script(text))
# ℋℯ𝓁𝓁ℴ 𝒲ℴ𝓇𝓁𝒹!

print(dt.script_bold(text))
# 𝓗𝓮𝓵𝓵𝓸 𝓦𝓸𝓻𝓵𝓭!

print(dt.fraktur(text))
# 𝔍𝔢𝔩𝔩𝔬 𝔚𝔬𝔯𝔩𝔡!

print(dt.fraktur_bold(text))
# 𝕳𝖊𝖑𝖑𝖔 𝖂𝖔𝖗𝖑𝖉!

print(dt.circled(text))
# Ⓗⓔⓛⓛⓞ Ⓦⓞⓡⓛⓓ!

print(dt.fullwidth(text))
# Ｈｅｌｌｏ Ｗｏｒｌｄ!

print(dt.double_struck(text))
# ℍ𝕖𝕝𝕝𝕠 𝕎𝕠𝕣𝕝𝕕!
```

---

## Supported Styles

| Style | Example |
| :--- | :--- |
| **Mono** | 𝙷𝚎𝚕𝚕𝚘 𝚆𝚘𝚛𝚕𝚍! |
| **Serif Bold** | 𝐇𝐞𝐥𝐥𝐨 𝐖𝐨𝐫𝐥𝐝! |
| **Italic** | 𝐻𝑒𝑙𝑙𝑜 𝑊𝑜𝑟𝑙𝑑! |
| **Bold Italic** | 𝑯𝒆𝒍𝒍𝒐 𝑾𝒐𝒓𝒍𝒅! |
| **Sans** | 𝖧𝖾𝗅𝗅𝗈 𝖶𝗈𝗋𝗅𝖽! |
| **Sans Bold** | 𝗛𝗲𝗹𝗹𝗼 𝗪𝗼𝗿𝗹𝗱! |
| **Sans Italic** | 𝘏𝘦𝘭𝘭𝘰 𝑊𝘰ｒ𝑙𝘥! |
| **Sans Bold Italic** | 𝙃𝙚𝙡𝙡𝙤 𝙒𝙤𝙧𝙡𝙙! |
| **Script** | ℋℯ𝓁𝓁ℴ 𝒲ℴ𝓇𝓁𝒹! |
| **Script Bold** | 𝓗𝓮𝓵𝓵𝓸 𝓦𝓸 r𝓵𝓭! |
| **Fraktur** | 𝔍𝔢𝔩𝔩𝔬 𝔚𝔬𝔯𝔩𝔡! |
| **Fraktur Bold** | 𝕳𝖊𝖑𝖑𝖔 𝖂𝖔𝖗𝖑𝖉! |
| **Circled** | Ⓗⓔⓛⓛⓞ Ⓦⓞⓡⓛⓓ! |
| **Fullwidth** | Ｈｅｌｌｏ Ｗｏｒｌｄ! |
| **Double Struck** | ℍ𝕖𝕝𝕝𝕠 𝕎𝕠𝕣𝕝𝕕! |

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
