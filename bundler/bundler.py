import argparse

parser = argparse.ArgumentParser(description="Wrap the bundlle like it's epic meal time or somethin'")
parser.add_argument('-w','--wrap', type=str, help='wraps it')
args = parser.parse_args()

if __name__ == '__main__':
    bundle = str(args.wrap)
    
    with open(bundle, "r+") as f:
        first_line = f.readline()
        if first_line != "(function($){":
            lines = f.readlines()
            f.seek(0)
            f.write("(function($){")
            f.write(first_line)
            f.writelines(lines)

    with open(bundle, "a") as myfile:
        myfile.write("})(jQuery);")
