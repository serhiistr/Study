import time


class Messenger:
    db = []
    requested_count = 0

    def send_message(self, name, text, ):  # фукция принимает на вход текст
        timestamp = time.asctime()
        self.db.append({
            "name": name,
            "text": text,
            "timestmp": timestamp
        })

    def get_messages(self):
        return self.db

    def get_new_messages(self):
        new_messages = self.db[self.requested_count:]
        self.requested_count += len(new_messages)
        return self.db


messenger = Messenger()
messenger.send_message("Jack", "abc")
messenger.send_message("Jack", "abcd")
print(messenger.get_messages())
print(messenger.get_new_messages())
print()

messenger.send_message("Black", "Hello!")
print(messenger.get_messages())
print(messenger.get_new_messages())
print()

messenger.send_message("Black", "Hello2!")
print(messenger.get_messages())
print(messenger.get_new_messages())
print()

messenger.send_message("Black", "Hello3!")
print(messenger.get_messages())
print(messenger.get_new_messages())
print()