# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(25, -1, 25, -1)
        self.verticalLayout.setObjectName("verticalLayout")

        # Team selection layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Team label
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)

        # Team combobox
        self.team_combobox = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.team_combobox.setFont(font)
        self.team_combobox.setObjectName("team_combobox")

        # Load teams from database
        conn = sqlite3.connect('fantasy.db')
        self.horizontalLayout.addWidget(self.team_combobox)
        sql = "select name from teams"
        cur = conn.execute(sql)
        for row in cur:
            self.team_combobox.addItem(row[0])

        # Match selection
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)

        # Match combobox
        self.match_combobox = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.match_combobox.setFont(font)
        self.match_combobox.setObjectName("match_combobox")

        # Get all match tables from database in ascending order
        cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'match%' ORDER BY name ASC")
        matches = cur.fetchall()
        print("Fetched matches:", matches)  # Debugging line
        for match in matches:
            self.match_combobox.addItem(match[0])

        conn.close()
        self.horizontalLayout.addWidget(self.match_combobox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Separator line
        self.line = QtWidgets.QFrame(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        # Calculate button and total score layout
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Players label
        self.label_1 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addWidget(self.label_1)

        # Score label
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # Another separator
        self.line_2 = QtWidgets.QFrame(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)

        # Player and score list layout
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # Players list
        self.lw1 = QtWidgets.QListWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lw1.setFont(font)
        self.lw1.setObjectName("lw1")
        self.horizontalLayout_4.addWidget(self.lw1)

        # Spacer
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)

        # Scores list
        self.lw2 = QtWidgets.QListWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lw2.setFont(font)
        self.lw2.setObjectName("lw2")
        self.horizontalLayout_4.addWidget(self.lw2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        # Final separator
        self.line_3 = QtWidgets.QFrame(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)

        # Calculate button and total score layout
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Calculate button
        self.calculate_button = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.calculate_button.setFont(font)
        self.calculate_button.setObjectName("calculate_button")
        self.calculate_button.clicked.connect(self.calculate_score)
        self.horizontalLayout_3.addWidget(self.calculate_button)

        # Spacer
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)

        # Total score label
        self.total_score_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.total_score_label.setFont(font)
        self.total_score_label.setObjectName("total_score_label")
        self.horizontalLayout_3.addWidget(self.total_score_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def calculate_score(self):
        """Calculate scores for selected team and match"""
        import sqlite3
        conn = sqlite3.connect('fantasy.db')

        # Get selected team and match
        team = self.team_combobox.currentText()
        match = self.match_combobox.currentText()

        # Clear previous results
        self.lw1.clear()
        self.lw2.clear()

        # Get team players
        sql1 = f"select players, value from teams where name='{team}'"
        cur = conn.execute(sql1)
        row = cur.fetchone()
        selected = row[0].split(',')
        self.lw1.addItems(selected)

        # Calculate scores for each player
        teamttl = 0
        for i in range(self.lw1.count()):
            ttl, batscore, bowlscore, fieldscore = 0, 0, 0, 0
            nm = self.lw1.item(i).text()

            # Get player stats from selected match
            cursor = conn.execute(f"select * from {match} where player='{nm}'")
            row = cursor.fetchone()

            if row:
                # Calculate batting score
                batscore = int(row[1]/2)  # Runs
                if batscore >= 50: batscore += 5
                if batscore >= 100: batscore += 10
                if row[1] > 0:
                    sr = row[1]/row[2]  # Strike rate
                    if sr >= 80 and sr < 100: batscore += 2
                    if sr >= 100: batscore += 4
                batscore += row[3]  # Fours
                batscore += 2*row[4]  # Sixes

                # Calculate bowling score
                bowlscore = row[8]*10  # Wickets
                if row[8] >= 3: bowlscore += 5
                if row[8] >= 5: bowlscore += 10
                if row[7] > 0:
                    er = 6*row[7]/row[5]  # Economy rate
                    if er <= 2: bowlscore += 10
                    if er > 2 and er <= 3.5: bowlscore += 7
                    if er > 3.5 and er <= 4.5: bowlscore += 4

                # Calculate fielding score
                fieldscore = (row[9] + row[10] + row[11])*10  # Catches + Stumpings + Run outs

                # Total score
                ttl = batscore + bowlscore + fieldscore

            self.lw2.addItem(str(ttl))
            teamttl += ttl

        self.total_score_label.setText(str(teamttl))
        conn.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Fantasy Score Calculator"))
        self.label_5.setText(_translate("Dialog", "Choose Team"))
        self.label_4.setText(_translate("Dialog", "Choose Match"))
        self.label_1.setText(_translate("Dialog", "Players"))
        self.label_2.setText(_translate("Dialog", "Score"))
        self.calculate_button.setText(_translate("Dialog", "Calculate Score"))
        self.total_score_label.setText(_translate("Dialog", "00"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
