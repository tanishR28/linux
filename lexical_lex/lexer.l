%{
#include<stdio.h>
%}

%%

int|if|else|while|for|switch {
    printf("%s : KEYWORD\n", yytext);
}

[a-zA-Z_][a-zA-Z0-9_]* {
    printf("%s : IDENTIFIER\n", yytext);
}

[0-9]+ {
    printf("%s : INTEGER\n", yytext);
}

[+\-*/=><] {
    printf("%s : OPERATOR\n", yytext);
}

[ \t\n] ;

. {
    printf("%s : INVALID\n", yytext);
}

%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("TOKEN\t\tTYPE\n\n");
    yylex();
    return 0;
}