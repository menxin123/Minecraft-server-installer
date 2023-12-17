import fileinput


def replace_text(file_path, old_text, new_text):
    try:
        with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
            for line in file:
                line = line.replace(old_text, new_text)
                print(line, end='')

        print("文本替换成功！")

    except FileNotFoundError:
        print("文件路径无效！")

    except Exception as e:
        print("发生错误：", e)

file_path = "test.txt"
old_text = "'"
new_text = 'a'

replace_text(file_path, old_text, new_text)
