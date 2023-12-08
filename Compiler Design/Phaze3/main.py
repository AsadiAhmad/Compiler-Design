#Ahmad Asadi 99463107
#Golestan Mohammadi 97463150
from myLexer import *
from myParser import *

lexer = lex()
parser = yacc(debug = True)

test1 = """
class Ahmad {
    int th () {
        am = true;
        ie(k);
        if (im[5]) {
            a =10;
        }
    }
}
"""

test2 = """
class Golestan {
    void Ahmad () {
        int rpg = 10;
        while (true) {
            if (100 == bad) {
                while (id < 100) {
                    temp = temp + 1;
                }
            }
        }
    }
}
"""

test3 = """
class ahmad {
    private int h;
    public int ahmad (int h) {
        int h = 90;
        while (true) {
            shkila = false;
        }
        return 10;
    }
    public static int golestan (string len) {
        boolean h = true;
        if (a == c) {
            c = false;
            d = 10;
            if (temp <= 10) {
                temp = temp + 1;
            }
        }
    }
}
"""

test4 = """
class ak47 {
    ahmad = 98;
    while(true){
        mm();
    }
}
"""

test5 = """
class uzi {
    if (10 == 5 {
        h
    }
}

"""

ast = parser.parse(test4, debug = True)
print(ast)

if parser.errorok:
    print("compiled successfully")