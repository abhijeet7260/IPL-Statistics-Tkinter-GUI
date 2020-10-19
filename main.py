import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import matplotlib.ticker
import warnings as war
try:
    import tkinter as tk
    import tkinter.font as font
except ImportError:
    import Tkinter as tk
    import tkFont as font
from PIL import ImageTk, Image

with war.catch_warnings():
    war.filterwarnings("ignore")
    matches = pd.read_csv('matches.csv')
    matches['winner'].fillna('Draw', inplace=True)
    matches.replace(['Mumbai Indians', 'Kolkata Knight Riders', 'Royal Challengers Bangalore', 'Deccan Chargers',
                     'Chennai Super Kings',
                     'Rajasthan Royals', 'Delhi Daredevils', 'Kings XI Punjab',
                     'Sunrisers Hyderabad']
                    , ['MI', 'KKR', 'RCB', 'SRH', 'CSK', 'RR', 'DD', 'KXIP', 'SRH'], inplace=True)
    df_temp = pd.DataFrame(matches)
    m_team1 = df_temp['team1']
    m_team2 = df_temp['team2']
    m_toss = df_temp['toss_winner']
    m_win = df_temp['winner']
    m_team1 = list(m_team1)
    m_team2 = list(m_team2)
    m_win = list(m_win)
    encode = {'team1': {'MI': 1, 'KKR': 2, 'RCB': 3, 'CSK': 4, 'RR': 5, 'DD': 6, 'KXIP': 7, 'SRH': 8},
              'team2': {'MI': 1, 'KKR': 2, 'RCB': 3, 'CSK': 4, 'RR': 5, 'DD': 6, 'KXIP': 7, 'SRH': 8},
              'toss_winner': {'MI': 1, 'KKR': 2, 'RCB': 3, 'CSK': 4, 'RR': 5, 'DD': 6, 'KXIP': 7, 'SRH': 8},
              'winner': {'MI': 1, 'KKR': 2, 'RCB': 3, 'CSK': 4, 'RR': 5, 'DD': 6, 'KXIP': 7, 'SRH': 8}}
    m_venue = {"Wankhede": 1, "Brabourne": 2,
               "New Wanderer": 3, "SVNS": 4,
               "Sheikh Zayed": 5, "SuperSport": 6,
               "Punjab Cricket": 7,
               "St George": 8, "Kingsmead": 9,
               "Dr.YSR Reddy": 10,
               "Sharjah": 11, "Sawai Mansingh": 12,
               "Beer Diamond": 13, "M C A": 14,
               "Rajiv Gandhi": 15, "Barabati": 16,
               "Feroz Shah": 17, "Newlands": 18, "V C A": 19,
               "Eden Gardens": 20, "JSCA Int.": 21,
               "Buffalo Park": 22, "Chinaswamy": 23, "S R Sahara": 24, "Outsurance": 25, "DY Patil": 26,
               "H P Stadium": 27, "Chidambaram": 28,
               "PCA Stadium": 29, "Sardar Patel": 30}
    matches.replace(encode, inplace=True)
    dicVal = encode['winner']
    df = pd.DataFrame(matches)
    temp4 = df['team1'].value_counts(sort=False)
    temp5 = df['team2'].value_counts(sort=False)
    temp1 = temp4 + temp5
    temp2 = df['winner'].value_counts(sort=False)
    temp3 = df['venue'].value_counts(sort=False)
    temp1 = np.array(temp1)
    temp2 = np.array(temp2)
    team_name = ['MI', 'KKR', 'RCB', 'CSK', 'RR', 'DD', 'KXIP', 'SRH']


    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2., height, '%d' % int(height), ha='center', va='bottom')


    N = 8
    ind = np.arange(N)
    width = 0.35
    rect4 = plt.bar(ind, temp1, width, label='Matches Played')
    rect5 = plt.bar(ind + width, temp2, width, label='Matches Won')
    plt.ylabel("No. of Matches----->")
    plt.xlabel('Teams----->')
    plt.title("Total matches played vs Matches Won")
    plt.xticks(ind + width / 2, ('MI', 'KKR', 'RCB', 'SRH', 'CSK', 'RR', 'DD', 'KXIP', 'SRH'))
    autolabel(rect4)
    autolabel(rect5)
    plt.legend(loc='best')
    plt.savefig('pic/1.png', dpi=110, bbox_inches='tight')
    plt.close()
    rect6 = plt.bar(list(m_venue.keys()), list(temp3), color='#90ee90')
    plt.title('All matches per Venue(2008-16)')
    plt.xticks(rotation=90)
    plt.tight_layout()
    autolabel(rect6)
    plt.ylabel("No. of Matches played----->")
    plt.xlabel('Venues----->')
    plt.savefig('pic/2.png', dpi=103, bbox_inches='tight')
    plt.close()
    t1 = 'MI'
    def analysis1(t1):
        team_win = [0, 0, 0, 0, 0, 0, 0, 0]
        team_played = [0, 0, 0, 0, 0, 0, 0, 0]
        team_toss = [0, 0, 0, 0, 0, 0, 0, 0]
        team_name = ['MI', 'KKR', 'RCB', 'CSK', 'RR', 'DD', 'KXIP', 'SRH']
        i = 0
        for val in m_team1:
            if val == t1 and m_win[i] == t1:
                temp = m_team2[i]
                team_win[dicVal[temp] - 1] = team_win[dicVal[temp] - 1] + 1
                i = i + 1
            else:
                i = i + 1
        i = 0
        for val in m_team2:
            if val == t1 and m_win[i] == t1:
                temp = m_team1[i]
                team_win[dicVal[temp] - 1] = team_win[dicVal[temp] - 1] + 1
                i = i + 1
            else:
                i = i + 1
        i = 0
        for val in m_team1:
            if val == t1:
                temp = m_team2[i]
                team_played[dicVal[temp] - 1] = team_played[dicVal[temp] - 1] + 1
                i = i + 1
            else:
                i = i + 1
        i = 0
        for val in m_team2:
            if val == t1:
                temp = m_team1[i]
                team_played[dicVal[temp] - 1] = team_played[dicVal[temp] - 1] + 1
                i = i + 1
            else:
                i = i + 1
        i = 0
        for val in m_team1:
            if val == t1:
                t_win = m_toss[i]
                temp = m_team2[i]
                if t_win == t1:
                    team_toss[dicVal[temp] - 1] = team_toss[dicVal[temp] - 1] + 1
                    i = i + 1
                else:
                    i = i + 1
            else:
                i = i + 1
        i = 0
        for val in m_team2:
            if val == t1:
                t_win = m_toss[i]
                temp = m_team1[i]
                if t_win == t1:
                    team_toss[dicVal[temp] - 1] = team_toss[dicVal[temp] - 1] + 1
                    i = i + 1
                else:
                    i = i + 1
            else:
                i = i + 1
        team_win.remove(0)
        team_played.remove(0)
        team_toss.remove(0)
        team_name.remove(t1)
        ind = np.arange(7)
        width = 0.25
        rect1 = plt.bar(ind + 0.00, team_played, width, label='Total Match Played')
        rect2 = plt.bar(ind + 0.25, team_toss, width, label='Total Toss Won')
        rect3 = plt.bar(ind + 0.50, team_win, width, label='Total Match Won')
        plt.xlabel("No. of Matches--->")
        plt.ylabel("Teams Played--->")
        plt.title(t1 + ' stats vs other teams')
        plt.xticks(ind + 0.50 / 3, (team_name))
        locator = matplotlib.ticker.MultipleLocator(2)
        plt.gca().yaxis.set_major_locator(locator)
        formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
        plt.gca().yaxis.set_major_formatter(formatter)
        autolabel(rect1)
        autolabel(rect2)
        autolabel(rect3)
        plt.legend(loc='best')
        plt.savefig('pic/3.png', dpi=100)
        plt.close()


    def classification_model(model, data, predictors, outcome):
        model.fit(data[predictors], data[outcome])
        kf = KFold(n_splits=5)
        for train, test in kf.split(data):
            train_predictors = (data[predictors].iloc[train, :])
            train_target = data[outcome].iloc[train]
            model.fit(train_predictors, train_target)
            predictions = model.predict(data[predictors])
        accuracy = metrics.accuracy_score(data[outcome], predictions)
        return accuracy


    model = RandomForestClassifier(n_estimators=100)
    outcome_var = ['winner']


    # GUI
    def Analysis():
        ana = tk.Toplevel()
        ana.attributes("-fullscreen", True)
        filename = tk.PhotoImage(file="pic/back1.png")
        background_label = tk.Label(ana, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        ana.configure(background='black')

        def makeSomething(value):
            global t1
            t1 = value
            analysis1(t1)
            ana.destroy()
            Analysis()

        frame = tk.Frame(ana)
        frame.pack(side='top')
        mainbutton1 = tk.Button(frame, image=photo1, bg='blue', command=ana.destroy)
        mainbutton1.pack(side='left')
        indibutton1 = tk.Button(frame, image=photo2, bg='blue')
        indibutton1.pack(side='left')
        indibutton2 = tk.Button(frame, image=photo3, bg='blue', command=predict)
        indibutton2.pack(side='left')
        filename2 = tk.PhotoImage(file="pic/analabel.png")
        tk.Label(ana, image=filename2).pack(side='top')
        team_frame1 = tk.Frame(ana)
        team_frame1.pack(side='top')
        tk.Button(team_frame1, text="Mumbai Indians", fg="white", font=style1, bg='black', padx=10,
                  command=lambda *args: makeSomething('MI')).pack(side='left')
        tk.Button(team_frame1, text="Kolkata Knight Riders", fg="white", font=style1, bg='black', padx=10,
                  command=lambda *args: makeSomething('KKR')).pack(side='left')
        tk.Button(team_frame1, text="Royal Challengers Bangalore", font=style1, fg="white", bg='black', padx=10,
                  command=lambda *args: makeSomething('RCB')).pack(side='left')
        tk.Button(team_frame1, text="Chennai Super Kings", fg="white", font=style1, bg='black', padx=10,
                  command=lambda *args: makeSomething('CSK')).pack(side='left')
        team_frame2 = tk.Frame(ana)
        team_frame2.pack(side='top')
        tk.Button(team_frame2, text="Rajasthan Royals", fg="white", font=style1, bg='black', padx=10,
                  command=lambda *args: makeSomething('RR')).pack(side='left')
        tk.Button(team_frame2, text="Delhi Daredevils", fg="white", bg='black', font=style1, padx=10,
                  command=lambda *args: makeSomething('DD')).pack(side='left')
        tk.Button(team_frame2, text="Kings XI Punjab", fg="white", bg='black', font=style1, padx=10,
                  command=lambda *args: makeSomething('KXIP')).pack(side='left')
        tk.Button(team_frame2, text="Sunrisers Hyderabad", fg="white", bg='black', font=style1, padx=10,
                  command=lambda *args: makeSomething('SRH')).pack(side='left')
        img1 = ImageTk.PhotoImage(Image.open("pic/3.png"))
        tk.Label(ana, image=img1).place(x=400, y=250)
        ana.mainloop()


    def predict():
        pre = tk.Toplevel()
        pre.configure(background='black')
        pre.attributes("-fullscreen", True)
        filename = ImageTk.PhotoImage(Image.open("pic/pre.jpg"))
        background_label = tk.Label(pre, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        frame = tk.Frame(pre)
        frame.pack(side='top')
        mainbutton1 = tk.Button(frame, image=photo1, bg='blue', command=pre.destroy)
        mainbutton1.pack(side='left')
        indibutton1 = tk.Button(frame, image=photo2, bg='blue', command=Analysis)
        indibutton1.pack(side='left')
        indibutton2 = tk.Button(frame, image=photo3, bg='blue')
        indibutton2.pack(side='left')

        def get_input():
            team1 = e1.get()
            team2 = e2.get()
            team_name1 = ['MI', 'KKR', 'RCB', 'CSK', 'RR', 'DD', 'KXIP', 'SRH']
            ML_result = tk.StringVar()
            if team1 in team_name1 and team2 in team_name1:
                if team1 == team2:
                    ML_result.set('Both teams cannot be the same')
                else:
                    predictor_var = ['team1', 'team2']
                    s = classification_model(model, df, predictor_var, outcome_var)
                    inputs = [dicVal[team1], dicVal[team2]]
                    inputs = np.array(inputs).reshape((1, -1))
                    output = model.predict(inputs)
                    result = str(list(dicVal.keys())[list(dicVal.values()).index(output)])
                    if result != team1 or result != team2:
                        i = 0
                        team1_win = 0
                        team2_win = 0
                        for val in m_team1:
                            if val == team1 and m_win[i] == team1:
                                team1_win = team1_win + 1
                            else:
                                i = i + 1
                                i = 0
                                for val in m_team2:
                                    if val == team1 and m_win[i] == team1:
                                        team1_win = team1_win + 1

                                    else:
                                        i = i + 1
                        for val in m_team1:
                            if val == team2 and m_win[i] == team2:
                                team2_win = team2_win + 1
                            else:
                                i = i + 1
                                i = 0
                                for val in m_team2:
                                    if val == team2 and m_win[i] == team2:
                                        team2_win = team2_win + 1

                                    else:
                                        i = i + 1
                        if team1_win > team2_win:
                            result = team1
                        elif team1_win < team2_win:
                            result = team2
                        else:
                            result = team1
                    path = 'pic/'+result + '.png'
                    img12 = ImageTk.PhotoImage(Image.open(path))
                    panel = tk.Label(pre, image=img12)
                    panel.photo = img12
                    panel.place(x=900, y=200)
                    ML_result.set(result + '  will win with : ' + str(int(s * 100)) + ' % Accuracy')
            else:
                ML_result.set('Please check the name of above teams')
            tk.Label(pre, textvariable=ML_result, bg='black', fg='#90ee90', font=fontcool).place(x=350, y=500)

        def clear():
            pre.destroy()
            predict()

        prelabel1 = tk.PhotoImage(file="pic/prelabel1.png")
        prelabel2 = tk.PhotoImage(file="pic/prelabel2.png")
        tk.Label(pre, image=prelabel1).place(x=20, y=250)
        large_font = ('Verdana', 20)
        fontcool = ('Verdana', 24)
        e1 = tk.Entry(pre, font=large_font)
        e1.place(x=500, y=260)
        tk.Label(pre, image=prelabel2).place(x=20, y=350)
        e2 = tk.Entry(pre, font=large_font)
        e2.place(x=500, y=360)
        tk.Button(pre, text='Prediction', fg='white', bg='black', font=style, command=get_input).place(x=250, y=450)
        tk.Button(pre, text='Clear', fg='white', bg='black', font=style, command=clear).place(x=450, y=450)
        pre.mainloop()




    front = tk.Tk()
    front.attributes("-fullscreen", True)
    style = font.Font(family='Helvetica', size=18, weight='bold')
    style1 = font.Font(family='Helvetica', size=12, weight='bold')
    style2 = font.Font(family='Impact', size=16, weight='bold')
    style3 = font.Font(family='Impact', size=32, weight='bold')
    filename = tk.PhotoImage(file="pic/back1.png")
    filename1 = tk.PhotoImage(file="pic/labelback.png")
    background_label = tk.Label(front, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    frame = tk.Frame(front)
    frame.pack(side='top')
    photo1 = tk.PhotoImage(file="pic/overview.png")
    photo2 = tk.PhotoImage(file="pic/indi.png")
    photo3 = tk.PhotoImage(file="pic/pre.png")
    
    mainbutton = tk.Button(frame, image=photo1, bg='blue')
    mainbutton.pack(side='left')
    indibutton = tk.Button(frame, image=photo2, bg='blue', command=Analysis)
    indibutton.pack(side='left')
    indibutton2 = tk.Button(frame, image=photo3, bg='blue', command=predict)
    indibutton2.pack(side='left')
    tk.Label(front, image=filename1, text="IPL Statistics (2008-2016)", font=style3, fg='red').place(x=450, y=100)
    img1 = ImageTk.PhotoImage(Image.open("pic/1.png"))
    img2 = ImageTk.PhotoImage(Image.open("pic/2.png"))
    imglabel1 = tk.Label(front, image=img1).place(x=50, y=200)
    imglabel2 = tk.Label(front, image=img2).place(x=700, y=200)
    front.mainloop()