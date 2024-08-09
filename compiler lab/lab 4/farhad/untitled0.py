
import re

def cal_follow(s, productions, first):
    follow = set()
    if len(s)!=1 :
        return {}
    if(s == list(productions.keys())[0]):
        follow.add('$')

    for i in productions:
        for j in range(len(productions[i])):
            if(s in productions[i][j]):
                idx = productions[i][j].index(s)

                if(idx == len(productions[i][j])-1):
                    if(productions[i][j][idx] == i):
                        break
                    else:
                        f = cal_follow(i, productions, first)
                        for x in f:
                            follow.add(x)
                else:
                    while(idx != len(productions[i][j]) - 1):
                        idx += 1
                        if(not productions[i][j][idx].isupper()):
                            follow.add(productions[i][j][idx])
                            break
                        else:
                            f = cal_first(productions[i][j][idx], productions)

                            if('ε' not in f):
                                for x in f:
                                    follow.add(x)
                                break
                            elif('ε' in f and idx != len(productions[i][j])-1):
                                f.remove('ε')
                                for k in f:
                                    follow.add(k)

                            elif('ε' in f and idx == len(productions[i][j])-1):
                                f.remove('ε')
                                for k in f:
                                    follow.add(k)

                                f = cal_follow(i, productions, first)
                                for x in f:
                                    follow.add(x)

    return follow

def cal_first(s, productions):

    first = set()

    for i in range(len(productions[s])):

        for j in range(len(productions[s][i])):

            c = productions[s][i][j]

            if(c.isupper()):
                f = cal_first(c, productions)
                if('ε' not in f):
                    for k in f:
                        first.add(k)
                    break
                else:
                    if(j == len(productions[s][i])-1):
                        for k in f:
                            first.add(k)
                    else:
                        f.remove('ε')
                        for k in f:
                            first.add(k)
            else:
                first.add(c)
                break

    return first

def main():
    productions = {}
    grammar = open("input0.txt", "r")

    first = {}
    follow = {}

    for prod in grammar:
        l = re.split("( /->/\n/)*", prod)
        m = []
        for i in l:
            if (i == "" or i == None or i == '\n' or i == " " or i == "-" or i == ">"):
                pass
            else:
                m.append(i)

        left_prod = m.pop(0)
        right_prod = []
        t = []

        for j in m:
            if(j != '|'):
                t.append(j)
            else:
                right_prod.append(t)
                t = []

        right_prod.append(t)
        productions[left_prod] = right_prod

    for s in productions.keys():
        first[s] = cal_first(s, productions)

    print("FIRST :")
    for lhs, rhs in first.items():
        print(lhs, ":" , rhs)

    print("")

    for lhs in productions:
        follow[lhs] = set()

    for s in productions.keys():
        follow[s] = cal_follow(s, productions, first)

    print("FOLLOW :")
    for lhs, rhs in follow.items():
        print(lhs, ":" , rhs)

    grammar.close()

if __name__ == "__main__":
    main()

def remove_left_recursion(non_terminal, production_rule):
    output1 = ''
    output2 = ''
    productions = [p for p in production_rule.split('|') if p != 'ε']

    for production in productions:
        if not production.startswith(non_terminal):
            output1 += f"{production}{non_terminal}'|"
        else:
            output2 += f"{production.replace(non_terminal, '')}{non_terminal}'|"

    print("The output is:")
    output1 = output1[:-1]
    print(f"{non_terminal} --> {output1}")
    print(f"{non_terminal}' --> {output2} ε")

non_terminal = 'E'
productions = 'E+T|T'
print(f"The given grammar: {non_terminal} --> {productions}")

remove_left_recursion(non_terminal, productions)

def calculate_first(grammar):
    first = {}

    def calculate_first_recursive(non_terminal):
        if non_terminal in first:
            return first[non_terminal]

        first_set = set()
        for rule in grammar[non_terminal]:
            for symbol in rule:
                if not symbol.isupper():
                    first_set.add(symbol)
                    break
                first_set.update(calculate_first_recursive(symbol))
                if '#' not in first[symbol]:
                    break

        first[non_terminal] = first_set
        return first_set

    for non_terminal in grammar:
        calculate_first_recursive(non_terminal)

    return first

def calculate_follow(grammar, first, start_symbol):
    follow = {non_terminal: set() for non_terminal in grammar}

    follow[start_symbol].add('$')  # Adding $ to the start symbol

    def calculate_follow_recursive(non_terminal):
        for symbol in grammar:
            for rule in grammar[symbol]:
                for idx, r_symbol in enumerate(rule):
                    if r_symbol == non_terminal:
                        if idx == len(rule) - 1:
                            if symbol != non_terminal:
                                follow[symbol].update(calculate_follow_recursive(symbol))
                        else:
                            next_symbol = rule[idx + 1]
                            if not next_symbol.isupper():
                                follow[non_terminal].add(next_symbol)
                            else:
                                follow[non_terminal].update(first[next_symbol] - {'#'})
                                if '#' in first[next_symbol]:
                                    follow[non_terminal].update(calculate_follow_recursive(next_symbol))

        return follow[non_terminal]

    for non_terminal in grammar:
        calculate_follow_recursive(non_terminal)

    return follow

# Example usage
if __name__ == "__main__":
    # Define the grammar as a dictionary of non-terminals and their production rules
    grammar = {
        'E': ['TR'],
        'R': ['+TR', '#'],
        'T': ['FY'],
        'Y': ['*FY', '#'],
        'F': ['(E)', 'i']
    }

    # Specify the start symbol of the grammar
    start_symbol = 'E'

    # Calculate FIRST sets
    first = calculate_first(grammar)

    # Calculate FOLLOW sets
    follow = calculate_follow(grammar, first, start_symbol)

    # Print FIRST sets
    for non_terminal, first_set in first.items():
        print(f'First({non_terminal}) = {first_set}')

    # Print FOLLOW sets
    for non_terminal, follow_set in follow.items():
        print(f'Follow({non_terminal}) = {follow_set}')

import sys
sys.setrecursionlimit(60)

def first(string):
    #print("first({})".format(string))
    first_ = set()
    if string in non_terminals:
        alternatives = productions_dict[string]

        for alternative in alternatives:
            first_2 = first(alternative)
            first_ = first_ |first_2

    elif string in terminals:
        first_ = {string}

    elif string=='' or string=='#':
        first_ = {'#'}

    else:
        first_2 = first(string[0])
        if '#' in first_2:
            i = 1
            while '#' in first_2:
                #print("inside while")

                first_ = first_ | (first_2 - {'#'})
                #print('string[i:]=', string[i:])
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'#'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'#'}
                i += 1
        else:
            first_ = first_ | first_2


    #print("returning for first({})".format(string),first_)
    return  first_


def follow(nT):
    #print("inside follow({})".format(nT))
    follow_ = set()
    #print("FOLLOW", FOLLOW)
    prods = productions_dict.items()
    if nT==starting_symbol:
        follow_ = follow_ | {'$'}
    for nt,rhs in prods:
        #print("nt to rhs", nt,rhs)
        for alt in rhs:
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_ = follow_ | follow(nt)
                    else:
                        follow_2 = first(following_str)
                        if '#' in follow_2:
                            follow_ = follow_ | follow_2-{'#'}
                            follow_ = follow_ | follow(nt)
                        else:
                            follow_ = follow_ | follow_2
    #print("returning for follow({})".format(nT),follow_)
    return follow_





no_of_terminals=int(input("Enter no. of terminals: "))

terminals = []

print("Enter the terminals :")
for _ in range(no_of_terminals):
    terminals.append(input())

no_of_non_terminals=int(input("Enter no. of non terminals: "))

non_terminals = []

print("Enter the non terminals :")
for _ in range(no_of_non_terminals):
    non_terminals.append(input())

starting_symbol = input("Enter the starting symbol: ")

no_of_productions = int(input("Enter no of productions: "))

productions = []

print("Enter the productions:")
for _ in range(no_of_productions):
    productions.append(input())


#print("terminals", terminals)

#print("non terminals", non_terminals)

#print("productions",productions)


productions_dict = {}

for nT in non_terminals:
    productions_dict[nT] = []


#print("productions_dict",productions_dict)

for production in productions:
    nonterm_to_prod = production.split("->")
    alternatives = nonterm_to_prod[1].split("|")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)

#print("productions_dict",productions_dict)

#print("nonterm_to_prod",nonterm_to_prod)
#print("alternatives",alternatives)


FIRST = {}
FOLLOW = {}

for non_terminal in non_terminals:
    FIRST[non_terminal] = set()

for non_terminal in non_terminals:
    FOLLOW[non_terminal] = set()

#print("FIRST",FIRST)

for non_terminal in non_terminals:
    FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal)

#print("FIRST",FIRST)


FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
for non_terminal in non_terminals:
    FOLLOW[non_terminal] = FOLLOW[non_terminal] | follow(non_terminal)

#print("FOLLOW", FOLLOW)

print("{: ^20}{: ^20}{: ^20}".format('Non Terminals','First','Follow'))
for non_terminal in non_terminals:
    print("{: ^20}{: ^20}{: ^20}".format(non_terminal,str(FIRST[non_terminal]),str(FOLLOW[non_terminal])))