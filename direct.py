import glob

for name in glob.glob('cls?.py'):
    print(name)

for name in glob.glob('dir/file?.txt'):
    print(name)