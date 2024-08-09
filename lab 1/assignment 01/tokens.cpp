#include<bits/stdc++.h>
#include<stdio.h>
#include<conio.h>
#include<ctype.h>
#include<string.h>
#include<stdlib.h>
using namespace std;

stack<char>st;
stack<string>mul_com;
set<string>paren_string , constant_string , keyword_string , iden_string ;
set<char>arith_string, pun_string;

int com , paren_count , mul_com_count , mul_flag;
char pun[] = ";:,";
int keyword_library(char temp[])
{
    int count = 0, flag = 0;
    char keywords[32][12] = {"return", "continue", "extern", "static", "long", "signed",
                             "switch", "char", "else", "unsigned", "if", "struct",
                             "union", "goto", "while", "float", "enum", "sizeof", "double", "volatile",
                             "const", "case", "for", "break", "void", "register", "int",
                             "do", "default", "short", "typedef", "auto"
                            };
    while (count <= 31)
    {
        if (strcmp(keywords[count], temp) == 0)
        {
            flag = 1;
            break;
        }
        count = count + 1;
    }
    return (flag);
}

int const_library(char temp[]) {
    int count = 0 , i = 0 ,  flag = 0 ;
    char constant [] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    int size = 0 ;
    while (temp[size] != '\0') {
        size++;
    }
    while (temp[i] != '\0') {
        count = 0 ;
        while (count < 10) {
            if (constant[count] == temp[i]) {
                flag++;

                break;
            }
            count += 1 ;
        }
        i++;
    }
    if (flag == size)
        return 1 ;
    return 0 ;
}

void paren_library(char ch) {
    if (ch == '(' || ch == '{' || ch == '[') {
        st.push(ch);
    }
    else if (ch == ')' || ch == '}' || ch == ']') {
        if (!st.empty()) {
            if (ch == ')' && st.top() == '(')paren_string.insert("()");
            else if (ch == '}' && st.top() == '{')paren_string.insert("{}");
            else if (ch == ']' && st.top() == '[')paren_string.insert("[]");
            st.pop();
        }
    }
}


void display() {
    printf("\n");

    printf("\nkeywords (%d) : ", keyword_string.size());
    for (auto i : keyword_string)cout << i << " ";
    printf("\n");

    printf("\nidentifier (%d) : ", iden_string.size());
    for (string i : iden_string)cout << i << ' ';
    printf("\n");

    printf("\nArithmetic (%d): ", arith_string.size());
    for (auto i : arith_string)cout << i << " ";
    printf("\n");

    printf("\nconstant (%d): ", constant_string.size());
    for (auto i : constant_string)cout << i << " ";
    printf("\n");

    printf("\npunctuation (%d): ", pun_string.size());
    for (auto i : pun_string)cout << i << ' ';
    printf("\n");

    printf("\nparenthesis (%d): ", paren_string.size());
    for (auto i : paren_string)cout << i << ' ';
    printf("\n\n");


    //printf("\nSingle Comment count : %d\n", com);
    //printf("\nMultiple Comment count: %d\n", mul_com_count);


}

int x ;


int main()
{
    char ch, temp[40], arithmetic_operator[] = "=+%*/-" , pun[] = ";:,";
    FILE *file_pointer;
    int count;
    x = 0;
    file_pointer = fopen("input.txt", "r");
    if (file_pointer == NULL)
    {
        printf("The file could not be opened.\n");
        exit(0);
    }
    int com_flag = 0 , log_flag = 0 ;
    char comment , log = '$' ;
    while ((ch = fgetc(file_pointer)) != EOF)
    {
        // here is update comment .......
        if (ch == '*' && !mul_com.empty()) {
            mul_flag++;
            continue;
        }
        if (mul_flag > 0 && ch == '/') {
            mul_flag = 0 ;
            com_flag = 0 ;
            mul_com_count++;
            mul_com.pop();
        }
        if (ch == '/')
        {
            com_flag++; //2
            if (com_flag == 1)
            {
                comment = '/';
                continue;
            }
        }
        if (com_flag == 1)
        {
            if (ch == '*') {
                mul_com.push("/*");
                continue;
            }
            else {
                arith_string.insert(comment);
                comment =  NULL;
                com_flag = 0 ;
            }
        }
        else if (com_flag == 2 && ch == '\n')
        {
            com_flag = 0 ;
            comment = NULL;
            com++;
            continue;
        }
        else if (com_flag == 2)continue;

        if (ch == '(' || ch == ')' || ch == '{' || ch == '}' || ch == '[' || ch == ']') {
            paren_library(ch);
            continue;
        }

        count = 0;
        while (count <= 5)
        {
            if (ch == arithmetic_operator[count])
            {
                arith_string.insert(ch);
            }
            count = count + 1;
        }

        count = 0 ;
        while (count < 3)
        {
            if (ch == pun[count])
            {
                pun_string.insert(ch);

            }
            count = count + 1 ;

        }
        if (isalnum(ch))
        {
            temp[x++] = ch;
        }
        else if ((ch == '\n' || ch == ' ') && (x != 0))
        {
            temp[x] = '\0';
            x = 0;
            if (keyword_library(temp) == 1)
            {
                keyword_string.insert(temp);
            }
            else if (const_library(temp) == 1)
            {
                constant_string.insert(temp);
            }
            else
            {
                    iden_string.insert(temp);
            }
        }

    }
    display();

    return 0;
}

