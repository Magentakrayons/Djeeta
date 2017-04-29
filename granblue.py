def wiki(message, requests):
    """Performs an http://gbf.wiki search using json.
    :return: Relevant URLs"""
    string = message.split()
    string = string[1:]
    if len(string) <= 1:
        userInput = string[0]
    else:
        userInput = ""
        for i in string:
            userInput += i
            if string.index(i) != len(string) - 1:
                userInput += "_"
    url = "https://gbf.wiki/api.php?action=opensearch&format=json&formatversion=2&search=" + userInput
    t = requests.get(url).json()
    query = t[0]
    query = query.replace("_", " ")
    fullUrl = t[3]
    text = str(len(fullUrl)) + " matches for: " + query + "\n"
    addtext = ""
    for i in fullUrl:
        addtext += i + "\n"
    return text + addtext


def events(message, requests):
    """Parses http://gbf.wiki and returns the current events.
    :return: Event list text."""
    link = "http://gbf.wiki"
    f = requests.get(link)
    f = f.text.splitlines()
    searchtext = "Current Events"
    eventnames = []
    eventurls = []
    finished = False
    for i in range(len(f) + 1):
        if finished:
            break
        elif searchtext in f[i]:
            adding = True
            i = i + 8
            while adding:
                line = f[i]
                line = line.split('"')
                linkend = line[1]
                title = line[3]
                url = link + linkend
                eventurls.append(url)
                eventnames.append(title)
                i = i + 1
                if "</p>" in f[i]:
                    adding = False
                    finished = True

    text = "The Current Events include: \n \n"
    for i in range(len(eventnames)):
        text = text + eventnames[i] + "\n" + eventurls[i] + "\n\n"
    return text


def exp(message):
    """Performs table computation from exp table and returns remaining exp.
    :return: EXP remaining (str)"""
    if "char" in message:
        table = open('tables/charexp.txt', 'r')
    else:
        table = open('tables/exp.txt', 'r')
    text = message.split()
    uplvl = int(text[1])
    lowlvl = int(text[2])
    expleft = int(text[3])
    pointer = ""

    for i in range(lowlvl):
        pointer = table.readline()
    pointer = pointer.split()
    additive = int(pointer[1]) - expleft
    currentexp = int(pointer[2]) + additive
    for i in range(uplvl - lowlvl):
        pointer = table.readline()
    pointer = pointer.split()
    upperexp = int(pointer[2])

    exp = upperexp - currentexp
    text = "Amount of EXP needed: " + str(exp)
    table.close()
    return text


def skill(message):
    """Performs table look up from skill.txt and returns suggested skill fodder.
    :return: Suggested Skill Fodder"""
    userInput = message.split()
    type = userInput[1]
    type = type.upper()
    level = int(userInput[2])

    if type == "SSR":
        level += 10
    elif type == "BAHAMUT" or type == "SERAPH":
        level += 25
    if level < 1 or level == 10 or level == 25 or level > 39:
        return "Invalid Level. \nPlease use !help to see !skill's syntax."
    else:
        table = open('tables/skill.txt', 'r')
        for k in range(level):
            line = table.readline()
        line = line.split(',')
        text = ""
        for i in range(len(line)):
            text += line[i]
            if i != len(line) - 1:
                text += "\nor "
        text += "```"
        text = "To reach the next skill level, you can use:" + "\n```" + text
        return text

    
def servertime(datetime,timezone):
    month = {
        1: "Jan.",
        2: "Feb.",
        3: "Mar.",
        4: "Apr.",
        5: "May",
        6: "Jun.",
        7: "Jul.",
        8: "Aug.",
        9: "Sep.",
        10: "Oct.",
        11: "Nov.",
        12: "Dec."}
    t = timezone('Japan')
    t = datetime.now(t)
    if t.hour == 0:
        meridiem = "AM"
        hour = 12
    elif t.hour > 11:
        meridiem = "PM"
        hour = t.hour - 12
    else:
        meridiem = "AM"
        hour = t.hour

    time = "The Server Time is currently: \n" \
           "Date: " + month[t.month] + " " + str(t.day) + "\n" + \
           "Time: " + str(hour) + ":" + str(t.minute) + ":" + str(t.second) + " " + meridiem
    return time    
