def google(message):
    """Concatenates the google search url with user search request.
    :return: Google search URL"""
    string = message.split()
    string = string[1:]
    if len(string) == 1:
        text = "https://www.google.com/#safe=off&q=" + string[0] + "&*"
        return text
    else:
        returnval = ""
        for i in string:
            returnval += i
            if string.index(i) != len(string) - 1:
                returnval += "+"
        text = "https://www.google.com/#safe=off&q=" + returnval + "&*"
        return text