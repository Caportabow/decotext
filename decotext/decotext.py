from evals import ALPHABET, Fonts

class DecoText:
    @staticmethod
    def mono(text: str):
        """
        Example: 𝙷𝚎𝚕𝚕𝚘 𝚆𝚘𝚛𝚕𝚍!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.MONO))

    @staticmethod
    def serif_bold(text: str):
        """
        Example: 𝐇𝐞𝐥𝐥𝐨 𝐖𝐨𝐫𝐥𝐝!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.SERIF_BOLD))

    @staticmethod
    def italic(text: str):
        """
        Example: 𝐻𝑒𝑙𝑙𝑜 𝑊𝑜𝑟𝑙𝑑!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.ITALIC))

    @staticmethod
    def bold_italic(text: str):
        """
        Example: 𝑯𝒆𝒍𝒍𝒐 𝑾𝒐𝒓𝒍𝒅!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.BOLD_ITALIC))

    @staticmethod
    def sans(text: str):
        """
        Example: 𝖧𝖾𝗅𝗅𝗈 𝖶𝗈𝗋𝗅𝖽!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.SANS))

    @staticmethod
    def sans_bold(text: str):
        """
        Example: 𝗛𝗲𝗹𝗹𝗼 𝗪𝗼𝗿𝗹𝗱!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.SANS_BOLD))

    @staticmethod
    def sans_italic(text: str):
        """
        Example: 𝘏𝘦𝘭𝘭𝘰 𝘞𝘰𝘳𝘭𝘥!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.SANS_ITALIC))

    @staticmethod
    def sans_bold_italic(text: str):
        """
        Example: 𝙃𝙚𝙡𝙡𝙤 𝙒𝙤𝙧𝙡𝙙!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.SANS_BOLD_ITALIC))

    @staticmethod
    def script(text: str):
        """
        Example: ℋℯ𝓁𝓁ℴ 𝒲ℴ𝓇𝓁𝒹!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.SCRIPT))

    @staticmethod
    def script_bold(text: str):
        """
        Example: 𝓗𝓮𝓵𝓵𝓸 𝓦𝓸𝓻𝓵𝓭!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.SCRIPT_BOLD))

    @staticmethod
    def fraktur(text: str):
        """
        Example: 𝔍𝔢𝔩𝔩𝔬 𝔚𝔬𝔯𝔩𝔡!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.FRAKTUR))

    @staticmethod
    def fraktur_bold(text: str):
        """
        Example: 𝕳𝖊𝖑𝖑𝖔 𝖂𝖔𝖗𝖑𝖉!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.FRAKTUR_BOLD))

    @staticmethod
    def circled(text: str):
        """
        Example: Ⓗⓔⓛⓛⓞ Ⓦⓞⓡⓛⓓ!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.CIRCLED))

    @staticmethod
    def fullwidth(text: str):
        """
        Example: Ｈｅｌｌｏ Ｗｏｒｌｄ!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.FULLWIDTH))

    @staticmethod
    def double_struck(text: str):
        """
        Example: ℍ𝕖𝕝𝕝𝕠 𝕎𝕠𝕣𝕝𝕕!
        """
        return text.translate(str.maketrans(ALPHABET, Fonts.DOUBLE_STRUCK))

print(__name__)
if __name__ == "__main__":
    text = "Hello World!"
    print(DecoText.mono(text))
    print(DecoText.serif_bold(text))
    print(DecoText.italic(text))
    print(DecoText.bold_italic(text))
    print(DecoText.sans(text))
    print(DecoText.sans_bold(text))
    print(DecoText.sans_italic(text))
    print(DecoText.sans_bold_italic(text))
    print(DecoText.script(text))
    print(DecoText.script_bold(text))
    print(DecoText.fraktur(text))
    print(DecoText.fraktur_bold(text))
    print(DecoText.circled(text))
    print(DecoText.fullwidth(text))
    print(DecoText.double_struck(text))
