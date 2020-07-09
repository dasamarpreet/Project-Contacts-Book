print()

"""This delete function is added in the last of the allcontact.py file, 
because on deleting we don't want to open a new window. We're just writing
delete file code here to understand it only and hence we commented all lines."""

print()

# def delete_contact(self):
#     selected_contact = self.list_box.curselection()
#     contact = self.list_box.get(selected_contact)
#     person_id = contact.split(".")[0]
#
#     query = "DELETE FROM contactbook WHERE person_id = {}".format(person_id)
#     string_for_msgbox = 'Are you sure, you want to delete ' + contact.split(".")[1] + "?"
#     answer = messagebox.askquestion('Warning', string_for_msgbox)
#     if answer == 'yes':
#         try:
#             cursor.execute(query)
#             conn.commit()
#             messagebox.showinfo('Success', 'Contact Deleted')
#             self.destroy()
#
#         except Exception as e:
#             messagebox.showinfo('Info', str(e))
