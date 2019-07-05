"""
#低级密码
def bool_lowpsw(psw):
    if(len(psw)>8):
        return False
    else:
        for s in psw:
            if(ord(s)<48 and ord(s)>57 and ord(s)<65 and ord(s)>90 and ord(s)<97 and ord(s)>122):
                return False
        return True
#中级密码
def bool_midpsw(psw):
    if(len(psw)<:
        return False
    else:
        for s in psw:
            if(ord(s)<48 and ord(s)>57 and ord(s)<65 and ord(s)>90 and ord(s)<97 and ord(s)>122):
                return False
        return True
    
print(bool_lowpsw("1232222"))
"""
"""
案例3：模拟企业密码检查方式(密码安全性检查代码)
低级密码要求： 
1. 密码由单纯的数字或字母组成 
2. 密码长度小于等于8位
中级密码要求： 
1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合 
2. 密码长度不能低于8位
高级密码要求： 
1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合 
2. 密码只能由字母开头 
3. 密码长度不能低于16位
		
特殊符号：!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>
字符符号：abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
数字符号：0123456789

"""

spe_sym = """!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>"""
cha_sym = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"""
num_sym = """0123456789"""
def psw_len(psw):
    if(len(psw) == 0):
        return 0
    elif(len(psw)<=8):
        return 1
    elif(len(psw)>8 and len(psw)<16):
        return 2
    elif(len(psw)>=16):
        return 3

def psw_spe(psw,spe_sym):
    spe_num = 0
    for s in spe_sym:
        if(s in psw):
            spe_num = spe_num +1
    return spe_num

def psw_cha(psw,cha_sym):
    cha_num = 0
    for s in cha_sym:
        if(s in psw):
            cha_num = cha_num +1
    return cha_num

def psw_num(psw,num_sym):
    num = 0
    for s in num_sym:
        if(s in psw):
            num = num +1
    return num

def main():
    print("Please input password:")
    psw = input()
    p_len = psw_len(psw)
    spe_count = psw_spe(psw,spe_sym)
    cha_count = psw_cha(psw,cha_sym)
    num_count = psw_num(psw,num_sym)
    if(p_len==1 and cha_count>0 and spe_count==0 and num_count==0):
        print("Password security level:low")
    elif(p_len==1 and cha_count==0 and spe_count==0 and num_count>0):
        print("Password security level:low")
    elif(p_len==2 and cha_count>0 and spe_count>0 and num_count==0):
        print("Password security level:medium")
    elif(p_len==2 and cha_count>0 and spe_count==0 and num_count>0):
        print("Password security level:medium")
    elif(p_len==2 and cha_count==0 and spe_count>0 and num_count>0):
        print("Password security level:medium")
    elif(p_len==3 and cha_count>0 and spe_count>0 and num_count>0 and psw[0:1] in cha_sym):
        print("Password security level:high")
    else:
        print("The password is illegal! Please enter again:")
           

main()

    
