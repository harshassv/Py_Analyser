#Filter for replacing \n with $ in strings
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
        if convert[1] and '\n' in i:
            i='$'
        converted_string=converted_string+i
    return converted_string

#Function To retrieve Variables in code
def updated3_list_variables(lines):
    s_list=updated_Filter_string(lines)
    s_list=s_list.split('\n')
    ans=set()
    bracket_check_flag=False
    skip=0
    for i in s_list:
        if i!='':
            if 'def' in i or 'class' in i:
                skip=1
            elif ' ' in i[0]:
                pass
            else:
                skip=0
            if ('if ' not in i or (i.find("'")!=-1 and i.find("'") < i.find('if')) or (i.find('"')!=-1 and i.find('"') < i.find('if'))) and ('#' not in i and '"""' not in i and "'''" not in i):
                if not skip and not bracket_check_flag:
                    if '(' not in i:
                        if '=' in i and ',' not in i:
                         ans.add(i[:i.index('=')].strip())
                        elif '=' in i and ',' in i:
                            for j in i[:i.index('=')].split(','):
                                ans.add(j.strip())
                    elif '=' in i and i.find('=')<i.find('('):
                        if '(' in i:
                            bracket_check_flag= not bracket_check_flag
                            if ',' not in i:
                             ans.add(i[:i.index('=')].strip())
                            else:
                                for j in i[:i.index('=')].split(','):
                                    ans.add(j.strip())
                        if ')' in i:
                            bracket_check_flag=not bracket_check_flag
    return ans  


#Function For finding For loop Variables
#For loop Variables
def forloop_variables(lines):
    s_list=lines.split('\n')
    ans=set()
    for i in s_list:
        if 'for' in i and 'if' not in i:
                for j in i[4:i.index(' in ')].split(','):
                    ans.add(j.strip())
    return ans
