from sh3d.FileLoader import FileLoader, HomeSource


# Load home from Home.xml instead
with FileLoader('myHome.sh3d', home_source=HomeSource.XML) as file_loader:
    # Dump home, ~all models are dataclasses so you will actually see full readable dump
    print(file_loader.home)  # Home object