import os 

class Sheet:
    heading :str = ""
    table : list[list[str]] = []
    

class HTMLCheatsheetGen():
    def __init__(self, filepath: str):
        
        self.filepath = filepath
        self.md_lines = None
        
        if os.path.exists(self.filepath) is True and self.filepath.endswith(".md"):
            with open(filepath, "r+") as f:
                self.md_lines = f.read()
                
        elif self.filepath.endswith(".md") is False:
            raise ValueError("Given file is not a Markdown File. Please provide \
                   a valid markdown file.")
        
        else: 
            raise FileNotFoundError("Given File Path doesn't exist.")

        self.n_lines = None

        self.html_map = { "meta_title": ["<title>", "</title>\n"], 
                              "h1" : ["<h1 class=\"title\">","</h1>\n"] , 
                              "h2" : ["<h2 id=\"title\">", "</h2>\n"], 
                              "table": ["<table>", "</table>\n"],
                              "table_header" :"<thead>\n \
                                                <tr>\n \
                                                <th>command word</th>\n \
                                                <th>method/actions</th>\n \
                                                </tr>\n \
                                                </thead>\n",
                              "table_body" : ["<tbody>\n", "</tbody>\n"],
                              "table_row" : ["<tr>\n, </tr>\n"],
                              "table_cell_left": ["<td><strong>", "</strong></td>\n"],
                              "table_cell_right" : ["<td><em>", "</em></td>\n" ],
                              "html_header" : "<!DOCTYPE html>\n \
                                                <html xmlns=\"http://www.w3.org/1999/xhtml\" lang=\"\" xml:lang=\"\" >\n \
                                                    <head>\n \
                                                    <meta charset=\"UTF-8\">\n \
                                                    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n \
                                                    <title>header_title</title>\n \
                                                    <link rel=\"stylesheet\" href=\"../cheatsheet.css\">\n \
                                                </head>\n\n",
                               "html_body": ["<body>\n", "</body>"]}
        
        self.intermediate_representation = {
                                "meta_title": "", 
                                "sheets": [] 
                                }
        
    
    def get_intermediate_rep(self):
        
        md_split = self.md_lines.split("---------")
        
        title_block = md_split[0].splitlines()
        
        sheets = md_split[1:]
        
        title = title_block[1].split("\'")[1]
        print(f"Sheet title is {title}")
        
        self.intermediate_representation["meta_title"] = title
        
        for sheet_md in sheets:
            
            sheet_struct = Sheet()
            
            sheet_split = sheet_md.splitlines()
            
            for line in sheet_split:
                
                if "##" in line:
                    
                    sheet_struct.heading = line.replace("## ","")
                    
                elif "| **" in line:
                    
                    sheet_struct.table.append([line.split("|")[1], line.split("|")[3]])  
            
            self.intermediate_representation["sheets"].append(sheet_struct)
            
    def convert_to_html(self):
        
        name = self.filepath.split(".")[0]
        html_path = ".".join([name, "html"])
        
        with open(html_path, "w") as html:
            
            header = self.html_map["html_header"].replace("header_title", self.intermediate_representation["meta_title"])
            
            html.write( header )
            
            html.write(self.html_map["html_body"][0])
            
            h1_title = self.intermediate_representation["meta_title"]
            
            html.write(self.html_map["h1"][0])
            html.write(h1_title)
            html.write(self.html_map["h1"][1])
            
            for sheet in self.intermediate_representation["sheets"]:
                
                h2_tag1 = self.html_map["h2"][0].replace("title", sheet.heading)
                h2_tag2 = self.html_map["h2"][1]
                
                html.write(h2_tag1)
                html.write(sheet.heading)
                html.write(h2_tag2)
                
                html.write(self.html_map["table"][0])
                html.write(self.html_map["table_header"])
                html.write(self.html_map["table_body"][0])
                
                for idx, row in enumerate(sheet.table):
                    
                    html.write(self.html_map["table_row"][0])
                    
                    html.write(self.html_map["table_cell_left"][0])
                    html.write(row[0])
                    html.write(self.html_map["table_cell_left"][1])
                    
                    html.write(self.html_map["table_cell_right"][0])
                    html.write(row[1])
                    html.write(self.html_map["table_cell_right"][1])
                    
                    html.write(self.html_map["table_row"][1])
                
                html.write(self.html_map["table_body"][1])
                html.write(self.html_map["table"][1])
                
            
            html.write(self.html_map["html_body"][1])
            
            
            