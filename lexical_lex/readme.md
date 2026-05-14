flex lexer.l
<!-- gcc lex.yy.c -o lexer -ll -->
gcc lex.yy.c -o lexer -lfl
./lexer < input.txt