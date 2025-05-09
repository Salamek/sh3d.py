from sh3d.FileLoader import FileLoader

# Default is parsion of JavaObject Home
with FileLoader('myHome.sh3d') as file_loader:
    # Dump home, ~all models are dataclasses so you will actually see full readable dump
    print(file_loader.home)
