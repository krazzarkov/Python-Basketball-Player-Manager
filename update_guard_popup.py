import tkinter as tk
from tkinter import messagebox
import requests
from abstract_player import AbstractPlayer


class UpdateGuardPopup(tk.Frame):
    """ Popup fram to add a Center """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="Player ID:").grid(row=1, column=1)
        self._player_id = tk.Entry(self)
        self._player_id.grid(row=1, column=2)
        tk.Label(self, text="First Name:").grid(row=2, column=1)
        self._first_name = tk.Entry(self)
        self._first_name.grid(row=2, column=2)
        tk.Label(self, text="Last Name").grid(row=3, column=1)
        self._last_name = tk.Entry(self)
        self._last_name.grid(row=3, column=2)
        tk.Label(self, text="Height:").grid(row=4, column=1)
        self._height = tk.Entry(self)
        self._height.grid(row=4, column=2)
        tk.Label(self, text="Weight:").grid(row=5, column=1)
        self._weight = tk.Entry(self)
        self._weight.grid(row=5, column=2)
        tk.Label(self, text="Year Drafted:").grid(row=6, column=1)
        self._year_drafted = tk.Entry(self)
        self._year_drafted.grid(row=6, column=2)
        tk.Label(self, text="Number of Assists:").grid(row=7, column=1)
        self._num_assists = tk.Entry(self)
        self._num_assists.grid(row=7, column=2)
        tk.Label(self, text="Number of Steals:").grid(row=8, column=1)
        self._num_steals = tk.Entry(self)
        self._num_steals.grid(row=8, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=11, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=11, column=2)

    def _submit_cb(self):

        data = {}
        data['player_id'] = int(self._player_id.get())
        data['first_name'] = str(self._first_name.get())
        data['last_name'] = str(self._last_name.get())
        data['height'] = int(self._height.get())
        data['weight'] = int(self._weight.get())
        data['year_drafted'] = int(self._year_drafted.get())
        data['player_type'] = str("guard")
        data['num_assists'] = int(self._num_assists.get())
        data['num_steals'] = int(self._num_steals.get())

        url = 'http://localhost:5000/playermanager/players/' + str(data["player_id"])
        print(url)
        response = requests.put(url, json=data)
        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showwarning("Error", "Update Player Request Failed")
