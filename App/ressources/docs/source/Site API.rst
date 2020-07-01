==========
Site API
==========

Wizard contain some easy functions that you can use to create plugins, access the assets, 
create PyQt5 widgets and access the projects and users information.

Users
=====

Create a user
^^^^^^^^^^^^^

First import the "site" class from wizard/prefs/site ::

	from wizard.prefs.site import site

Then create a user using the "create_user() function" ::

	site().create_user( add_user_name = John,
					  promotion = Staff,
					  email = John@gmail.com,
					  password = 1234,
					  admin = 0 )
	>> 1

If the creation failed, wizard return a warning

Get the users list
^^^^^^^^^^^^^^^^^^

The function "get_users_list()" return the users as a Python list ::

	site().get_users_list()
	>> ["John", "Albert", "Maria"]

Change a user password
^^^^^^^^^^^^^^^^^^^^^^

The function "change_user_password()" need two arguments :
	- <user> ( The user you want to access )
	- <password> ( The new password )

The function exectute only if the requested user is in the users list, else return a warning ::

	site().change_user_password("John", "abcde8Fa")

Access a user data
^^^^^^^^^^^^^^^^^^

You can access a user email using the "get_email_from_user()" function ::

	site().get_email_from_user("John")
	>> John@gmail.com

You can access a user promotion using the "get_user_promotion()" function ::

	site().get_user_promotion("John")
	>> Staff

You can check if the user is as administrator using the "get_user_admin()" function ::

	site().get_user_admin("John")
	>> None

Set a user as current
^^^^^^^^^^^^^^^^^^^^^

First import the "prefs" class from wizard/prefs/main ::

	from wizard.prefs.main import prefs

You can set a user as current user using the "set_user" function ::

	prefs().set_user("John")

You can also get the current user using the "user" property ::

	prefs().user
	>>John

You can unlog a user using the "leave_user" function ::

	prefs().leave_user()

Access data from the current user
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get the promotion of the current user ::

	prefs().promotion
	>>Staff

Get the avatar image of the current user ::
	
	prefs().user_image
	>>../Data/Avatars/John.png

Get the email of the current user ::

	prefs().user_email
	>>John@gmail.com

Check if the current user is administrator ::

	prefs().admin
	>>None

Projects
========

Create a project
^^^^^^^^^^^^^^^^

First import the "create" class from wizard/project ::

	from wizard.project import create

Then you can create a project using the function "create_project"

This function need 7 arguments :

    - <project_name> The name of your project
    - <path> The base path of your project, knowing that wizard will create a folder named by your project name
    - <frame_rate> as an int
    - <format> The valids formats are ['NTSC', 'HD 720', 'HD 1080', ''SCOPE 2K', 'UHD 4K']
    - <color_managment> The vailds color managments arguments are ['sRGB', 'Aces cg']
    - <sampling_rate> The valid samplings rates arguments are ['24 000 Hz', '48 000 Hz', '96 000 Hz']
    - <password>

::
	
	create.create_project(project_name = "MyFilm",
						  path = "D:/projects/",
						  frame_rate = 24,
						  format = "UHD 4K",
						  color_management = "Aces cg",
						  sampling_rate = "48 000 Hz",
						  password = "myproject1234")
 	>>1

Get all the existing projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First import the "prefs" class form wizard/prefs/main::

	from wizard.prefs.main import prefs

Then with the property "projects" in the child class "site" you can access the projects names list::

	prefs().site.projects
	>>["MyFilm", "Indiana Jones", "MyProject"]

Set a project as current project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the function "change_project" in the "prefs" class and pass an existing project name argument as string::

	prefs().change_project("Indiana Jones")
	>>1

Access datas from the current project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Access the current project name and path ::

	prefs().project_name
	prefs().project_path
	>>Indiana Jones
	>>D:/projects/Indiana Jones/

Access the color management, frame rate and format::

	prefs().color_namagment
	prefs().frame_rate
	prefs().format
	>>Aces cg
	>>24
	>>UHD 4K

