def integer_to_binary(integer):
    binary = []
    while integer > 0:
        bit = integer % 2
        integer = integer // 2
        binary.append(bit)
    binary.reverse()
    return binary


num = []
dic = {}


def a_instruction(a_info, num, dic):
    instruct = ""
    a_info = a_info[1: len(a_info)]
    for a in a_info:
        instruct = instruct + str(a)
    if instruct.isdigit() == True:
        instructed = integer_to_binary(int(instruct))
        num_list = 16 - len(instructed)
        instruct = ""
        for w in instructed:
            instruct = instruct + str(w)
        instruct = num_list * "0" + instruct
        return instruct
    elif instruct.isalpha() == True:
        if instruct not in dic:
            binary = integer_to_binary(len(num) + 1)
            dic[instruct] = binary
            num.append(binary)
            num_list = 16 - len(binary)
            instruct = ""
            for k in binary:
                instruct = instruct + str(k)
            instruct = num_list * "0" + instruct
            return instruct
        elif instruct in dic:
            binary = dic[instruct]
            num_list = 16 - len(binary)
            instruct = ""
            for j in binary:
                instruct = instruct + str(j)
            instruct = num_list * "0" + instruct
            return instruct
    print(instruct)


comp = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "M": "1110000",
    "!D": "0001101",
    "!A": "0110001",
    "!M": "1110001",
    "-D": "0001111",
    "-A": "0110011",
    "-M": "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101"
}
dest = {
    "null": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}
jmp = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}


def c_instruction(c_info, comp, dest, jmp):
    instruct = ""
    for c_instruct in range(3):
        instruct = instruct + "1"
    list_c = list(c_info)
    if "=" in list_c:
        dest_item = list_c[0:list_c.index("=")]
        dest_str = ""
        for each_dest in dest_item:
            dest_str = dest_str + each_dest
        comp_item = list_c[list_c.index("=") + 1:]
        comp_str = ""
        for each_comp in comp_item:
            comp_str = comp_str + each_comp
        instruct = instruct + comp[comp_str] + dest[dest_str] + "000"
        return instruct
    elif ";" in list_c:
        comp_item = list_c[0:list_c.index(";")]
        comp_str = ""
        for each_comp in comp_item:
            comp_str = comp_str + each_comp
        jmp_item = list_c[list_c.index(";") + 1:]
        jmp_str = ""
        for each_jmp in jmp_item:
            jmp_str = jmp_str + each_jmp
        instruct = instruct + comp[comp_str] + "000" + jmp[jmp_str]
        return instruct


def main():
    print("Instruction: This code is going to be ue to convert symbolic language to machine language of 16 bit instruction.\nPlease copy and past your symbolic code into symbolic_code.txt \n\n Caution click enter after pasting it to go to the next empty line of IT CAN HAVE ERRORS\n\n and copy the relative file path into type in the file name instruction in the terminal.\nYou will be provided with a list of code after the comments and labels are removed while the a instruction and c instruction are converted. ")
    file_name = input("Please type in the file name: ")
    print("This is the file line list without comments or label")
    file_to_interpret = []
    with open(file_name, 'r') as parse_file:
        for line in parse_file:
            listy = list(line)
            if listy[0] == "/" or listy[0] == "\n" or listy[0] == "(":
                listy = ""
            elif "/" in listy:
                index = listy.index("/")
                for a in range(len(line) - index):
                    listy.pop()
                file_to_interpret.append(listy)
            else:
                listy.pop()
                file_to_interpret.append(listy)
        print(file_to_interpret)
        for inter_lines in file_to_interpret:
            if inter_lines[0] == "@":
                print(a_instruction(inter_lines, num, dic))
            elif inter_lines[0] != "@":
                print(c_instruction(inter_lines, comp, dest, jmp))



main()
