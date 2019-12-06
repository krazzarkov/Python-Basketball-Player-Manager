import tkinter as tk
from tkinter import messagebox
import requests


class RemovePopup(tk.Frame):
    """ Popup Frame to Sell a Vehicle """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="Player ID:").grid(row=1, column=1)
        self._player_id = tk.Entry(self)
        self._player_id.grid(row=1, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=7, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=7, column=2)

    def _submit_cb(self):
        """ Submit Sell Vehicle """
        data = {}
        data['player_id'] = self._player_id.get()

        self._remove_player(data)

    def _remove_player(self, data):
        """ Adds a point to the backend grid """
        headers = {"content-type": "application/json"}
        response = requests.delete("http://127.0.0.1:5000/playermanager/players/" + str(data["player_id"]))

        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showerror("Error", "Cannot remove player because: " + response.text)