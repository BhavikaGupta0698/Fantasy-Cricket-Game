# -*- coding: utf-8 -*-
"""
Fantasy Cricket - Dream Team Selector
A PyQt5-based GUI application for selecting and managing cricket teams.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """Setup the main window UI components with enhanced styling."""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 675)
        MainWindow.move(100, 10)

        # Apply the new color scheme
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font: 14px 'Arial', sans-serif;
                color: #333333;
            }
            QPushButton {
                background-color: #008080;
                color: white;
                border: none;
                padding: 10px 20px;
                font: 14px 'Arial', sans-serif;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FFA500;
            }
            QListWidget {
                font: 14px 'Arial', sans-serif;
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 5px;
            }
            QMenuBar {
                background-color: #008080;
                color: white;
            }
            QMenuBar::item {
                spacing: 3px;
                padding: 10px 20px;
            }
            QMenuBar::item:selected {
                background-color: #FFA500;
            }
        """)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        MainWindow.setAutoFillBackground(False)

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)

        self.label_batsmen = QtWidgets.QLabel(self.central_widget)
        self.label_batsmen.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_batsmen.setFont(font)
        self.label_batsmen.setObjectName("label_batsmen")
        self.horizontalLayout_5.addWidget(self.label_batsmen)

        self.batsmen_count = QtWidgets.QLineEdit(self.central_widget)
        self.batsmen_count.setEnabled(False)
        self.batsmen_count.setObjectName("batsmen_count")
        self.horizontalLayout_5.addWidget(self.batsmen_count)

        self.label_bowlers = QtWidgets.QLabel(self.central_widget)
        self.label_bowlers.setEnabled(False)
        self.label_bowlers.setFont(font)
        self.label_bowlers.setObjectName("label_bowlers")
        self.horizontalLayout_5.addWidget(self.label_bowlers)

        self.bowlers_count = QtWidgets.QLineEdit(self.central_widget)
        self.bowlers_count.setEnabled(False)
        self.bowlers_count.setObjectName("bowlers_count")
        self.horizontalLayout_5.addWidget(self.bowlers_count)

        self.label_allrounders = QtWidgets.QLabel(self.central_widget)
        self.label_allrounders.setEnabled(False)
        self.label_allrounders.setFont(font)
        self.label_allrounders.setObjectName("label_allrounders")
        self.horizontalLayout_5.addWidget(self.label_allrounders)

        self.allrounders_count = QtWidgets.QLineEdit(self.central_widget)
        self.allrounders_count.setEnabled(False)
        self.allrounders_count.setObjectName("allrounders_count")
        self.horizontalLayout_5.addWidget(self.allrounders_count)

        self.label_wicketkeepers = QtWidgets.QLabel(self.central_widget)
        self.label_wicketkeepers.setEnabled(False)
        self.label_wicketkeepers.setFont(font)
        self.label_wicketkeepers.setObjectName("label_wicketkeepers")
        self.horizontalLayout_5.addWidget(self.label_wicketkeepers)

        self.wicketkeepers_count = QtWidgets.QLineEdit(self.central_widget)
        self.wicketkeepers_count.setEnabled(False)
        self.wicketkeepers_count.setObjectName("wicketkeepers_count")
        self.horizontalLayout_5.addWidget(self.wicketkeepers_count)

        spacerItem1 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)

        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QtWidgets.QFrame(self.central_widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)

        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.label_categories = QtWidgets.QLabel(self.central_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_categories.setFont(font)
        self.label_categories.setObjectName("label_categories")
        self.verticalLayout_8.addWidget(self.label_categories, 0, QtCore.Qt.AlignHCenter)

        self.groupBox = QtWidgets.QGroupBox(self.central_widget)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.radioButton_bat = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_bat.setObjectName("radioButton_bat")
        self.horizontalLayout_4.addWidget(self.radioButton_bat)

        self.radioButton_bowl = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_bowl.setObjectName("radioButton_bowl")
        self.horizontalLayout_4.addWidget(self.radioButton_bowl)

        self.radioButton_ar = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_ar.setObjectName("radioButton_ar")
        self.horizontalLayout_4.addWidget(self.radioButton_ar)

        self.radioButton_wk = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_wk.setObjectName("radioButton_wk")
        self.horizontalLayout_4.addWidget(self.radioButton_wk)

        self.radioButton_bat.toggled.connect(self.update_player_list)
        self.radioButton_bowl.toggled.connect(self.update_player_list)
        self.radioButton_ar.toggled.connect(self.update_player_list)
        self.radioButton_wk.toggled.connect(self.update_player_list)

        self.verticalLayout_8.addWidget(self.groupBox)

        self.available_players_list = QtWidgets.QListWidget(self.central_widget)
        self.available_players_list.setAutoFillBackground(True)
        self.available_players_list.setStyleSheet("color: rgb(0, 0, 127);\n"
                                                  "font: 75 12pt \"MS Shell Dlg 2\";")
        self.available_players_list.setAutoScroll(True)
        self.available_players_list.setObjectName("available_players_list")
        self.available_players_list.itemDoubleClicked.connect(self.remove_from_available_list)
        self.verticalLayout_8.addWidget(self.available_players_list)

        self.available_points_label = QtWidgets.QPushButton(self.central_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.available_points_label.setFont(font)
        self.available_points_label.setObjectName("available_points_label")
        self.verticalLayout_8.addWidget(self.available_points_label)

        self.label_criteria = QtWidgets.QLabel(self.central_widget)
        self.label_criteria.setText("")
        self.label_criteria.setPixmap(QtGui.QPixmap("criteria.jpg"))
        self.label_criteria.setAlignment(QtCore.Qt.AlignCenter)
        self.label_criteria.setObjectName("label_criteria")
        self.verticalLayout_8.addWidget(self.label_criteria)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        # Add "<<" and ">>" buttons
        self.verticalLayout_buttons = QtWidgets.QVBoxLayout()
        self.verticalLayout_buttons.setObjectName("verticalLayout_buttons")

        self.btn_remove_player = QtWidgets.QPushButton(self.central_widget)
        self.btn_remove_player.setText("<<")
        self.btn_remove_player.setFont(font)
        self.btn_remove_player.clicked.connect(self.move_left)
        self.verticalLayout_buttons.addWidget(self.btn_remove_player)

        self.btn_add_player = QtWidgets.QPushButton(self.central_widget)
        self.btn_add_player.setText(">>")
        self.btn_add_player.setFont(font)
        self.btn_add_player.clicked.connect(self.move_right)
        self.verticalLayout_buttons.addWidget(self.btn_add_player)

        self.horizontalLayout_3.addLayout(self.verticalLayout_buttons)

        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.label_selected_players = QtWidgets.QLabel(self.central_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_selected_players.setFont(font)
        self.label_selected_players.setAlignment(QtCore.Qt.AlignCenter)
        self.label_selected_players.setObjectName("label_selected_players")
        self.verticalLayout_9.addWidget(self.label_selected_players)

        self.team_name_label = QtWidgets.QLabel(self.central_widget)
        self.team_name_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.team_name_label.setFont(font)
        self.team_name_label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                           "background-color: rgb(0, 0, 127);\n"
                                           "color: rgb(255, 255, 255);")
        self.team_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.team_name_label.setObjectName("team_name_label")
        self.verticalLayout_9.addWidget(self.team_name_label)

        self.line_2 = QtWidgets.QFrame(self.central_widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_9.addWidget(self.line_2)

        spacerItem4 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem4)

        self.selected_players_list = QtWidgets.QListWidget(self.central_widget)
        self.selected_players_list.setStyleSheet("color: rgb(0, 0, 127);\n"
                                                "font: 75 12pt \"MS Shell Dlg 2\";")
        self.selected_players_list.setObjectName("selected_players_list")
        self.selected_players_list.itemDoubleClicked.connect(self.remove_from_selected_list)
        self.verticalLayout_9.addWidget(self.selected_players_list)

        self.used_points_label = QtWidgets.QPushButton(self.central_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.used_points_label.setFont(font)
        self.used_points_label.setObjectName("used_points_label")
        self.verticalLayout_9.addWidget(self.used_points_label)

        self.label_dream_team = QtWidgets.QLabel(self.central_widget)
        self.label_dream_team.setText("")
        self.label_dream_team.setPixmap(QtGui.QPixmap("dream1.png"))
        self.label_dream_team.setObjectName("label_dream_team")
        self.verticalLayout_9.addWidget(self.label_dream_team)

        self.horizontalLayout_3.addLayout(self.verticalLayout_9)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menu_bar.setObjectName("menu_bar")
        self.menuFile = QtWidgets.QMenu(self.menu_bar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menu_bar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionRules = QtWidgets.QAction(MainWindow)
        self.actionRules.setObjectName("actionRules")
        self.actionInstructions = QtWidgets.QAction(MainWindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Team)
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.triggered[QtWidgets.QAction].connect(self.menu_function)
        self.menuHelp.addAction(self.actionRules)
        self.menuHelp.addAction(self.actionInstructions)
        self.menu_bar.addAction(self.menuFile.menuAction())
        self.menu_bar.addAction(self.menuHelp.menuAction())

        ## Declaration of class attributes
        self.bat = 0
        self.bwl = 0
        self.ar = 0
        self.wk = 0
        self.avl = 1000
        self.used = 0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.customContextMenuRequested.connect(self.context_menu)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dream Team Selector"))
        self.label_batsmen.setText(_translate("MainWindow", "Batsmen"))
        self.label_bowlers.setText(_translate("MainWindow", "Bowlers"))
        self.label_allrounders.setText(_translate("MainWindow", "All Rounders"))
        self.label_wicketkeepers.setText(_translate("MainWindow", "Wicketkeepers"))
        self.label_categories.setText(_translate("MainWindow", "Player Categories"))
        self.radioButton_bat.setText(_translate("MainWindow", "BAT"))
        self.radioButton_bowl.setText(_translate("MainWindow", "BOWL"))
        self.radioButton_ar.setText(_translate("MainWindow", "AR"))
        self.radioButton_wk.setText(_translate("MainWindow", "WK"))
        self.available_points_label.setText(_translate("MainWindow", "Available Points : 1000"))
        self.label_selected_players.setText(_translate("MainWindow", "Selected Players"))
        self.team_name_label.setText(_translate("MainWindow", "???"))
        self.used_points_label.setText(_translate("MainWindow", "Points used : "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New Team"))
        self.actionOpen.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionRules.setText(_translate("MainWindow", "Rules"))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions"))
        self.actionQuit.setText(_translate("MainWindow", "Team Score"))

    def menu_function(self, action):
        """Handle menu actions."""
        txt = action.text()
        if txt == "New Team":
            self.new_team()
        elif txt == 'Save Team':
            self.save_team()
        elif txt == "Open Team":
            self.open_team()
        elif txt == "Team Score":
            self.show_team_score()

    def new_team(self):
        """Reset the team selection and prompt for a new team name."""
        self.bat = 0
        self.bwl = 0
        self.ar = 0
        self.wk = 0
        self.avl = 1000
        self.used = 0
        self.available_players_list.clear()
        self.selected_players_list.clear()
        self.team_name_label.setText("???")
        self.show_status()
        text, ok = QtWidgets.QInputDialog.getText(MainWindow, 'Dream Team Selector', 'Enter name of team:')
        if ok:
            self.team_name_label.setText(str(text))

    def save_team(self):
        """Save the selected team to the database."""
        selected = ",".join([self.selected_players_list.item(i).text() for i in range(self.selected_players_list.count())])
        self.save_team_to_db(self.team_name_label.text(), selected, self.used)

    def save_team_to_db(self, team_name, players, value):
        """
        Save the selected team to the database.

        Parameters:
        - team_name (str): The name of the team.
        - players (str): A comma-separated string of selected players.
        - value (int): The total value of the selected players.

        Raises:
        - ValueError: If the team does not have exactly 11 players.
        - sqlite3.Error: If there is a database error.
        """
        try:
            if self.bat + self.bwl + self.ar + self.wk != 11:
                raise ValueError("Insufficient players. A team must have exactly 11 players.")

            sql = "INSERT INTO teams (name, players, value) VALUES (?, ?, ?)"
            with conn:  # Using context manager for database operations
                conn.execute(sql, (team_name, players, value))

            self.show_dialog("Team Saved successfully")

        except ValueError as ve:
            self.show_dialog(f"Error: {ve}")
        except sqlite3.Error as e:
            self.show_dialog(f"Database error: {e}")
        except Exception as e:
            self.show_dialog(f"An unexpected error occurred: {e}")

    def open_team(self):
        """Open an existing team from the database."""
        try:
            sql = "SELECT name FROM teams"
            cur = conn.execute(sql)
            teams = [row[0] for row in cur.fetchall()]
            team, ok = QtWidgets.QInputDialog.getItem(MainWindow, "Dream Team Selector",
                                                        "Choose a team", teams, 0, False)
            if ok and team:
                self.load_team_from_db(team)
        except sqlite3.Error as e:
            self.show_dialog(f"Database error: {e}")
        except Exception as e:
            self.show_dialog(f"An unexpected error occurred: {e}")

    def load_team_from_db(self, team_name):
        """
        Load a team from the database.

        Parameters:
        - team_name (str): The name of the team to load.
        """
        try:
            self.bat = 0
            self.bwl = 0
            self.ar = 0
            self.wk = 0
            self.avl = 1000
            self.used = 0
            self.available_players_list.clear()
            self.selected_players_list.clear()
            self.team_name_label.setText(team_name)

            sql = "SELECT players, value FROM teams WHERE name=?"
            cur = conn.execute(sql, (team_name,))
            row = cur.fetchone()
            selected_players = row[0].split(',')
            self.selected_players_list.addItems(selected_players)
            self.used = row[1]
            self.avl = 1000 - row[1]

            for player in selected_players:
                sql = "SELECT ctg FROM stats WHERE player=?"
                cur = conn.execute(sql, (player,))
                row = cur.fetchone()
                ctgr = row[0]
                if ctgr == "BAT":
                    self.bat += 1
                if ctgr == "BWL":
                    self.bwl += 1
                if ctgr == "AR":
                    self.ar += 1
                if ctgr == "WK":
                    self.wk += 1

            self.show_status()

        except sqlite3.Error as e:
            self.show_dialog(f"Database error: {e}")
        except Exception as e:
            self.show_dialog(f"An unexpected error occurred: {e}")

    def context_menu(self, MainWindow):
        """Show context menu with additional options."""
        MainWindow.menu = QtWidgets.QMenu()
        MainWindow.menu.addAction("Profile")
        MainWindow.menu.triggered[QtWidgets.QAction].connect(MainWindow.profile)
        MainWindow.menu.exec_(QtGui.QCursor.pos())

    def update_player_list(self):
        """Update the list of available players based on selected category."""
        try:
            if self.team_name_label.text() == '???':
                self.show_dialog("Enter name of team")
                return

            category = self.get_selected_category()
            self.fill_player_list(category)

        except sqlite3.Error as e:
            self.show_dialog(f"Database error: {e}")
        except Exception as e:
            self.show_dialog(f"An unexpected error occurred: {e}")

    def get_selected_category(self):
        """Return the currently selected player category."""
        if self.radioButton_bat.isChecked():
            return 'BAT'
        if self.radioButton_bowl.isChecked():
            return 'BWL'
        if self.radioButton_ar.isChecked():
            return 'AR'
        if self.radioButton_wk.isChecked():
            return 'WK'
        return ''

    def fill_player_list(self, category):
        """Fill the list of available players for the given category."""
        try:
            self.available_players_list.clear()
            cursor = conn.execute("SELECT player FROM stats WHERE ctg=?", (category,))
            selected_players = [self.selected_players_list.item(i).text() for i in range(self.selected_players_list.count())]
            for row in cursor:
                if row[0] not in selected_players:
                    self.available_players_list.addItem(row[0])
        except sqlite3.Error as e:
            self.show_dialog(f"Database error: {e}")
        except Exception as e:
            self.show_dialog(f"An unexpected error occurred: {e}")

    def show_team_score(self):
        """Show the score dialog for the selected team."""
        from dlgscore import Ui_Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec()

    def criteria(self, category, item):
        """
        Check if the selected player meets the criteria for the team.

        Parameters:
        - category (str): The category of the player.
        - item (QListWidgetItem): The selected player item.

        Returns:
        - bool: True if the player meets the criteria, False otherwise.
        """
        if self.selected_players_list.count() >= 11:
            self.show_dialog("Cannot select more than 11 players")
            return False

        msg = ''
        if category == "BAT" and self.bat >= 5:
            msg = "Batsmen not more than 5"
        if category == "BWL" and self.bwl >= 5:
            msg = "Bowlers not more than 5"
        if category == "AR" and self.ar >= 3:
            msg = "Allrounders not more than 3"
        if category == "WK" and self.wk >= 1:
            msg = "Wicketkeepers not more than 1"
        if msg or self.avl <= 0:
            msg = 'You have exhausted your points'
            self.show_dialog(msg)
            return False

        if category == "BAT":
            self.bat += 1
        if category == "BWL":
            self.bwl += 1
        if category == "AR":
            self.ar += 1
        if category == "WK":
            self.wk += 1

        cursor = conn.execute("SELECT player, value FROM stats WHERE player=?", (item.text(),))
        row = cursor.fetchone()
        self.avl -= int(row[1])
        self.used += int(row[1])
        return True

    def show_status(self):
        """Update the status labels with current team composition and points."""
        self.batsmen_count.setText(str(self.bat))
        self.bowlers_count.setText(str(self.bwl))
        self.allrounders_count.setText(str(self.ar))
        self.wicketkeepers_count.setText(str(self.wk))
        self.available_points_label.setText(f"Available Points : {self.avl}")
        self.used_points_label.setText(f"Points used : {self.used}")

    def remove_from_available_list(self, item):
        """Remove a player from the available list and add to the selected list."""
        category = self.get_selected_category()
        if self.criteria(category, item):
            self.available_players_list.takeItem(self.available_players_list.row(item))
            self.selected_players_list.addItem(item.text())
            self.show_status()

    def show_dialog(self, msg):
        """Show a message dialog with the given message."""
        Dialog = QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Dream Team Selector")
        ret = Dialog.exec()

    def remove_from_selected_list(self, item):
        """Remove a player from the selected list and add back to the available list."""
        self.selected_players_list.takeItem(self.selected_players_list.row(item))
        cursor = conn.execute("SELECT player, value, ctg FROM stats WHERE player=?", (item.text(),))
        row = cursor.fetchone()
        self.avl += int(row[1])
        self.used -= int(row[1])
        category = row[2]

        if category == "BAT":
            self.bat -= 1
            if self.radioButton_bat.isChecked():
                self.available_players_list.addItem(item.text())
        if category == "BWL":
            self.bwl -= 1
            if self.radioButton_bowl.isChecked():
                self.available_players_list.addItem(item.text())
        if category == "AR":
            self.ar -= 1
            if self.radioButton_ar.isChecked():
                self.available_players_list.addItem(item.text())
        if category == "WK":
            self.wk -= 1
            if self.radioButton_wk.isChecked():
                self.available_players_list.addItem(item.text())

        self.show_status()

    def move_left(self):
        """Move selected players from the selected list to the available list."""
        selected_items = self.selected_players_list.selectedItems()
        for item in selected_items:
            self.selected_players_list.takeItem(self.selected_players_list.row(item))
            self.available_players_list.addItem(item.text())
        self.show_status()

    def move_right(self):
        """Move selected players from the available list to the selected list."""
        if self.selected_players_list.count() >= 11:
            self.show_dialog("Cannot select more than 11 players")
            return
        selected_items = self.available_players_list.selectedItems()
        for item in selected_items:
            self.available_players_list.takeItem(self.available_players_list.row(item))
            self.selected_players_list.addItem(item.text())
        self.show_status()

if __name__ == "__main__":
    import sys
    conn = sqlite3.connect('fantasy.db')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
