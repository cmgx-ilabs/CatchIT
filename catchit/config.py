class Catchit_Config:
    def __init__(self):
        self.bash: str = "bash"
        self.scanning_path: str = "."
        self.system_path_sep: str = "**/*"
        self.tunnel_flags = ""
        self.case_flag = ""
        self.timeout = 2
        self.includes = ""
