def send_messages(lists, sent_messages):
    while lists:
        hold = lists.pop()
        print(hold)
        sent_messages.append(hold)
    sent_messages.reverse()


def show_messages(lists):
    for list in lists:
        print(list)


listofmessage = ['ahmed', 'essam', 'azab']
sent_messages = []
send_messages(listofmessage[:], sent_messages)
show_messages(listofmessage)
show_messages(sent_messages)