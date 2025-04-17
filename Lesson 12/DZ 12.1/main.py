import codecs



def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        cln_txt = ""
        final_txt = ""
        in_tag = False
        for lines in html:
            if lines == "<":
                in_tag = True
            elif lines == ">":
                in_tag = False
            elif not in_tag:
                cln_txt += lines

        cln_txt = cln_txt.splitlines()
        text_lines = [cln.strip() for cln in cln_txt if cln.strip() !=""]
        final_txt += "\n".join(text_lines)
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(final_txt)


delete_html_tags("draft.html", "cleaned.txt")