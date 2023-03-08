from googletrans import Translator
class color:

        HEADER = f'\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        def Txt(type, txt):
            print(f"{type}{txt} {color.ENDC}", end='')
def doubt(txt):
    print("IHS Interactive Helping Sistem")
    translator = Translator()
    translation = translator.translate(txt, dest='pt')
    print(f"({translation.src}) {translation.origin}\n")
    print(color.Txt(color.HEADER, f"\nEm Português ({translation.dest})\n{translation.text}"))

txt = str(input().__doc__)
doubt(txt)