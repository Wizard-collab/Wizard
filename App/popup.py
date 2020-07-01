import popup_ui
import save_popup_ui
from wizard.prefs.user import user
from wizard.vars import defaults

class popup():
	def __init__(self):
		self.popup_prefs_dic = user().get_popup_prefs()
		self.enable = self.popup_prefs_dic[defaults._popup_enable_key_]
		self.sound = self.popup_prefs_dic[defaults._popup_sound_key_]
		self.duration = int(self.popup_prefs_dic[defaults._popup_duration_key_])*1000
		self.creation = self.popup_prefs_dic[defaults._popup_creation_key_]
		self.publish = self.popup_prefs_dic[defaults._popup_publish_key_]
		self.playblast = self.popup_prefs_dic[defaults._popup_playblast_key_]
		self.save = self.popup_prefs_dic[defaults._popup_save_key_]
		self.message = self.popup_prefs_dic[defaults._popup_message_key_]

	def creation_pop(self, message):
		if self.enable and self.creation:
			popup_ui.popup(message, self.duration, self.sound, defaults._creation_pop_icon_).pop()

	def publish_pop(self, message):
		if self.enable and self.publish:
			popup_ui.popup(message, self.duration, self.sound, defaults._publish_pop_icon_).pop()

	def playblast_pop(self, message):
		if self.enable and self.playblast:
			popup_ui.popup(message, self.duration, self.sound, defaults._playblast_pop_icon_).pop()

	def ticket_pop(self, message):
		if self.enable:
			popup_ui.popup(message, self.duration, self.sound, defaults._ticket_pop_icon_).pop()

	def closed_ticket_pop(self, message):
		if self.enable:
			popup_ui.popup(message, self.duration, self.sound, defaults._closed_ticket_pop_icon_).pop()

	def save_pop(self):
		if self.enable and self.save:
			save_popup_ui.popup(2000, 0).pop()

	def xp_pop(self, message):
		if self.enable:
			popup_ui.popup(message, self.duration, self.sound, defaults._xp_pop_icon_).pop()

	def message_pop(self, message):
		if self.enable and self.message:
			popup_ui.popup(message, self.duration, self.sound, defaults._message_pop_icon_).pop()

	def server_pop(self, message):
		if self.message:
			popup_ui.popup(message, 3000, self.sound, defaults._server_running_gif_).pop()

	def no_server_pop(self, message):
		if self.message:
			popup_ui.popup(message, 7000, self.sound, defaults._server_running_gif_).pop()

	def new_chat_user_pop(self, message):
		if self.message:
			popup_ui.popup(message, 3000, self.sound, defaults._new_user_chat_icon_).pop()

	def remove_pop(self, message):
		if self.message:
			popup_ui.popup(message, 3000, self.sound, defaults._remove_pop_icon_).pop()