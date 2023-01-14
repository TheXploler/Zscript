from pathlib2 import Path
import shutil
import os

def replacetext(compiled_filename, search_text, replace_text):
    file = Path(compiled_filename)
    data = file.read_text()
    data = data.replace(search_text, replace_text)
    file.write_text(data)
    return "Text replaced"

def addmodule(compiled_filename):
    filenames = ["basic_module.zmodule", compiled_filename, "override.zmodule"]
    with open("output.py", "w") as outfile:
        for names in filenames:
            with open(names) as infile:
                outfile.write(infile.read())
            outfile.write("\n")
    os.remove(compiled_filename)

def main_compiler(compiled_filename):
    with open(compiled_filename, "r") as file:
        lines = file.readlines()
        for x in lines:
            line = x.strip()
            if x.startswith("#") != True:
                replacetext(compiled_filename, "[End]", "clear()")
                replacetext(compiled_filename, line, f"print('{line}')")
        replacetext(compiled_filename, "#", "time.sleep(")
        replacetext(compiled_filename, ";", ")")
        addmodule(compiled_filename)

def compile(filename):
    shutil.copyfile(filename, f"{filename}_raw") 
    main_compiler(f"{filename}_raw")

compile("main.zscript")
