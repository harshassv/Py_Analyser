# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)


# #### Sample Regexs ####

# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
import re
def updated_Filter_string(lines):
    convert=[0,0]
    convert[0]=''
    convert[1]=False
    converted_string=''
    for i in (lines):
        #print(i)
        if "'" in i and (convert[0]=='' or convert[0]=="'"):
            #print(i)
            convert[0]="'"
            convert[1]=not convert[1]
            converted_string=converted_string+i
            if not convert[1]:
                convert[0]=''
            continue
        if '"' in i and (convert[0]=='' or convert[0]=='"'):
            convert[0]='"'
            convert[1]=not convert[1]
            converted_string=converted_string+i
            if not convert[1]:
                convert[0]=''
            continue
        if convert[1] and ('\n' in i or '#' in i or '(' in i):
            i='$'
        converted_string=converted_string+i
    return converted_string
def variables(i):
    result=re.search(r"^(\s*\w+\s*[,]?)+",i)
    if result!=None:
        index=list(result.span())
        for temp in i[index[0]:index[1]].split(','):
            temp=temp.strip()
            if temp!='' and temp not in ans:
                ans.append(temp)
def updated9_list_variables(lines):
    s_list=updated_Filter_string(lines)
    s_list=s_list.split('\n')
    global ans
    ans=[]
    bracket_check_flag=0
    skip=0
    for i in s_list:
        if ('#' in i):
            i=i[:i.index('#')]
        elif '"""' in i:
            i=i[:i.index('"""')]
        elif "'''" in i:
            i=i[:i.index("'''")]
        if not (bool(re.match('(assert|if|elif|while)',i)) or i==''):
            if bool(re.match('global',i)):
                for temp in i[i.index('global')+7:].split(','):
                    temp=temp.strip()
                    if temp not in ans:
                        if ';' not in temp:
                            ans.append(temp)
                        else:
                            ans.append(temp[:-1])
            if 'def' in i or 'class' in i:
                if '(' in i:
                    bracket_check_flag+=1
                if ')' in i:
                    bracket_check_flag-=1
                skip=1
            elif ' ' in i[0]:
                pass
            else:
                skip=0
            if not skip and bracket_check_flag==0:
                if '=' in i and '(' not in i:
                    variables(i)
                elif '=' in i and i.find('=')<i.find('('):
                    if '(' in i:
                        bracket_check_flag+=1
                        variables(i)
                    if ')' in i:
                        bracket_check_flag-=1
                else:
                    if '(' in i:
                        bracket_check_flag+=1
                    if ')' in i:
                        bracket_check_flag-=1
            elif bracket_check_flag>0 and ')' in i:
                bracket_check_flag-=1
    return ans
print(updated9_list_variables('''
def Test(
    t_z=kjbdkjw
):
    pass
x=45
'''))



        
        
