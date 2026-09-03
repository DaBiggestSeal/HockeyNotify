from plyer import notification

class Notify:
    def Send(home_team:str, away_team:str, message:str):
        notification.notify(title=f"{home_team} : ")