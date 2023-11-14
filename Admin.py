# user.py



from privileges import Admin

# Create an Admin instance
admin_user = Admin("John", "Doe", 30, ["can add post", "can delete post", "can ban user"])

# Call the show_privileges method
admin_user.privileges.show_privileges()

