import tkinter as tk
from tkinter import messagebox
from tkinter import IntVar
import requests
from abstract_player import AbstractPlayer
from add_guard_popup import AddGuardPopup
from add_forward_popup import AddForwardPopup
from add_center_popup import AddCenterPopup
from remove_popup import RemovePopup
from update_guard_popup import UpdateGuardPopup
from update_center_popup import UpdateCenterPopup
from update_forward_popup import UpdateForwardPopup
import json

class MainAppController(tk.Frame):
    """ Main Application for GUI """

    _selected_type = None

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="Player Stats").grid(row=1, column=3)
        self._stats_listbox = tk.Listbox(self, height=8, width=160)
        self._stats_listbox.grid(row=2, column=1, columnspan=5)

        tk.Label(self, text="Guards").grid(row=3, column=3)
        self._guards_listbox = tk.Listbox(self, height=8, width=160)
        self._guards_listbox.grid(row=4, column=1, columnspan=5)

        tk.Label(self, text="Forwards").grid(row=5, column=3)
        self._forwards_listbox = tk.Listbox(self, height=8, width=160)
        self._forwards_listbox.grid(row=6, column=1, columnspan=5)

        tk.Label(self, text="Centers").grid(row=7, column=3)
        self._centers_listbox = tk.Listbox(self, height=8, width=160)
        self._centers_listbox.grid(row=8, column=1, columnspan=5)


        self._selection = IntVar()

        tk.Button(self, text="Add Guard", command=self._add_guard).grid(row=9, column=1)
        tk.Button(self, text="Add Forward", command=self._add_forward).grid(row=9, column=2)
        tk.Button(self, text="Add Center", command=self._add_center).grid(row=9, column=3)
        tk.Button(self, text="Remove Guard", command=self._remove_player).grid(row=9, column=4)
        tk.Button(self, text="Update Guard", command=self._update_guard).grid(row=9, column=5)
        tk.Button(self, text="Update Forward", command=self._update_forward).grid(row=9, column=6)
        tk.Button(self, text="Update Center", command=self._update_center).grid(row=9, column=7)


        self._get_player_stats()
        self._update_guards_list()
        self._update_centers_list()
        self._update_forwards_list()


    def _update_guard(self):
        """remove player"""
        self._popup_win = tk.Toplevel()
        self._popup = UpdateGuardPopup(self._popup_win, self._close_remove_cb)

    def _update_center(self):
        """remove player"""
        self._popup_win = tk.Toplevel()
        self._popup = UpdateCenterPopup(self._popup_win, self._close_remove_cb)

    def _update_forward(self):
        """remove player"""
        self._popup_win = tk.Toplevel()
        self._popup = UpdateForwardPopup(self._popup_win, self._close_remove_cb)

    def _remove_player(self):
        """remove player"""
        self._popup_win = tk.Toplevel()
        self._popup = RemovePopup(self._popup_win, self._close_remove_cb)
    
    def _add_guard(self):
        """ Add Car Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddGuardPopup(self._popup_win, self._close_guard_cb)

    def _close_guard_cb(self):
        """ Close Add Car Popup """
        self._popup_win.destroy()
        self._get_player_stats()
        self._update_guards_list()

    def _close_remove_cb(self):
        """ Close Add Car Popup """
        self._popup_win.destroy()
        self._get_player_stats()
        self._update_guards_list()
        self._update_centers_list()
        self._update_forwards_list()


    def _add_forward(self):
        """ Add Truck Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddForwardPopup(self._popup_win, self._close_forward_cb)

    def _close_forward_cb(self):
        """ Close Add Truck Popup """
        self._popup_win.destroy()
        self._get_player_stats()
        self._update_forwards_list()

    def _add_center(self):
        """ Add Truck Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddCenterPopup(self._popup_win, self._close_center_cb)

    def _close_center_cb(self):
        """ Close Add Truck Popup """
        self._popup_win.destroy()
        self._get_player_stats()
        self._update_centers_list()

    def _update_product(self):

        player = self._


    def _update_guards_list(self):
        lines = []
        
        url = 'http://localhost:5000/playermanager/players/all/guard'
        response = requests.get(url)
        guards = response.json()
        lines.append("Guards")
        for guard in guards:
            lines.append(guard)
        
        lines.append("")

        self._guards_listbox.delete(0, tk.END)
        for line in lines:
            self._guards_listbox.insert(tk.END, line)

    def _update_forwards_list(self):
        lines = []

        url = 'http://localhost:5000/playermanager/players/all/forward'
        response = requests.get(url)
        forwards = response.json()
        lines.append("Forwards")
        for forward in forwards:
            lines.append(forward)

        lines.append("")

        self._forwards_listbox.delete(0, tk.END)
        for line in lines:
            self._forwards_listbox.insert(tk.END, line)

    def _update_centers_list(self):
        lines = []
        url = 'http://localhost:5000/playermanager/players/all/center'
        response = requests.get(url)
        centers = response.json()
        lines.append("Centers")
        for center in centers:
            lines.append(center)

        lines.append("")

        self._centers_listbox.delete(0, tk.END)
        for line in lines:
            self._centers_listbox.insert(tk.END, line)


    def _get_player_stats(self):
        response = requests.get('http://localhost:5000/playermanager/playerstats')
        if response.status_code == 200:
            data = response.json()
            num_players = data['num_players']
            num_guards = data['num_guards']
            num_forwards = data['num_forwards']
            num_centers = data['num_centers']
            avg_years_played = data['avg_years_played']


            self._stats_listbox.delete(0, tk.END)
            self._stats_listbox.insert(tk.END, "Player Statistics")
            self._stats_listbox.insert(tk.END, "")
            self._stats_listbox.insert(tk.END, "Number of players: " + str(num_players))
            self._stats_listbox.insert(tk.END, "Number of Guards: " + str(num_guards))
            self._stats_listbox.insert(tk.END, "Number of Forwards: " + str(num_forwards))
            self._stats_listbox.insert(tk.END, "Number of Centers: " + str(num_centers))
            self._stats_listbox.insert(tk.END, "Average years played: " + str(avg_years_played))







if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()