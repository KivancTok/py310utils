from dataclasses import dataclass


@dataclass
class CalendarEvent:
    name: str
    date: list


class Calendar:
    def __init__(self, events: list[CalendarEvent]):
        self.events = events

    def get_events_data(self):
        for i in range(self.events.__len__()):
            print(f"""Event {i + 1} name: {self.events[i].name}
Event {i + 1} date: {self.events[i].date[0]}/{self.events[i].date[1]}""")

    def get_events_by_date(self, date: list):
        for i in range(self.events.__len__()):
            if self.events[i].date == date:
                print(f"""Event {i + 1} name: {self.events[i].name}
Event {i + 1} date: {self.events[i].date[0]}/{self.events[i].date[1]}""")

    def get_events_by_name(self, name: str):
        for i in range(self.events.__len__()):
            if self.events[i].name == name:
                print(f"""Event {i + 1} name: {self.events[i].name}
Event {i + 1} date: {self.events[i].date[0]}/{self.events[i].date[1]}""")


if __name__ == "__main__":
    a = CalendarEvent("a", [4, 7])
    ev = CalendarEvent("ev", [4, 7])
    b = CalendarEvent("b", [4, 6])
    c = Calendar(events=[a, b, ev])
    c.get_events_data()
    c.get_events_by_date([4, 7])
    c.get_events_by_name("a")
    c.get_events_by_name("b")
    c.get_events_by_date([4, 6])

