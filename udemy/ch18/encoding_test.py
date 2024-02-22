unicode_string = "中"
utf_bytes = unicode_string.encode("utf-8")
print(utf_bytes)

result_string = utf_bytes.decode("utf-8")
print(result_string)
