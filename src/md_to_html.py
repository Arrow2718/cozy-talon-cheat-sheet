import os 

class HTMLCheatsheetGen():
    def __init__(self, filepath: str):
        
        self.filepath = filepath
        self.md_lines = None
        
        if os.path.exists(self.filepath) is True and self.filepath.endswith(".md"):
            with open(filepath, "r+") as f:
                self.md_lines = f.readlines()
                
        elif self.filepath.endswith(".md") is False:
            raise ValueError("Given file is not a Markdown File. Please provide \
                   a valid markdown file.")
        
        else: 
            raise FileNotFoundError("Given File Path doesn't exist.")

        self.n_lines = None
        self.md_line_map = {
                            "title:": "meta_title",
                            "#": "h1"  ,
                            "##": "h2" ,
                            "| command word |  method/actions |": "table_header",

                            }
        self.html_line_map = { "meta_title": ["<title>", "</title>"], 
                              "h1" : ["<h1 class=\"title\">","</h1>"] , 
                              "h2" : ["<h2 id=\"context\">", "</h2>"], 
                              "table_header": ["<thead>\n<th>","</th>\n</thead>" ],
                              "table_head_cell" : ["<th>", "</th>"],
                              "table_body" : ["<tbody>", "</tbody>"],
                              "table_row" : ["<tr>, </tr>"],
                              "table_cell_left": ["<td><strong>", "</strong></td>"],
                              "table_cell_right" : ["<td><em>", "</em></td>" ],
                              "html_header" : "<!DOCTYPE html>\n \
                                                <html xmlns=\"http://www.w3.org/1999/xhtml\" lang=\"\" xml:lang=\"\" >\n \
                                                    <head>\n \
                                                    <meta charset=\"UTF-8\">\n \
                                                    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n \
                                                    <title>community Command Set</title>\n \
                                                    <link rel=\"stylesheet\" href=\"../cheatsheet.css\">\n \
                                                </head>"}
            
    def get_n_lines(self):
        
        if self.n_lines is None and self.md_lines is not None:
            self.n_lines = len(self.md_lines)

        
        return self.n_lines
             