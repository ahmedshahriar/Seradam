
processor_text = "Intel Core i3 9005U"
processor = ""
generation = ""
search = "Intel Core i"
if search in processor_text:
    search_pos = processor_text.find(search)
    key_pos = search_pos + len(search)
    processor = search + processor_text[key_pos]
    print(processor)
    gen_pos =  key_pos + 2
    generation = processor_text[gen_pos]+"th"
    print(generation)