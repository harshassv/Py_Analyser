def updated_functions(data):      
    s_list=data.split('\n')
    top=-1
    e_indent=['elif','else','except','try','finally','for','if','try','while','with']
    ei_flag=False    #This flag will tells whether extra indendation is caused by any of the element present in e_indent
    ei=0        # ei -> Extra indendation which is caused by elements present in e_indent
    f_dict={}
    f_stack=[]
    for i in indent_dict.keys():
        f_dict[i]=''
    cli=None     #cli_temp -> current line indentation
    for i,k in zip(s_list,range(0,len(s_list))):
        if i!='':
            if 'def' in i:
                f_stack.append([i[i.index('def')+4:i.index('(')].strip(),0])
                top+=1
                continue
            for j2 in e_indent:
                if j2 in i:
                    for j3 in s_list[k+1]:
                        if j3!=' ':
                            f_stack[top][1]=f_stack[top][1]+(s_list[k+1].index(j3)-indent_dict[f_stack[top][0]])
                            indent_dict[f_stack[top][0]]=s_list[k+1].index(j3)
                            ei_flag=True
                            break
            if ei_flag:
                ei_flag=False
                continue
            for j in i:
                if j!=' ':
                    cli=i.index(j)
                    break
            if cli==indent_dict[f_stack[top][0]]:
                f_dict[f_stack[top][0]]=f_dict[f_stack[top][0]]+f'\n{i}'
            else:
                if cli>=indent_dict[f_stack[top][0]]-f_stack[top][1] and cli<indent_dict[f_stack[top][0]]:
                    diff_indent=indent_dict[f_stack[top][0]]-cli
                    f_stack[top][1]=f_stack[top][1]-diff_indent
                    indent_dict[f_stack[top][0]]=indent_dict[f_stack[top][0]]-diff_indent
                    f_dict[f_stack[top][0]]=f_dict[f_stack[top][0]]+f'\n{i}'
                else:
                    while True:
                        f_stack.pop()
                        top-=1
                        if top==-1:
                            break
                        if cli>=indent_dict[f_stack[top][0]]-f_stack[top][1] and cli<=indent_dict[f_stack[top][0]]:
                            diff_indent=indent_dict[f_stack[top][0]]-cli
                            f_stack[top][1]=f_stack[top][1]-diff_indent
                            indent_dict[f_stack[top][0]]=indent_dict[f_stack[top][0]]-diff_indent
                            f_dict[f_stack[top][0]]=f_dict[f_stack[top][0]]+f'\n{i}'
                            break
                        
#             else:
#                 print(f_stack)
#                 f_stack.pop()
#                 top-=1
#                 f_dict[f_stack[top][0]]=f_dict[f_stack[top][0]]+f'\n{i}'
#             if top==-1:
#                 break
    return f_dict   #f_dict to be return
string='''
def test1():
    t1=20
    def test2():
        t2=90
        def test3():
            t3=89
            t3_1=87
            def tets4():
                t4=90
            t3_2=90
        t2_2=98
    t1_1=90    
'''
indent_dict=initialise_functions(string)
updated_functions(string)