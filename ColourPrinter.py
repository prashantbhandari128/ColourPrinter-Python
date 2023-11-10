# +------------------------------------------------------------+ 
# | URL : https://cwoebker.com/posts/ansi-escape-codes         |
# | URL : https://www.nayab.xyz/linux/escapecodes              |
# +------------------------------------------------------------+

class ColourPrinter(object):
    # +-------------------------------------------------+
    # |    Format : ESC[{attr1};{attr2};....{attrn)m    |
    # +-------------------------------------------------+

    #ESCAPE = '\033[%sm'
    #ENDC = ESCAPE % '0'

    ESCAPE = '[%sm'
    ENDC = ESCAPE % '0'
    
    # ---------------[ Text Formatting ]--------------
    REGULAR = '0'
    BOLD = '1'
    LOW_INTENSITY = '2' # Not widely supported
    ITALIC = '3'
    UNDERLINE = '4'
    BLINKING = '5'
    REVERSE = '6' # Not widely supported
    BACKGROUND = '7'
    INVISIBLE = '8'
    # ------------------------------------------------

    # -----------------[ Text Colors ]----------------
    COLORS = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37'
    }
    # ------------------------------------------------

    # -------------[ Background Colors ]--------------
    BACKGROUND_COLORS = {
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'magenta': '45',
        'cyan': '46',
        'white': '47'
    }
    # ------------------------------------------------

    def __init__(self):
        pass

    def decorate(self, styleformat, message):
        totallength = len(styleformat)
        formatstring = ""
        for x in styleformat:
            if styleformat.index(x) == totallength - 1 :
                formatstring = formatstring + x 
            else:
                formatstring = formatstring + x + ";"  
        format_sequence = self.ESCAPE % formatstring
        return (format_sequence + message + self.ENDC)

    # EXAMPLE USE
    def print_red_bold_underline(self, message):
        style = [
            self.BOLD,
            self.UNDERLINE,
            self.COLORS['red']
        ]
        print(self.decorate(style, message))

c = ColourPrinter()
c.print_red_bold_underline("Sample Text")
